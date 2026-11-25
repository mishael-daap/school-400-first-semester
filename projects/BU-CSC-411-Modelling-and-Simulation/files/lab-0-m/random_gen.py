# Class Number: B017
# Date: 7 November 2026
# Matriculation Number: 23/1127
# Group: CS-B
# Programme: BSc Computer Science
# AI use: Claude helped me comment the code and check the arithmetic. I can explain and change every line.

class SimpleRandom:
    def __init__(self, seed):
        # the seed is only the starting point of the sequence. the three
        # constants are the ones the brief gave us, so I keep them on the
        # object instead of hardcoding them inside next()
        self.state = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2 ** 31

    def next(self):
        # move the state forward first, then divide by m to squeeze the
        # result into [0, 1). the same seed does the same jumps every time
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m
