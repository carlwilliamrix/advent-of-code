f = open('input.txt', 'r')
data = f.readlines()
clean_data = [line.strip() for line in data]

# Part one
def check(r):
    row_sorted = sorted(r)
    row_sorted_reversed = sorted(r, reverse=True)
    if r == row_sorted:
        cur = r[0]
        for num in r[1:]:
            if num == cur or num > cur + 3:
                return False
            cur = num
    elif r == row_sorted_reversed:
        cur = r[0]
        for num in r[1:]:
            if num == cur or num < cur - 3:
                return False
            cur = num
    else:
        return False
    return True

def check_with_remove(r):
    # for i in range(len(r)):
    #     if check(r[:i] + r[i+1:]):
    #         return True
    # return False
    return any(check(r[:i] + r[i + 1:]) for i in range(len(r)))

safe = 0
safe_part_two = 0
for row in clean_data:
    split_row = [int(n) for n in row.split(' ')]
    if check(split_row):
        safe += 1
    elif check_with_remove(split_row):
        safe_part_two += 1

print(f"Safe for part one: {safe} and safe for part two: {safe_part_two} and total safe: {safe+safe_part_two}")
#369
#59
#428
