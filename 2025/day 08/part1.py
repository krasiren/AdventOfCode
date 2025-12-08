from functools import reduce
from operator import mul

import numpy as np
from scipy.spatial import distance_matrix


if __name__ == '__main__':
    with open('2025/day 08/input.txt', 'r') as f:
        lines = f.read().splitlines()

    boxes = []
    for line in lines:
        coords = line.split(',')
        boxes.append([int(coords[0]), int(coords[1]), int(coords[2])])

    boxes = np.array(boxes, dtype=np.uint32)
    dm = distance_matrix(boxes, boxes) + np.eye(len(boxes), dtype=np.uint32) * 1_000_000_000

    indices = np.unravel_index(np.argsort(dm, axis=None), dm.shape)[0]
    indices = indices.reshape(-1, 2)

    circuits = [[i] for i in range(len(boxes))]
    for i1, i2 in indices[:1000]:
        i1, i2 = int(i1), int(i2)
        c1 = [i1 in c for c in circuits].index(True)
        c2 = [i2 in c for c in circuits].index(True)

        if c1 == c2:
            continue

        circuits[c1].extend(circuits[c2])
        del circuits[c2]

    print(reduce(mul, sorted([len(c) for c in circuits], reverse=True)[:3]))
