import re

with open("input.txt", 'r') as f:
    text = f.read()

def find_uncorrupted(part_one):
    total = 0
    do = True
    print(text)
    for i, j, k in re.findall("mul\(([0-9]+),([0-9]+)\)|(do\(\)|don't\(\))", text):
        if k == "do()":
            do = True
        elif k == "don't()":
            do = False
        else:
            if do or part_one:
                total += int(i) * int(j)
    return total

print(f"Part one: {find_uncorrupted(True)}")
print(f"Part two: {find_uncorrupted(False)}")
