def bank_joltage(bank: str) -> int:
    tenths, tenths_ix = 0, 0
    for i, c in enumerate(bank[:-1]):
        c = int(c)
        if c > tenths:
            tenths = c
            tenths_ix = i
        if c == 9:
            break

    ones = 0
    for c in bank[tenths_ix + 1:]:
        c = int(c)
        if c > ones:
            ones = c

    return int(f'{tenths}{ones}')


if __name__ == '__main__':
    with open('2025/day 03/input.txt', 'r') as f:
        lines = f.read().splitlines()

    print(sum(bank_joltage(line) for line in lines))
