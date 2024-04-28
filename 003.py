def prime_factors(n):
    maxi = 2
    while n & 1 == 0:
        n >>= 1
    d = 3
    while d * d <= n:
        if n % d == 0:
            maxi = d
            while n % d == 0:
                n //= d
        d += 2
    return max(maxi, n)


print(prime_factors(600851475143))
