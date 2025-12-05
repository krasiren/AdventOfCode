with open('2025/day 04/input.txt', 'r') as f:
    lines = f.read().splitlines()

diagram = [[c for c in line] for line in lines]


def is_accessible(row, col):
    options = [(row-1, col), (row-1, col+1), (row, col+1), (row+1, col+1), (row+1, col), (row+1, col-1), (row, col-1), (row-1, col-1)]

    count = 0
    for r, c in options:
        if 0 <= r < len(diagram) and 0 <= c < len(diagram[r]):
            if diagram[r][c] == '@':
                count += 1

            if count >= 4:
                return False
    return True


total = 0
for i, line in enumerate(diagram):
    for j, c in enumerate(line):
        if c == '@':
            if is_accessible(i, j):
                total += 1

print(total)
