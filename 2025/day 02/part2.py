def num_invalid_ids(start, end):
    invalid_sum = 0
    for i in range(int(start), int(end) + 1):
        if is_invalid(str(i)):
            invalid_sum += i
    return invalid_sum


def is_invalid(n: str):
    l = len(n)
    for i in range(l//2, 0, -1):
        if l % i != 0:
            continue
        if n[:i] * (l // i) == n:
            print(n)
            return True
    return False


if __name__ == '__main__':
    with open('2025/day 02/input.txt', 'r') as f:
        line = f.read()

    ranges = line.split(',')

    cum_sum = 0
    for r in ranges:
        start, end = r.split('-')
        cum_sum += num_invalid_ids(start, end)

    print(cum_sum)
