with open('2024/day 01/input.txt', 'r') as f:
	lines = f.readlines()

first = []
second = []
for line in lines:
	a, b = int(line.split('   ')[0]), int(line.split('   ')[1])
	first.append(a)
	second.append(b)

first.sort()
second.sort()

sum = 0
for i in range(len(first)):
	sum += abs(first[i] - second[i])

print(sum)