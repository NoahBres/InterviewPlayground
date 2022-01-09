def sieve1(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


if __name__ == "__main__":
    import timeit

    print(timeit.timeit("sieve1(1000000)", globals=locals()))

    # print(list(sieve1(1000000)))
