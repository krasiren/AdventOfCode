from operator import add, mul
from functools import reduce
from pathlib import Path


with (Path(__file__).parent / 'input.txt').open() as f:
    lines = f.read().splitlines()

# Manually add spaces to make all lines the same length
assert all(len(l) == len(lines[0]) for l in lines)

problems = []
problem_operations = []
for j in range(len(lines[0])):
    if lines[-1][j] in ('+', '*'):
        problem_operations.append(lines[-1][j])
        problems.append([])
    column_num = ''
    for i in range(len(lines)-1):
        column_num += lines[i][j].strip()
    if column_num:
        problems[-1].append(int(column_num))


print(sum(reduce(add if problem_operations[i] == '+' else mul, problems[i]) for i in range(len(problems))))
