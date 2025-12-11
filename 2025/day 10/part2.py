import re
from pathlib import Path


def to_joltages(s):
    return [int(j) for j in s.split(',')]


def to_buttons(lst):
    return [[int(i) for i in b.split(',')] for b in lst]


def parse_line_content(s):
    pattern = r'\[(.*?)\]|\((.*?)\)|\{(.*?)\}'
    matches = re.findall(pattern, s)
    matches = [it for m in matches for it in m if it]
    return matches[0], to_buttons(matches[1:-1]), to_joltages(matches[-1])


def get_min_steps(end, btns: list[list[int]]) -> int:
    steps = 0
    previous_states = [[0] * len(end)]
    while True:
        steps += 1
        next_states = []
        for s in previous_states:
            for b in btns:
                next_state = [s[i] + (i in b) for i in range(len(s))]
                if all(next_state[i] == end[i] for i in range(len(end))):
                    return steps
                next_states.append(next_state)

        previous_states = next_states


if __name__ == "__main__":
    with Path(__file__).with_name('input.txt').open() as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        _, buttons, joltage_levels = parse_line_content(line)

        total += get_min_steps(joltage_levels, buttons)

    print(total)
