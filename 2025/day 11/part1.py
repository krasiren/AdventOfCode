
from pathlib import Path


def count_paths(start) -> int:
	if 'out' in racks[start]:
		return 1
	return sum(count_paths(rack) for rack in racks[start])


if __name__ == '__main__':
	with Path(__file__).with_name('input.txt').open() as f:
		lines = f.read().splitlines()

	racks = {}
	first_rack = None
	for line in lines:
		key, values = line.split(': ')
		racks[key] = values.split(' ')

		if key == 'you':
			first_rack = key

	print(count_paths(first_rack))
