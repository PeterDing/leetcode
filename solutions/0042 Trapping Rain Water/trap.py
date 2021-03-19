def trap(height):
    max_lefts = [0] * len(height)
    max_left = 0
    for i in range(len(height)):
        max_left = max(max_left, height[i])
        max_lefts[i] = max_left

    max_rigths = [0] * len(height)
    max_rigth = 0
    for i in range(len(height) - 1, -1, -1):
        max_rigth = max(max_rigth, height[i])
        max_rigths[i] = max_rigth

    r = 0
    for i, (ml, mr) in enumerate(zip(max_lefts, max_rigths)):
        r += min(ml, mr) - height[i]

    return r


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
r = trap(height)
print(r)
