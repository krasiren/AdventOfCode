with open('2024/day 04/input.txt', 'r') as f:
	lines = f.read().split('\n')
	
# These two may not be needed
def is_legit(num):
	if num < 0 or num >= len(lines):
		raise Exception('Wrong index')
	return num

def find_words(start_i, start_j, dir_i=None, dir_j=None, char_ix=0):
	# if we found all letters in the `word` increase counter (return 1)
	if char_ix == 4:
		return 1
	
	# The first time we come in this function (form double for loop),
	# return the sum of all directions
	if dir_i is None and dir_j is None:
		return sum([find_words(start_i, start_j, ver, hor, char_ix+1) 
			  for hor in {-1, 0, 1} for ver in {-1, 0, 1}])
	
	# A condition to check for valid indeces
	try:
		cur_i = is_legit(start_i + dir_i)
		cur_j = is_legit(start_j + dir_j)
	except:
		return 0
	
	if lines[cur_i][cur_j] == word[char_ix]:
		return find_words(cur_i, cur_j, dir_i, dir_j, char_ix+1)
	return 0


# Go through all characters and for every `X` search in all directions
word = ['X', 'M', 'A', 'S']
counter = 0
for i, row in enumerate(lines):
	for j, char in enumerate(row):
		if char == 'X':
			counter += find_words(i, j)

print(counter)