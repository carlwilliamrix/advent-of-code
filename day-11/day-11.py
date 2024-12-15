from collections import Counter

with open("input.txt") as f:
    data = Counter(map(int, f.read().split()))

# try using a counter object
# https://www.geeksforgeeks.org/python-counter-objects-elements/

def split_stone(stone):
    str_stone = str(stone)
    mid = len(str_stone) // 2
    left = int(str_stone[:mid])
    right = int(str_stone[mid:])
    return left, right

def blink(stones, r):
    for i in range(r):
        after_blink = Counter()
        for stone, n in stones.items():
            if stone == 0:
                after_blink[1] += n
            elif len(str(stone)) % 2 == 0:
                left, right = split_stone(stone)
                after_blink[left] += n
                after_blink[right] += n
            else:
                after_blink[stone * 2024] += n
        stones = after_blink
    return sum(stones.values())

print(f"part one: {blink(data, 25)}")
#217812
print(f"part two: {blink(data, 75)}")