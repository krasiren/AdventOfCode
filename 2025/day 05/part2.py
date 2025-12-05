with open('2025/day 05/input.txt', 'r') as f:
    lines = f.read().splitlines()

line_split_ix = lines.index('')

ranges = []
for line in lines[:line_split_ix]:
    start, end = line.split('-')
    ranges.append((int(start), int(end)))


def join_ranges(all_ranges):
    merged = []
    for i, r in enumerate(all_ranges):
        f_start, f_end = r
        was_merged = False
        for j, rs in enumerate(all_ranges):
            s_start, s_end = rs
            if i == j:
                continue
            if (f_start <= s_start <= f_end) or (f_start <= s_end <= f_end):
                merged.append((min(f_start, s_start), max(f_end, s_end)))
                was_merged = True

        if not was_merged:
            merged.append(r)

    return list(set(merged))


while True:
    new_ranges = join_ranges(ranges)
    if len(new_ranges) == len(ranges):
        break
    ranges = new_ranges


num_ids = 0
for start, end in ranges:
    num_ids += end - start + 1

print(num_ids)

