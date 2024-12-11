with open('2024/day 05/input.txt', 'r') as f:
	file = f.read()

def is_ordered(array):
	for a, b in zip(array[:-1], array[1:]):
		if not b in rules_dic[a][1]:
			return False
	return True
		

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

	if is_ordered(current_pages):
		add_middle_pages += int(current_pages[(len(current_pages)-1) // 2])

print(add_middle_pages)