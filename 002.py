def naive(n):
    a, b = 0, 1
    c = a + b
    rez = 0
    while c <= n:
        if not c & 1:
            rez += c
        a, b = b, a + b
        c = a + b
    return rez


print(naive(4_000_000))
