def is_prime(k):
    for d in range(2,k):
        if k % d == 0:
            return False
    return True

def f(n):
    k = 2
    counter = 0
    while counter < n:
        if is_prime(k):
            counter += 1
        k += 1
    return k - 1


