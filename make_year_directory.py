from os import listdir, mkdir, path, rmdir

year = '2024'   # change year
initial_lines = "with open('<year>/<day>/input.txt', 'r') as f:\n\tlines = f.readlines()"

if year not in listdir():
    mkdir(year)

for day in range(1, 26):
    if not f'day {day}' in listdir(year):
        mkdir(path.join(year, f'day {day}'))
    
    for part in range(1, 3):
        with open(path.join(year, f'day {day}', f'part{part}.py'), 'w') as f:
            f.write(initial_lines.replace('<year>', year).replace('<day>', f'day {day}'))

    with open(path.join(year, f'day {day}', 'input.txt'), 'w') as f:
            f.write("")