import re
from functools import lru_cache
from pathlib import Path

import numpy as np


def to_joltages(s):
    return [int(j) for j in s.split(',')]
    return np.array([int(j) for j in s.split(',')]).reshape(1, -1)


def to_vectors(lst, size: int):
    vecs = [[1 if i in map(int, b.split(',')) else 0 for i in range(size)] for b in lst]
    return vecs
    return np.array(vecs)


def parse_line_content(s):
    pattern = r'\[(.*?)\]|\((.*?)\)|\{(.*?)\}'
    matches = re.findall(pattern, s)
    matches = [it for m in matches for it in m if it]
    return matches[0], to_vectors(matches[1:-1], len(matches[0])), to_joltages(matches[-1])


def get_min_steps(end, vecs) -> int:
    @lru_cache
    def solve(current) -> int | float:
        if all(current[i] == end[i] for i in range(len(end))):
            return 0
        if any(current[i] > end[i] for i in range(len(end))):
            return float('inf')
        min_steps = float('inf')
        for v in vecs:
            steps = solve(tuple(current[i] + v[i] for i in range(len(end))))
            if steps < min_steps:
                min_steps = steps
        return min_steps + 1
    solve.cache_info()
    return int(solve(tuple([0] * len(end))))


if __name__ == "__main__":
    with Path(__file__).with_name('input.txt').open() as f:
        lines = f.read().splitlines()

    total = 0
    for i, line in enumerate(lines):
        _, buttons, joltage_levels = parse_line_content(line)

        print(i)
        t = get_min_steps(joltage_levels, buttons)
        total += t
    print(total)
