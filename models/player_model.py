from tinydb import TinyDB

player_db = TinyDB("player_db.json")

class Player:

    def __init__(self, name="non renseigné",
                 last_name="non renseigné",
                 birthday="non renseigné",
                 sexe="non renseigné",
                 rank=None,
                 score=0, #
                 player_id=None):
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank
        self.score = score
        self.player_id = player_id

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def serializer(self):
        serialized_player = {
            'name': self.name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'sexe': self.birthday
            'classement': self.rank,
            'score': self.score
        }
        return serialized_player

    def reverse_serializer(self,serialized_player):
        name = serialized_player['name']
        last_name = serialized_player['last_name']
        birthday = serialized_player['birthday']
        sexe = serialized_player['sexe']
        rank = serialized_player['rank']
        score = serialized_player['score']
        return Player(name, last_name, birthday, sexe, rank, score)

    def update_tiny(self, player_option):
        player = Player(option[0],
                        option[1],
                        option[2],
                        option[3],
                        option[4])

class PlayerList:

    PLAYER_LIST = []

    def add_player(self, Player):
        PlayerList.PLAYER_LIST.append(player)
        PlayerList.PLAYER_LIST.sort()