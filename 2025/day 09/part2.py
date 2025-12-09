from shapely import LineString
from shapely.geometry.polygon import Polygon

if __name__ == "__main__":
    with open('2025/day 09/input.txt', 'r') as f:
        lines = f.read().splitlines()

    points = [tuple(map(int, line.split(','))) for line in lines]
    poly = Polygon(points)

    max_area = 0
    for p1 in points:
        for p2 in points:
            if any(p1[i] == p2[i] for i in (0, 1)):
                shape = LineString([p1, p2])
            else:
                shape = Polygon([p1, (p1[0], p2[1]), p2, (p2[0], p1[1])])

            if shape.covered_by(poly):
                area = (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)
                if area > max_area:
                    max_area = area
                    print(p1, p2, area)

    print(max_area)
