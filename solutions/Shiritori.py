seen = set()
N = int(input())
broken = False

for i in range(0,N):
    word = input()
    if i != 0:
        if prev[-1] != word[0] and (i == 0 or i % 2 == 0):
            print("Player 1 lost")
            broken = True
            break
        elif prev[-1] != word[0]:
            print("Player 2 lost")
            broken = True
            break

    if word in seen:
        if i == 0 or i % 2 == 0:
            print("Player 1 lost")
        else:
            print("Player 2 lost")
        broken = True
        break
    seen.add(word)
    prev = word

if not broken:
    print("Fair Game")