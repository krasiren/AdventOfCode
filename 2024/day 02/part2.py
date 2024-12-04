with open('2024/day 02/input.txt', 'r') as f:
	lines = f.readlines()

def is_report_safe(arr):
	first = int(arr[0])
	increasing = None
	for level in arr[1:]:
		current = int(level)	# parse to int

		# firstly initialize the direction (+1 or -1)
		if increasing is None:
			increasing = 1 if current - first >= 0 else -1

		# beautiful
		if increasing * (current - first) not in {1, 2, 3}:
			return False
		first = current
	return True

num_safe_reports = 0
for report in lines:
	levels = report.replace('\n', '').split(' ')

	if is_report_safe(levels):
		num_safe_reports += 1
	else:
		for ix in range(len(levels)):
			levels_copy = [el for i, el in enumerate(levels) if i != ix]
			if is_report_safe(levels_copy):
				num_safe_reports += 1
				break

print(num_safe_reports)