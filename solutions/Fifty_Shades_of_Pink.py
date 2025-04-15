N = int(input())
count = 0

while N != 0:
    word = input().lower()
    if "pink" in word or "rose" in word:
        count += 1
    
    N -= 1
    
if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
