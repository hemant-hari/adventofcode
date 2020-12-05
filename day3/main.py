def is_tree(line: str, x: int):
    i = x%len(line)
    print(line[i], i, len(line), x%len(line), line+line+line)
    return line[i] == '#'

map = []
f = open("input.txt")
for line in f:
    map.append(line.strip())

x = 0
count = 0
i = 2
while i < len(map):
    line = map[i]
    x += 1
    if is_tree(line, x):
        count += 1
    i+=2

print(count)

#r1d1 = 68
#r3d1 = 268
#r5d1 = 73
#r7d1 = 75