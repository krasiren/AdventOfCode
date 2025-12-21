from pathlib import Path


if __name__ == '__main__':
	with Path(__file__).with_name('input.txt').open() as f:
		lines = f.read().splitlines()
