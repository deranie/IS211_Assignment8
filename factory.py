from player import Player

class PlayerFactory:
    """Factory for creating Player objects."""
    @staticmethod
    def create_players(num_players):
        players = []
        for i in range(num_players):
            name = input(f"Enter name for Player {i + 1}: ") or f"Player {i + 1}"
            players.append(Player(name))
        return players
