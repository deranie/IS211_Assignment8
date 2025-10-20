import random

class Die:
    """Represents a six-sided die."""
    def __init__(self):
        # Fixed seed for reproducible testing
        random.seed(0)

    def roll(self):
        """Roll the die and return a number between 1 and 6."""
        return random.randint(1, 6)
