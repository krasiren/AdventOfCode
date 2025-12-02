from os import listdir, mkdir, path, rmdir


if __name__ == '__main__':
    year = '2025'   # change year
    initial_lines = "with open('<year>/<day>/input.txt', 'r') as f:\n\tlines = f.readlines()"

    if year not in listdir():
        mkdir(year)

    for day in range(1, 26):
        if not f'day {day}' in listdir(year):
            day_dir = f'day {day:02d}'
            mkdir(path.join(year, day_dir))
        for part in range(1, 3):
            with open(path.join(year, day_dir, f'part{part}.py'), 'w') as f:
                f.write(initial_lines.replace('<year>', year).replace('<day>', day_dir))

        with open(path.join(year, day_dir, 'input.txt'), 'w') as f:
            f.write("")
