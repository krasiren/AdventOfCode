with open('2025/day 01/input.txt', 'r') as f:
    lines = f.readlines()

total_zeros = 0
num = 50
for line in lines:
    dir = line[0]
    rotate_num = int(line[1:])
    if dir == 'L':
        num = (num - rotate_num) % 100
    elif dir == 'R':
        num = (num + rotate_num) % 100

    if num == 0:
        total_zeros += 1

print(total_zeros)
