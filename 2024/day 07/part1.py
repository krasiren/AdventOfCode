with open('2024/day 07/input.txt', 'r') as f:
	lines = f.read().split('\n')

def do_operations(items: list, result):
	if len(items) == 2:
		a, b = items
		return (result == eval(a+'+'+b)) + (result == eval(a+'*'+b))
	
	a = items.pop(0)
	b = items.pop(0)

	sum_ = items.copy()
	prod_ = items.copy()

	sum_.insert(0, str(eval(a+'+'+b)))
	prod_.insert(0, str(eval(a+'*'+b)))

	return do_operations(sum_, test_value) + do_operations(prod_, test_value)
	
	

calibration_result = 0
for equation in lines:
	test_value, factors = equation.split(': ')
	
	factors = factors.split(' ')
	test_value = int(test_value)

	if do_operations(factors, test_value):
		calibration_result += test_value


print(calibration_result)
		