
from pathlib import Path
from functools import lru_cache


@lru_cache
def count_paths(start, end) -> int:
	if 'out' != end and 'out' in racks[start]:
		return 0
	if end in racks[start]:
		return 1
	res = sum(count_paths(rack, end) for rack in racks[start])
	return res


if __name__ == '__main__':
	with Path(__file__).with_name('input.txt').open() as f:
		lines = f.read().splitlines()

	total = 0
	racks = {}
	first_rack = None
	for line in lines:
		key, values = line.split(': ')
		racks[key] = values.split(' ')

	s1 = count_paths('svr', 'fft')
	m1 = count_paths('fft', 'dac')
	e1 = count_paths('dac', 'out')
	total += (s1 * m1 * e1)

	s2 = count_paths('svr', 'dac')
	m2 = count_paths('dac', 'fft')
	e2 = count_paths('fft', 'out')
	total += (s2 * m2 * e2)

	print(total)
