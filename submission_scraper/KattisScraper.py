"""
DISCLAIMER:
This script is entirely generated by Claude 3.7 Sonnet
with some prompt engineering done along the way. There
will be issues and it is very slow. However, it is
easy to use. For more information, ensure you have looked
at the README for the script.
"""


import os
import re
import time
import requests
from bs4 import BeautifulSoup
import getpass


class KattisScraper:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://open.kattis.com"
        self.login_url = f"{self.base_url}/login/email"
        self.submissions_url = f"{self.base_url}/submissions"
        self.output_dir = "solutions"

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def login(self, username, password):
        print(f"Logging in as {username}...")

        response = self.session.get(self.login_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        token_element = soup.find('input', {'name': 'csrf_token'})

        if token_element is None:
            token_element = soup.find('input', {'type': 'hidden'})

            if token_element is None:
                print("Could not find CSRF token. The login page structure might have changed.")
                print("Attempting to login without CSRF token...")
                token = ""
            else:
                token = token_element.get('value', '')
        else:
            token = token_element['value']

        login_data = {
            'user': username,
            'password': password,
            'submit': 'Submit'
        }

        if token:
            login_data['csrf_token'] = token

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': self.login_url
        }

        response = self.session.post(self.login_url, data=login_data, headers=headers)

        if "My submissions" in response.text or username.lower() in response.text.lower():
            print("Login successful!")
            return True
        else:
            profile_response = self.session.get(f"{self.base_url}/users/{username}")
            if "Submissions" in profile_response.text and not "Login" in profile_response.text:
                print("Login seems successful!")
                return True
            else:
                print("Login failed. Please check your username and password.")
                print("The Kattis login process might have changed.")
                return False

    def get_all_submission_ids(self, username):
        print("Getting list of all submissions...")
        submission_ids = []
        page = 0

        personal_submissions_url = f"{self.base_url}/users/{username}"
        response = self.session.get(personal_submissions_url)

        if response.status_code != 200:
            print(f"Could not access personal submissions page: {personal_submissions_url}")
            print("Trying general submissions page instead...")
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            submission_links = soup.select('a[href*="/submissions/"]')

            if not submission_links:
                print("No submission links found on personal page. Trying table rows...")
                submission_rows = soup.select('table.table-submissions tr') or soup.select('table tr')

                if len(submission_rows) <= 1:
                    print("No submission rows found on personal page. Trying general submissions page...")
                else:
                    print(f"Found {len(submission_rows) - 1} potential submission rows on personal page.")

                    for row in submission_rows[1:]:
                        links = row.select('a')

                        submission_id = None
                        problem_name = None
                        status = None

                        for link in links:
                            href = link.get('href', '')
                            if '/submissions/' in href:
                                submission_id = href.split('/')[-1]
                            elif '/problems/' in href:
                                problem_name = link.text.strip()

                        status_cells = row.select('td')
                        for cell in status_cells:
                            cell_text = cell.text.strip().lower()
                            if 'accepted' in cell_text:
                                status = 'Accepted'
                                break

                        if submission_id and problem_name and status == 'Accepted':
                            submission_ids.append((submission_id, problem_name))

                    if submission_ids:
                        print(f"Found {len(submission_ids)} accepted submissions on personal page.")
                        return submission_ids
            else:
                print(f"Found {len(submission_links)} submission links on personal page.")

                for link in submission_links:
                    submission_id = link['href'].split('/')[-1]

                    row = link.find_parent('tr')
                    problem_name = None
                    status = None

                    if row:
                        problem_link = row.select_one('a[href*="/problems/"]')
                        if problem_link:
                            problem_name = problem_link.text.strip()

                        status_cells = row.select('td')
                        for cell in status_cells:
                            cell_text = cell.text.strip().lower()
                            if 'accepted' in cell_text:
                                status = 'Accepted'
                                break

                    if submission_id and problem_name and status == 'Accepted':
                        submission_ids.append((submission_id, problem_name))

                if submission_ids:
                    print(f"Found {len(submission_ids)} accepted submissions on personal page.")
                    return submission_ids
                else:
                    print(
                        "Found submission links but couldn't extract complete information. Trying general submissions page...")

        while True:
            response = self.session.get(f"{self.submissions_url}?page={page}")

            print(f"Checking submissions page {page + 1}, response status: {response.status_code}")

            if response.status_code != 200:
                print(f"Failed to access {self.submissions_url}?page={page}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')

            submissions = (
                    soup.select('tr[data-submission-id]') or
                    soup.select('tr.submission') or
                    soup.select('table.table-submissions tr') or
                    soup.select('table tr')
            )

            if not submissions or len(submissions) <= 1:
                print(f"No submissions found on page {page + 1}")

                page_text = soup.get_text()[:500]
                print("Page content preview:")
                print(page_text.strip())

                if page == 0:
                    links = soup.select('a')
                    for link in links:
                        href = link.get('href', '')
                        text = link.text.strip().lower()
                        if 'submission' in text and href:
                            print(f"Found possible submissions link: {text} -> {href}")

                            new_url = href if href.startswith('http') else f"{self.base_url}{href}"
                            print(f"Following link to: {new_url}")

                            new_response = self.session.get(new_url)
                            if new_response.status_code == 200:
                                new_soup = BeautifulSoup(new_response.text, 'html.parser')
                                new_submissions = (
                                        new_soup.select('tr[data-submission-id]') or
                                        new_soup.select('tr.submission') or
                                        new_soup.select('table.table-submissions tr') or
                                        new_soup.select('table tr')
                                )

                                if len(new_submissions) > 1:
                                    print(f"Found {len(new_submissions) - 1} submissions at {new_url}")
                                    submissions = new_submissions
                                    break

                if len(submissions) <= 1:
                    break

            new_submissions_found = 0

            for submission in submissions[1:]:
                submission_id = None

                if 'data-submission-id' in submission.attrs:
                    submission_id = submission['data-submission-id']
                else:
                    link = submission.select_one('a[href*="/submissions/"]')
                    if link:
                        submission_id = link['href'].split('/')[-1]

                if not submission_id:
                    continue

                problem_name = None
                problem_link = (
                        submission.select_one('td:nth-child(2) a') or
                        submission.select_one('a[href*="/problems/"]')
                )

                if problem_link:
                    problem_name = problem_link.text.strip()

                if not problem_name:
                    continue

                status_elem = (
                        submission.select_one('td:nth-child(4)') or
                        submission.select_one('.status') or
                        submission.select_one('td')
                )

                if status_elem:
                    status = status_elem.text.strip()
                    if "Accepted" in status:
                        submission_ids.append((submission_id, problem_name))
                        new_submissions_found += 1

            if new_submissions_found == 0:
                break

            print(f"Found {len(submission_ids)} accepted submissions so far (page {page + 1})...")
            page += 1
            time.sleep(1)

        return submission_ids

    def get_solution_code(self, submission_id):
        print(f"Accessing submission page for ID: {submission_id}")
        response = self.session.get(f"{self.base_url}/submissions/{submission_id}")

        if response.status_code != 200:
            print(f"Failed to get submission {submission_id}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for download buttons or links to source code
        download_links = soup.select('a[href*="/source/"]') or soup.select('a[href*="/submissions/"][href*="/source/"]')
        for link in download_links:
            href = link.get('href', '')
            if '/source/' in href and ('download' in href.lower() or
                                       link.find('button') is not None or
                                       'download' in link.text.lower()):
                source_url = href if href.startswith('http') else f"{self.base_url}{href}"
                print(f"Found download link: {source_url}")

                source_response = self.session.get(source_url)
                if source_response.status_code == 200:
                    return source_response.text

        # If no download link found, try to find the source code directly on the page
        source_code = (
                soup.select_one('pre.source-content') or
                soup.select_one('pre.prettyprint') or
                soup.select_one('pre code') or
                soup.select_one('pre')
        )

        if source_code:
            return source_code.text

        # Check for iframe that might contain code
        iframes = soup.select('iframe')
        if iframes:
            for iframe in iframes:
                src = iframe.get('src', '')
                if src:
                    iframe_url = src if src.startswith('http') else f"{self.base_url}{src}"
                    print(f"Found iframe, accessing: {iframe_url}")

                    iframe_response = self.session.get(iframe_url)
                    if iframe_response.status_code == 200:
                        iframe_soup = BeautifulSoup(iframe_response.text, 'html.parser')
                        iframe_code = (
                                iframe_soup.select_one('pre.source-content') or
                                iframe_soup.select_one('pre.prettyprint') or
                                iframe_soup.select_one('pre code') or
                                iframe_soup.select_one('pre')
                        )

                        if iframe_code:
                            return iframe_code.text

        print(f"Could not find source code for submission {submission_id}.")
        print("This might be due to access restrictions or different page structure.")
        return None

    def determine_file_extension(self, code):
        if "#include <" in code or "#include<" in code:
            return ".cpp"
        elif "import java." in code or "public class" in code:
            return ".java"
        elif "import " in code and ("def " in code or "print(" in code):
            return ".py"
        elif "using namespace" in code:
            return ".cpp"
        elif "func main" in code and "package main" in code:
            return ".go"
        elif "console.log" in code or "function " in code:
            return ".js"
        elif "<?php" in code:
            return ".php"
        elif "#include <" in code and "int main" in code:
            return ".c"
        else:
            return ".txt"

    def download_all_solutions(self, username):
        submission_ids = self.get_all_submission_ids(username)

        if not submission_ids:
            print("No accepted submissions found.")
            return False

        print(f"Found {len(submission_ids)} accepted submissions. Downloading solutions...")

        downloaded_problems = set()
        downloaded_count = 0

        for idx, (submission_id, problem_name) in enumerate(submission_ids):
            if problem_name in downloaded_problems:
                continue

            print(f"Downloading solution for '{problem_name}' ({idx + 1}/{len(submission_ids)})...")

            code = self.get_solution_code(submission_id)

            if code:
                safe_name = re.sub(r'[^\w\-_]', '_', problem_name)
                extension = self.determine_file_extension(code)

                filename = f"{self.output_dir}/{safe_name}{extension}"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(code)

                print(f"Saved: {filename}")
                downloaded_problems.add(problem_name)
                downloaded_count += 1
            else:
                print(f"Failed to download solution for {problem_name}")
                print("You may want to manually check this submission at:")
                print(f"{self.base_url}/submissions/{submission_id}")

            time.sleep(1)

        return downloaded_count > 0


def main():
    scraper = KattisScraper()

    username = input("Enter your Kattis username: ")
    password = getpass.getpass("Enter your Kattis password: ")

    if scraper.login(username, password):
        print("\nAfter login, please check if you have permission to view your submission source code.")
        print("Open a submission in your browser and see if you can view the source code.")
        proceed = input("Can you view your source code in the browser? (y/n): ").lower()

        if proceed != 'y':
            print("\nIt seems you may not have permission to view the source code of your submissions.")
            print("This can happen due to various reasons:")
            print("1. The course/contest settings may restrict access to your own solution code")
            print("2. Some educational institutions limit access to past solutions")
            print("3. Your session might not have the right permissions")
            print("\nSuggestions:")
            print("- Try logging in to Kattis directly in your browser and see if you can view your solutions")
            print("- Check with your instructor or Kattis administrator about access permissions")
            print("- Try downloading solutions from a different Kattis instance if you're using one")
            exit(0)

        if scraper.download_all_solutions(username):
            print(f"\nAll solutions downloaded to '{scraper.output_dir}' directory!")
        else:
            print("\nNo solutions were downloaded. If you believe this is an error, please try:")
            print("1. Checking if you have any accepted submissions on Kattis")
            print("2. Verifying your username is correct")
            print("3. Manually downloading a few solutions to see if it's possible")
    else:
        print("Exiting due to login failure.")


if __name__ == "__main__":
    main()