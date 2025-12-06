from operator import add, mul
from functools import reduce


with open('2025/day 06/input.txt', 'r') as f:
    lines = f.read().splitlines()


problems = []
problem_operations = []
for i, line in enumerate(lines):
    problem_ix = 0
    for el in line.split(' '):
        if not el:
            continue
        if i == 0:
            problems.append([int(el)])
        elif i == len(lines)-1:
            problem_operations.append(el)
        else:
            problems[problem_ix].append(int(el))
        problem_ix += 1

print(sum(reduce(add if problem_operations[i] == '+' else mul, problems[i]) for i in range(len(problems))))
