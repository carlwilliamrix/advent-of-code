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

total_distance = sum(abs(l * right_sorted.count(l)) for l, r in zip(left_sorted, right_sorted))

print(total_distance)
#18997088