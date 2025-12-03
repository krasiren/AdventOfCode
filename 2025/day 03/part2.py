from pathlib import Path


def bank_joltage(bank: str, start_ix=0, sub_bank=11) -> str:
    if sub_bank < 0:
        return ''

    place, place_ix = 0, 0
    for i, c in enumerate(bank[start_ix:len(bank)-sub_bank]):
        c = int(c)
        if c > place:
            place = c
            place_ix = i + start_ix
        if c == 9:
            break

    return str(place) + bank_joltage(bank, place_ix + 1, sub_bank - 1)


if __name__ == '__main__':
    with (Path(__file__).parent / 'input.txt').open('r') as f:
        lines = f.read().splitlines()

    print(sum(int(bank_joltage(line)) for line in lines))
