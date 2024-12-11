with open('2024/day 07/input.txt', 'r') as f:
	lines = f.read().split('\n')

cached = {}

def do_operations(items: list, result):
	c_item = (tuple(items), result)

	if c_item in cached:
		return cached[c_item]
	
	if len(items) == 2:
		a, b = items
		cached[c_item] = ((result == eval(a+'+'+b)) or 
						  (result == eval(a+'*'+b)) or 
						  (result == int(a+b)))
		return cached[c_item]
	
	a = items.pop(0)
	b = items.pop(0)

	sum_ = items.copy()
	prod_ = items.copy()
	concat_ = items.copy()

	sum_.insert(0, str(eval(a+'+'+b)))
	prod_.insert(0, str(eval(a+'*'+b)))
	concat_.insert(0, a+b)

	return (do_operations(sum_, test_value) or 
			do_operations(prod_, test_value) or
			do_operations(concat_, test_value))
	
	

calibration_result = 0
i = 0
for equation in lines:
	test_value, factors = equation.split(': ')
	
	factors = factors.split(' ')
	test_value = int(test_value)

	if do_operations(factors, test_value):
		calibration_result += test_value

print()
print(calibration_result)
		