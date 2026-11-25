class SimpleRandom:
    def __init__(self, seed):
        """Set up the generator with a starting seed."""
        self.state = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31

    def next(self):
        """Generate the next pseudo-random number between 0 and 1."""
        # self.state = (self.a * self.state + self.c) % self.m
        # return self.state / self.m
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m

rng = SimpleRandom(4)

def flip_coin(rng):
    if rng.next() < 0.5:
        return "Heads"
    else:
        return "Tails"

def roll_die(rng):
    # int() cuts off any numbers after the decimal point
    return int(rng.next() * 6) + 1