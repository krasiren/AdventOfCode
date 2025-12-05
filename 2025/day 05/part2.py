with open('2025/day 05/input.txt', 'r') as f:
    lines = f.read().splitlines()

line_split_ix = lines.index('')

ranges = []
for line in lines[:line_split_ix]:
    start, end = line.split('-')
    ranges.append((int(start), int(end)))


def find_pair(all_ranges):
    for i, r in enumerate(all_ranges):
        f_start, f_end = r
        for j, rs in enumerate(all_ranges):
            s_start, s_end = rs
            if i == j:
                continue
            if (f_start <= s_start <= f_end) or (f_start <= s_end <= f_end):
                return i, j, (min(f_start, s_start), max(f_end, s_end))

    return -1, -1, None


def merge_two_ranges(all_ranges, i, j, element):
    new_ranges = []
    for k, r in enumerate(all_ranges):
        if k != i and k != j:
            new_ranges.append(r)
    new_ranges.append(element)
    return new_ranges


while True:
    first_pos, second_pos, new_range = find_pair(ranges)
    if new_range is None:
        break
    ranges = merge_two_ranges(ranges, first_pos, second_pos, new_range)

num_ids = 0
for start, end in ranges:
    num_ids += end - start + 1

print(num_ids)

