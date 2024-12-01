f = open('input.txt', 'r')
lines = f.readlines()
left = []
right = []

# Split the input file
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

# Sort lists
left_sorted = sorted(left)
right_sorted = sorted(right)

# Sum the total "distance" between each line
# Combine two list element lines into pairs
# Compute the absolute difference between each pair of elements l and r, then sum the up
total_distance = sum(abs(l-r) for l, r in zip(left_sorted, right_sorted))

print(total_distance)