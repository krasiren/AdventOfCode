from pathlib import Path


def can_fit_presents(shape, values, presents):
	return True


if __name__ == '__main__':
	with Path(__file__).with_name('input.txt').open() as f:
		data = f.read()


	splits = data.split('\n\n')

	presents = []
	for block in splits[:-1]:
		presents.append(block.splitlines()[1:])

	total = 0
	for line in splits[-1].splitlines():
		key, value = line.split(': ')
		grid_shape = tuple(map(int, key.split('x')))
		values = list(map(int, value.split(' ')))

		total += can_fit_presents(grid_shape, values, presents)

	print(total)
