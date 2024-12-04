import re

with open('2024/day 03/input.txt', 'r') as f:
	file = f.read()

n = '\d?\d?\d'
r_expr = f'mul\({n},{n}\)'

muls = re.findall(r_expr, file)

s = 0
for m in muls:
	a, b = re.findall(n, m)
	s += int(a)*int(b)

print(s)