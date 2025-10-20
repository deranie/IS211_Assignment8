class GameProxy:
    """Proxy that controls access to the real Pig game."""
    def __init__(self, game):
        self._game = game

    def play_game(self):
        print("Proxy: Initializing game session...")
        self._game.play_game()
        print("Proxy: Game session ended.")
