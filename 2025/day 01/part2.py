from pathlib import Path

with (Path(__file__).parent / 'input.txt').open('r') as f:
    lines = f.read().splitlines()


def rotate(n,  direction, rotate_num):
    zero = 0
    while rotate_num > 0:
        if direction == 'L':
            n -= 1
            if n < 0:
                n = 99
        else:
            n += 1
            if n > 99:
                n = 0
        rotate_num -= 1
        if n == 0:
            zero += 1
    return n, zero


total_zeros = 0
num = 50
for line in lines:
    zero_start = False
    rotate_num = int(line[1:])

    num, crosses = rotate(num, line[0], rotate_num)
    total_zeros += crosses

print(total_zeros)
