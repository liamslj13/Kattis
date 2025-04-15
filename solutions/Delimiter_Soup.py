L = int(input())
bracket_string = input()

brackets = {")":"(", "]":"[", "}":"{"}
stack = []
i = 0
broken = False
for c in bracket_string:
    i += 1
    if c == ' ':
        continue

    if c == '(' or c == "[" or c == '{':
        stack.append(c)
    else:
        if not stack:
            broken = True
            break
        elif brackets[c] != stack[-1]:
            broken = True
            break
        else:
            stack.pop()

if broken:
    print(f"{c} {i-1}")
else:
    print("ok so far")