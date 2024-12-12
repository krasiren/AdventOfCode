class Antena():
	def __init__(self, location, freq):
		self.location = location	# i, j
		self.frequency = freq

	def get_antinode(self, other):
		di = other.location[0]-self.location[0]
		dj = other.location[1]-self.location[1]
		return self.location[0]-di, self.location[1]-dj
	

if __name__ == '__main__':
	with open('2024/day 08/input.txt', 'r') as f:
		lines = f.read().split('\n')

	antenas = []
	for i, line in enumerate(lines):
		for j, c in enumerate(line):
			if c != '.':
				antenas.append(Antena((i, j), c))

	antinodes = set()
	for first in antenas:
		for second in antenas:
			if first != second:
				if first.frequency == second.frequency:
					antinodes.add(first.get_antinode(second))

	count_unique = 0
	for antinode in antinodes:
		if (antinode[0] < len(lines) and antinode[0] >= 0 and
	  		antinode[1] < len(lines[0]) and antinode[1] >= 0):
			count_unique += 1

	print(count_unique)