with open('2024/day 05/input.txt', 'r') as f:
	file = f.read()

def is_ordered(array):
	for a, b in zip(array[:-1], array[1:]):
		if not b in rules_dic[a][1]:
			return False
	return True

def get_dict_greater(array):
	"""Returns a dictionary where keys are items of the `array` and values are the number of 
	pages that should be printed before it."""
	greater = {}
	for a in array:
		for b in array:
			if a != b:
				if a not in greater:
					greater[a] = 0
				if b in rules_dic[a][1]:
					greater[a] += 1
	return greater
		

rules, updates = file.split('\n\n')

rules_dic = {}
for rule in rules.split('\n'):
	a, b = rule.split('|')

	if b not in rules_dic:
		rules_dic[b] = [[a], []]
	else:
		rules_dic[b][0].append(a)

	if a not in rules_dic:
		rules_dic[a] = [[], [b]]
	else:
		rules_dic[a][1].append(b)

add_middle_pages = 0
for update in updates.split('\n'):
	current_pages = update.split(',')

	if not is_ordered(current_pages):
		num_greater = get_dict_greater(current_pages)
		ordered_pages = sorted(current_pages, key=lambda x: num_greater[x])
		add_middle_pages += int(ordered_pages[(len(ordered_pages)-1) // 2])

print(add_middle_pages)