def triangle(n, k):
    occ = n // k
    return occ * -~occ // 2 * k


def naive(n):
    return sum(i for i in range(n + 1) if not i % 3 or not i % 5)


def smart(n):
    return triangle(n, 3) + triangle(n, 5) - triangle(n, 15)


print(smart(1_000))
