def rotate_clock(matrix):
    rotated = []
    for col in zip(*matrix):
        rotated.append(list(reversed(col)))
    for row in rotated:
        print(list(row))

print(rotate_clock([[1, 2, 3, 4],
     [4, 5, 6, 4],
     [7, 8, 9, 3],
     [5, 7, 5, 2]]))

