from functools import lru_cache

initial_fish = list(map(int, open('input').read().strip().split(",")))


@lru_cache(maxsize=None)
def simulate(timer, days_left):
    if days_left < timer:
        return 1
    else:
        # One fish spawns another at (days_left - timer - 1)
        # Add this fish + all its descendants
        return simulate(6, days_left - timer - 1) + simulate(8, days_left - timer - 1)


days = 256
total = sum(simulate(timer, days - 1) for timer in initial_fish)
print(total)
