for a in range(1000):
    for b in range(a, 1000 - a + 1):
        for c in range(b, 1000 - a - b + 1):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a)
                print(b)
                print(c)
                print(a * b * c)
                break
