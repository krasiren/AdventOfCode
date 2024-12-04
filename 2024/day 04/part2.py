with open('2024/day 04/input.txt', 'r') as f:
	lines = f.read().split('\n')

def find_x_mases(x, y, direction=None):
	def is_valid_x_mas():
		remaining = ['M', 'M', 'S', 'S']
		for k in range(1, 4):
			next_c = corners[(i+k) % 4]
			if lines[x+next_c[0]][y+next_c[1]] != remaining[k]:
				return False
		return True
	
	for i, corner in enumerate(corners):
		if lines[x+corner[0]][y+corner[1]] == 'M':
			if is_valid_x_mas():
				return 1
	
	return 0


# Go through all characters and for every `A` search for `MAS`
# Can skip outer walls, cuz `A` is in the center
# These must be cyclic (curently counter clock-wise)
corners = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
word = ['X', 'M', 'A', 'S']
counter = 0
for i, row in enumerate(lines):
	if i not in {0, len(lines)-1}:
		for j, char in enumerate(row):
			if j not in {0, len(lines[0])-1} and char == 'A':
				counter += find_x_mases(i, j)

print(counter)