# data = [[0,0],[0,1],[1,1],[1,0]]
data = [[1,1], [1,2], [2,2], [2,1], [1,1]]
# data = [[0,0], [0,1], [1,1], [1,0], [0,0]]

length = 0
input = data.copy()
while len(input) > 1:
    point = input.pop()
    next = input[-1]
    xDelta = abs(point[0] - next[0])
    yDelta = abs(point[1] - next[1])
    if xDelta and not yDelta:
        length += xDelta
    elif yDelta and not xDelta:
        length += yDelta
    else:
        length += abs(
            ((yDelta ** 2) + (xDelta ** 2)) ** 0.5
        )
print("length of sides", length)
input = data.copy()

area1 = 0
area2 = 0
i = 0
while i < len(input):
    if i == len(input) - 1:
        area1 += input[i][0] * input[-1][1]
        area2 += input[i][1] * input[-1][0]
    else:
        area1 += input[i][0] * input[i + 1][1]
        area2 += input[i][1] * input[i + 1][0]
    i += 1
    print(area1, area2)

area = (abs(area1 - area2)) / 2

print(area)
    