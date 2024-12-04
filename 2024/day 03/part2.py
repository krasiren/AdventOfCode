import re

with open('2024/day 03/input.txt', 'r') as f:
	file = f.read()

n = '\d?\d?\d'
mul_expr = f'mul\({n},{n}\)'
do_expr = 'do\(\)'
dont_expr = "don't\(\)"

all_expressions = re.findall(f"{mul_expr}|{do_expr}|{dont_expr}", file)

s = 0
is_next_mul_enabled = True

for expr in all_expressions:
	if expr.startswith('mul'):
		if is_next_mul_enabled:
			a, b = re.findall(n, expr)
			s += int(a)*int(b)

	elif expr == 'do()':
		is_next_mul_enabled = True
	else:
		is_next_mul_enabled = False

print(s)