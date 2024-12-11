class Guard():
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	patrolled_map: list[list[str]]
	unique_positions_visited = 1

	def __init__(self, position: tuple):
		self.position = position
		self.direction = 0

	def map_copy(self, array):
		self.patrolled_map = [[c for c in l] for l in array.copy()]

	def is_in_loop(self):
		i, j = self.position
		return self.patrolled_map[i][j] == self.direction
		return (len(self.moves_made) >= 4 and 
	  			self.moves_made[-1] == self.moves_made[-3] and
				self.moves_made[-2] == self.moves_made[-4])

	def mark_unique_location(self):
		i, j = self.position
		if self.patrolled_map[i][j] == '.':
			self.patrolled_map[i][j] = self.direction
			return 1
		return 0

	def inside_map(self, position=None):
		if not position:
			position = self.position
		return (position[0] >= 0 and 
				position[1] >= 0 and 
				position[0] < len(self.patrolled_map) and 
				position[1] < len(self.patrolled_map[1]))

	def can_move_forward(self):
		new_i = self.position[0] + self.directions[self.direction][0]
		new_j = self.position[1] + self.directions[self.direction][1]
		return self.patrolled_map[new_i][new_j] != '#'

	def move(self):
		self.position = self.next_position()

	def update_positions_visited(self):
		self.unique_positions_visited += self.mark_unique_location()

	def turn(self):
		self.direction = (self.direction + 1) % len(self.directions)

	def next_position(self):
		new_i = self.position[0] + self.directions[self.direction][0]
		new_j = self.position[1] + self.directions[self.direction][1]
		return new_i, new_j


if __name__ == '__main__':
	with open('2024/day 06/input.txt', 'r') as f:
		input = f.read()

	starting_map = []
	for i, line in enumerate(input.split('\n')):
		if '^' in line:
			big_g = Guard((i, line.index('^')))
		starting_map.append(line)

	big_g.map_copy(starting_map)

	# patroling
	while big_g.inside_map(big_g.next_position()):
		if big_g.can_move_forward():
			big_g.move()
			big_g.update_positions_visited()
		else:
			big_g.turn()

	print(big_g.unique_positions_visited)