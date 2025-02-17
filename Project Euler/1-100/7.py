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


def first_n_primes(n):
    primes = []
    number = 2  # Start checking from the first prime number

    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1  # Increment to check the next number

    return primes

n = 10001
primes = first_n_primes(n)
print(primes)
