from functools import cmp_to_key
import networkx as nx

with open("input.txt") as f:
    data = f.read().strip().split("\n\n")

rules = [tuple(map(int, line.split("|"))) for line in data[0].split("\n")]
updates = [tuple(map(int, line.split(","))) for line in data[1].split("\n")]

def is_valid_update(u, r):
    for a, b in r:
        if a in u and b in u:
            if u.index(a) > u.index(b):
                return False
    return True

def find_middle_page(u):
    n = len(u)
    return update[n // 2]



valid_updates = []
middle_page_sum = 0
middle_page_sum_part_two = 0

for update in updates:
    if is_valid_update(update, rules):
        valid_updates.append(update)
        middle_page_sum += find_middle_page(update)



print(f"Part one: {middle_page_sum}")
# 5391

# Idea https://docs.python.org/3/library/functools.html#functools.cmp_to_key
#cmp = cmp_to_key(lambda x, y: -((x, y) in rules))

# for update in valid_updates:
#     print(update)
#     sorted_applied_updates = sorted(update, key=cmp)
#     print(f" hi {sorted_applied_updates}")
#     middle_page_sum += find_middle_page(sorted_applied_updates)
unsorted_updates = {
    update
    for update in updates
    if any(
        a in update and b in update and update.index(a) > update.index(b)
        for a, b in rules
    )
}
# Part 2
sorted_updates = [list(nx.topological_sort(nx.DiGraph((a, b) for a, b in rules if a in update and b in update))) for update in valid_updates]

print(sum(update[len(update) // 2] for update in sorted_updates))


