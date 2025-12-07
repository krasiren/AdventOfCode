from functools import lru_cache


@lru_cache
def trace_beam(position: tuple[int, int]) -> int:
    if position[0] == len(lines):
        return 1

    if position in splitters:
        return trace_beam((position[0] + 1, position[1] - 1)) + trace_beam((position[0] + 1, position[1] + 1))

    lines[position[0]][position[1]] = '|'
    return trace_beam((position[0] + 1, position[1]))


def print_lines() -> None:
    for line in lines:
        print(''.join(line))


if __name__ == '__main__':
    with open('2025/day 07/input.txt', 'r') as f:
        lines = [list(line) for line in f.read().splitlines()]

    print_lines()

    beam_start = None
    splitters = dict()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                continue
            elif c == 'S':
                beam_start = (i, j)
            elif c == '^':
                splitters[(i, j)] = 0

    print()
    num_timelines = trace_beam(beam_start)

    print_lines()
    print(num_timelines)
