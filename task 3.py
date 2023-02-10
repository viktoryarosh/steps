
def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2

    for _ in range (2, n):
        b = a + b
        a = b - a
    return b
print(climb_stairs(5))