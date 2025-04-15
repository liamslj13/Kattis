nums = input().split()
n, k = int(nums[0]), int(nums[1])

if k >= 350:
    print("Your wish is granted!")
else:
    if 2**k >= n:
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")