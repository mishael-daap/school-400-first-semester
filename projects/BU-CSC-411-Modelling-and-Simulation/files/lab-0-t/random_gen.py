# Class Number: B095
# Date: 7 November 2026
# Matriculation Number: 23/0970
# Group: CS-B
# Programme: BSc Computer Science
# AI use: Claude helped me comment the code and check the arithmetic. I can explain and change every line.

class SimpleRandom:
    """Linear congruential generator exposed as a Python iterator.

    The three constants live on the class because they never vary between
    instances; only the state moves.
    """

    MULTIPLIER = 1103515245
    INCREMENT = 12345
    SPAN = 1 << 31        # 2**31 written as a left shift
    LOW_BITS = SPAN - 1   # one less than a power of two is an all-ones mask

    def __init__(self, seed):
        self._state = seed

    def _advance(self):
        # SPAN is a power of two, so cutting the value down to its low 31
        # bits gives exactly the same remainder as % 2**31 would, without
        # the division
        self._state = (self.MULTIPLIER * self._state + self.INCREMENT) & self.LOW_BITS
        return self._state

    def next(self):
        # scale the whole 31-bit state down onto the half-open range [0, 1)
        return self._advance() / self.SPAN

    def __iter__(self):
        # the generator hands out its own values, so it is its own iterator
        return self

    def __next__(self):
        # lets next(rng) and for-loops pull from the same sequence as .next()
        return self.next()
