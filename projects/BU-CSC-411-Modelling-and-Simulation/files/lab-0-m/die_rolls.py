# Class Number: B017
# Date: 7 November 2026
# Matriculation Number: 23/1127
# Group: CS-B
# Programme: BSc Computer Science
# AI use: Claude helped me comment the code and check the arithmetic. I can explain and change every line.

# works whether I run this from inside lab0 or from the folder above it
try:
    from random_gen import SimpleRandom
except ImportError:
    from lab0.random_gen import SimpleRandom

# one generator for the whole file, seeded once, so every run prints the
# same numbers and my evaluator can reproduce them
rng = SimpleRandom(123)


def simulate_die_rolls(n):
    total = 0
    for _ in range(n):
        # next() is in [0, 1), so times 6 and cut the decimals off gives
        # 0 up to 5, then +1 turns that into a real die face
        total += int(rng.next() * 6) + 1
    # the mean, not the sum, otherwise the number just grows with n
    return total / n


if __name__ == "__main__":
    # the count sits in 5 characters so the four lines line up,
    # and the average gets 4 decimal places
    for n in (10, 100, 1000, 10000):
        print(f"Average of {n:5d} rolls: {simulate_die_rolls(n):.4f}")
