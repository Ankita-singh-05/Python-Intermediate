points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D)
print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]

def sort_by_y(x):
    return x[1]

points2D_sorted = sorted(points2D, key=sort_by_y)
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]