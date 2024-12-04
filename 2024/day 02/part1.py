with open('2024/day 02/input.txt', 'r') as f:
	lines = f.readlines()

num_safe_reports = 0
for report in lines:
	levels = report.replace('\n', '').split(' ')
	first = int(levels[0])
	increasing = None
	is_current_safe = True

	for level in levels[1:]:
		current = int(level)	# parse to int

		# firstly initialize the direction (+1 or -1)
		if increasing is None:
			increasing = 1 if current - first >= 0 else -1

		# beautiful
		if increasing * (current - first) not in {1, 2, 3}:
			is_current_safe = False
			break

		first = current

	if is_current_safe:
		num_safe_reports += 1

print(num_safe_reports)