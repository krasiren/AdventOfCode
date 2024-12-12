class Antena():
	def __init__(self, location, freq):
		self.location = location	# i, j
		self.frequency = freq

	def get_antinode_dir(self, other):
		di = other.location[0]-self.location[0]
		dj = other.location[1]-self.location[1]
		return di, dj
	

class Antinode():
	def __init__(self, direction, start):
		self.direction = direction
		self.start_location = start

	def get_inboud_accurances(self, array):
		c = 0
		i, j = self.start_location
		while i>=0 and j>=0 and i<len(array) and j<len(array[0]):
			if not array[i][j]:
				c += 1
				array[i][j] = True
			i += self.direction[0]
			j += self.direction[1]

		return c, array


if __name__ == '__main__':
	with open('2024/day 08/input.txt', 'r') as f:
		lines = f.read().split('\n')

	antenas = []
	for i, line in enumerate(lines):
		for j, c in enumerate(line):
			if c != '.':
				antenas.append(Antena((i, j), c))

	antinodes = []
	for first in antenas:
		for second in antenas:
			if first != second:
				if first.frequency == second.frequency:
					antinodes.append(Antinode(first.get_antinode_dir(second), second.location))

	antinode_map = [[False for _ in l] for l in lines]
	count_unique = 0
	for antinode in antinodes:
		counted, antinode_map = antinode.get_inboud_accurances(antinode_map)
		count_unique += counted

	print(count_unique)
	# print( "\n".join( ["".join(['#' if e else '.' for e in row]) for row in antinode_map] ) )