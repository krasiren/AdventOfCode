with open('2024/day 01/input.txt', 'r') as f:
	lines = f.readlines()

left = []
right = []
for l in lines:
	nums = l.split('   ')
	left.append(int(nums[0]))
	right.append(int(nums[1]))

# how many times a number appears in THEIR OWN list
right_count = {}
for n in right:
	if n in right_count:
		right_count[n] += 1
	else:
		right_count[n] = 1

# finally get the similarity
similarty = 0
for n in left:
	if n in right_count:
		similarty += n * right_count[n]

print(similarty)