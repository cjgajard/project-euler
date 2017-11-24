# PROBLEM 67


def maxsum_route(text):
    rows = (x for x in text.split('\n') if x)
    triangle = [(int(x) for x in row.split()) for row in rows]

    while len(triangle) > 1:
        floor = list(triangle.pop())
        ceil = list(triangle.pop())

        new = []
        for i in range(len(ceil)):
            num = ceil[i]
            left = floor[i]
            right = floor[i + 1]
            greater = (left if left >= right else right)  # >=, <= IDK
            new.append(num + greater)
        triangle.append(new)

    return(triangle[0][0])


with open('p067_triangle.txt', 'r') as f:
    print(maxsum_route(f.read()))
