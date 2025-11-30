import math
points = [
(12, 55),
(880, 123),
(64, 64),
(190, 1024),
(77, 33),
(42, 11),
(0, 90)
]
distance = 10**5
x_coordinate, y_coordinate = map(int, input().split())
best_x, best_y = 0, 0
for i in range (len(points)):
        if abs((points[i][0] - x_coordinate) + (points[i][1] - y_coordinate))**0.5 < abs(distance):
                distance = ((points[i][0] - x_coordinate) + (points[i][1] - y_coordinate))**0.5
                best_x = points[i][0]
                best_y = points[i][1]
        else:
                continue
print(best_x, best_y)