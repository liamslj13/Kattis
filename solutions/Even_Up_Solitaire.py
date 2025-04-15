n = int(input())
nums = input().split()
stack = []


for num in nums:
    if not stack:
        stack.append(int(num))
        continue

    if (stack[-1] + int(num)) % 2 == 0:
        stack.pop()
    else:
        stack.append(int(num))

print(len(stack))