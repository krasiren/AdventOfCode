with open('2025/day 05/input.txt', 'r') as f:
    lines = f.read().splitlines()

line_split_ix = lines.index('')

ranges = []
for line in lines[:line_split_ix]:
    start, end = line.split('-')
    ranges.append((int(start), int(end)))


num_fresh = 0
for line in lines[line_split_ix + 1:]:
    num = int(line)
    for start, end in ranges:
        if start <= num <= end:
            num_fresh += 1
            break

print(num_fresh)
