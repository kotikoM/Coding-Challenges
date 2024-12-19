factors_memo = {}

def odd_factors(n):
    if n in factors_memo:
        return factors_memo[n]

    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 1:  # Only include odd factors
                factors.append(i)
            if (n // i) % 2 == 1 and i != n // i:  # Include the complementary factor
                factors.append(n // i)


    factors_memo[n] = factors  # Cache the result
    return factors

def is_prime(n):
    if n <= 1:
        return False
    if n in factors_memo:
        return len(factors_memo[n]) == 2
    return len(odd_factors(n)) == 2

facs = odd_factors(600851475143)
for fac in reversed(facs):
    if is_prime(fac):
        print(f"Largest prime factor: {fac}")
        break
