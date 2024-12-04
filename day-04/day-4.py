
with open("input.txt") as f:
    data = f.read().strip().split("\n")

print(data)

# Possibilities: left/right, right/left, up/down, down/up, diagonal down/up

total_xmas = 0
total_x_mas = 0

width = len(data[0])
height = len(data)

# Check left to right and right to left
for i in range(height):
    for j in range(width - 3):
        cur = data[i][j:j+4]
        if cur == "XMAS" or cur == "SAMX":
            total_xmas += 1

# Check up/down and down/up
for i in range(height-3):
    for j in range(width):
        cur = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
        if cur == "XMAS" or cur == "SAMX":
            total_xmas += 1

# Check diagonal down/up
for i in range(height-3):
    for j in range(width-3):
        cur_diag_down = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        if cur_diag_down == "XMAS" or cur_diag_down == "SAMX":
            total_xmas += 1
        cur_diag_up = data[i + 3][j] + data[i + 2][j + 1] + data[i + 1][j + 2] + data[i][j + 3]
        if cur_diag_up == "XMAS" or cur_diag_up == "SAMX":
            total_xmas += 1

# Check x-mas
for i in range(height-2):
    for j in range(width-2):
        cur_right = data[i][j] + data[i+1][j+1] + data[i+2][j+2]
        cur_left = data[i+2][j] + data[i+1][j+1] + data[i][j+2]
        if(cur_right == "MAS" or cur_right == "SAM") and (cur_left == "MAS" or cur_left == "SAM"):
            total_x_mas += 1


print(f"Total number of xmas: {total_xmas}")
# 2557

print(f"Total number of x-mas: {total_x_mas}")
# 1854