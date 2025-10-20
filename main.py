import argparse
from die import Die
from factory import PlayerFactory
from proxy import GameProxy

class PigGame:
    """Implements the rules and flow of the Pig game."""
    def __init__(self, players):
        self.die = Die()
        self.players = players
        self.current_player_index = 0

    def switch_turn(self):
        """Switch to the next player."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        """Handles a full turn for the current player."""
        player = self.players[self.current_player_index]
        player.reset_turn()

        print(f"\n{player.name}'s turn.")
        print(f"Current score: {player.score}")

        while True:
            action = input("Roll (r) or Hold (h)? ").strip().lower()

            if action == 'r':
                roll = self.die.roll()
                print(f"{player.name} rolled a {roll}.")

                if roll == 1:
                    print("Rolled a 1! No points this turn.")
                    player.reset_turn()
                    break
                else:
                    player.turn_total += roll
                    print(f"Turn total: {player.turn_total}, Overall score: {player.score}")

            elif action == 'h':
                player.add_to_score()
                print(f"{player.name} holds. Total score: {player.score}")
                break
            else:
                print("Invalid input. Enter 'r' to roll or 'h' to hold.")

        self.switch_turn()

    def play_game(self):
        """Runs the game until one player reaches 100 points."""
        print("\nWelcome to the Pig Game!")
        print("First player to reach 100 points wins!\n")

        while True:
            self.play_turn()
            for player in self.players:
                if player.score >= 100:
                    print(f"\n {player.name} wins with {player.score} points! ")
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play the Pig dice game (with Factory & Proxy).")
    parser.add_argument("--numPlayers", type=int, default=2, help="Number of players (default: 2)")
    args = parser.parse_args()

    # Create players using Factory pattern
    players = PlayerFactory.create_players(args.numPlayers)

    # Create real game and wrap it with Proxy
    game = PigGame(players)
    proxy = GameProxy(game)

    # Start game through Proxy
    proxy.play_game()
