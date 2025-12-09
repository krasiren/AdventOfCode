if __name__ == "__main__":
    with open('2025/day 09/input.txt', 'r') as f:
        lines = f.read().splitlines()

    points = [tuple(map(int, line.split(','))) for line in lines]

    max_area = 0
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            area = (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)
            if area > max_area:
                max_area = area

    print(max_area)
