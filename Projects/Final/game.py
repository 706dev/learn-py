from character import Character
from room import Room


class Game:
    def __init__(
        self,
        player_name
    ):
        self.characters = [Character(0, player_name)]
        
        self.player = self.characters[0]
        self.populate_characters()
        self.map = [
            Room((0, 0)),
            Room((0, 1)),
            Room((1, 0))
        ]

    def populate_characters(self):

        names = [
            'Josh',
            'James'
        ]

        for name in names:
            self.characters.append(
                Character(
                    uid=len(self.characters),
                    name=name
                )
            )
    
    def attempt_player_move(self, direction):
        new_position = self.player.get_new_position(direction)
        for room in self.map:
            if new_position == room.position:
                self.player.update_position(new_position)