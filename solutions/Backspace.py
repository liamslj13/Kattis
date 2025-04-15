string = input()
heap = []

for char in string:
    if not heap and char == "<":
        continue
    elif char == "<":
        heap.pop()
    else:
        heap.append(char)

print("".join(heap))
