def minTimeToVisitAllPoints(points):
    return sum(max(abs(x2 - x1), abs(y2 - y1)) for (x1, y1), (x2, y2) in zip(points, points[1:]))

points = [[1, 1], [3, 4], [-1, 0]]
print(minTimeToVisitAllPoints(points))
