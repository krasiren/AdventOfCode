from part1 import Guard

if __name__ == '__main__':
	with open('2024/day 06/input.txt', 'r') as f:
		input = f.read()

	starting_map = []
	starting_position = (0, 0)
	for i, line in enumerate(input.split('\n')):
		if '^' in line:
			starting_position = (i, line.index('^'))
		starting_map.append([c for c in line])

	num_loops = 0
	# checking for valid obstacles
	for i, row in enumerate(starting_map):
		print(f"testing at row: {i}")
		for j, char in enumerate(row):
			if char == '.':
				current_copy = [[c for c in l] for l in starting_map]
				current_copy[i][j] = '#'

				big_g = Guard(starting_position)
				big_g.map_copy(current_copy)

				# test if looping
				is_loop = False
				while big_g.inside_map(big_g.next_position()):
					# print(big_g.patrolled_map)
					
					if big_g.can_move_forward():
						big_g.move()

						if big_g.is_in_loop():
							# print(big_g.position, big_g.direction)
							is_loop = True
							break
						big_g.update_positions_visited()
					else:
						big_g.turn()

				
				if is_loop:
					num_loops += 1

	print(num_loops)