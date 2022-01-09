# Basic Sieve of Eratosthenes
def sieve1(limit):
    if limit < 2:
        return

    a = [True] * (limit)  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


# Basic Sieve of Eratosthenes
# Only generate odd numbers
def sieve2(limit):
    if limit < 2:
        return

    yield 2

    half = (limit - 1) // 2

    a = [True] * half  # Initialize the primality list

    for (i, isprime) in enumerate(a):
        if isprime:
            val = i * 2 + 3
            yield val

            for n in range(val ** 2, limit + 1, val):  # Mark factors non-prime
                if n % 2 != 0:
                    a[n // 2 - 1] = False


if __name__ == "__main__":
    import timeit

    print(timeit.timeit("sieve1(10000000000)", globals=locals()))
    print(timeit.timeit("sieve2(10000000000)", globals=locals()))
