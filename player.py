class Player:
    """Represents a player in the Pig game."""
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0

    def reset_turn(self):
        """Resets the player’s turn total."""
        self.turn_total = 0

    def add_to_score(self):
        """Adds the current turn total to the overall score."""
        self.score += self.turn_total
        self.reset_turn()
