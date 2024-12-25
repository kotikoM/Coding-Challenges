def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Skip even numbers
    for i in range(3, int(n ** 0.5) + 1, 2):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True


def up_to_n_primes(n):
    primes = []

    for number in range(2, n):
        if is_prime(number):
            primes.append(number)


    return primes

n = 2 * (10**6)
primes = up_to_n_primes(n)
print(primes)
print(sum(primes))

