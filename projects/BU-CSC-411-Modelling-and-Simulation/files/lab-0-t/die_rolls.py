# Class Number: B095
# Date: 7 November 2026
# Matriculation Number: 23/0970
# Group: CS-B
# Programme: BSc Computer Science
# AI use: Claude helped me comment the code and check the arithmetic. I can explain and change every line.

import sys
from itertools import islice
from pathlib import Path

# make the folder holding this script importable, so the file runs from its
# own directory or from any directory above it without an import error
sys.path.insert(0, str(Path(__file__).resolve().parent))
from random_gen import SimpleRandom  # noqa: E402

FACES = 6
SEED = 123
SAMPLE_SIZES = (10, 100, 1000, 10000)

# a single instance, built once, so successive calls continue the same
# stream instead of restarting it
_rng = SimpleRandom(SEED)


def _uniform_values(count):
    """Lazily produce `count` numbers in [0, 1) from the shared generator."""
    yield from islice(_rng, count)


def _as_face(value):
    # chop the fraction off after widening it by the number of faces, then
    # shift the 0..5 band up to 1..6
    return int(value * FACES) + 1


def simulate_die_rolls(n):
    # sum the faces in one pass, then divide once at the end so the answer
    # stays a mean and does not climb with n
    running_total = sum(_as_face(value) for value in _uniform_values(n))
    return running_total / n


if __name__ == "__main__":
    for n in SAMPLE_SIZES:
        print(f"Average of {n:5d} rolls: {simulate_die_rolls(n):.4f}")
