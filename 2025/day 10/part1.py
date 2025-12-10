import re
from pathlib import Path


def to_state(s):
    return int(''.join([str(int(s == '#')) for s in s]), 2)


def parse_button(b, n_bits) -> int:
    mask = []
    indices = b.split(',')
    for i in range(n_bits):
        if str(i) in indices:
            mask.append('1')
        else:
            mask.append('0')
    return int(''.join(mask), 2)


def to_buttons(lst, n_bits):
    return [parse_button(b, n_bits) for b in lst]


def parse_line_content(s):
    pattern = r'\[(.*?)\]|\((.*?)\)|\{(.*?)\}'
    matches = re.findall(pattern, s)
    matches = [it for m in matches for it in m if it]
    return to_state(matches[0]), to_buttons(matches[1:-1], len(matches[0])), matches[-1]


def get_min_steps(end, btns: list[int]) -> int:
    steps = 0
    previous_states = [0]
    while True:
        steps += 1
        next_states = []
        for s in previous_states:
            for b in btns:
                next_state = s ^ b
                if next_state == end:
                    return steps
                next_states.append(next_state)

        previous_states = next_states


if __name__ == "__main__":
    with Path(__file__).with_name('input.txt').open() as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        end_state, buttons, _ = parse_line_content(line)

        total += get_min_steps(end_state, buttons)

    print(total)
