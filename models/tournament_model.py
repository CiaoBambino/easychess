import datetime
from models import gamemode

class Tournament:

    TOURNAMENT_COUNTER = 1
    PLACE = "Club d'échecs de Paname"
    DATE = datetime.datetime.now()

    def __init__(self,
                 name="Tournoi n°%s du %s" % (TOURNAMENT_COUNTER, DATE),
                 place=PLACE,
                 date=DATE,
                 number_of_rounds=4,
                 players=None,
                 mode=gamemode.Blitz,
                 description=None):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.players = players
        self.mode = mode
        self.description = description

    def __call__(self, *args, **kwargs):
        Tournament.TOURNAMENT_COUNTER += 1

    def serializer(self):
        serialized_tournament = {
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'number_of_rounds': self.number_of_rounds
            'players': self.players,
            'mode': self.mode
            'description': self.description
        }
        return serialized_tournament

    def reverse_serializer(self, serialized_tournament):
        name = serialized_tournament['name']
        place = serialized_tournament['place']
        date = serialized_tournament['date']
        number_of_rounds = serialized_tournament['number_of_rounds']
        players = serialized_tournament['players']
        mode = serialized_tournament['mode']
        description = serialized_tournament['description']
        return Tournament(name,
                          place,
                          date,
                          number_of_rounds,
                          players,
                          mode,
                          description)

class Round:

    ROUND_NUMBER = 1

    def __init__(self, name, start_time, end_time, matchmaking):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matchmaking

    def __call__(self):

    def create_match_list(self):

    def c

    def serializer(self):
        serialized_round = {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
        return serialized_round

    def reverse_serializer(self, serializer_round):
        name = serializer_round['name']
        start_time = serializer_round['start_time']
        end_time = serializer_round['end_time']
        return Round(name, start_time, end_time)

#class MatchMaking:

    def __init__(self, players):
        self.players = players

    def __call__(self):

    def matchmaking(self, player_list):


class Match:

    MATCH_NUMBER = 1
    DEFAULT_NAME = "Match n°%s" %(MATCH_NUMBER)

    def __init__(self, name=DEFAULT_NAME, player1=None, player2=None, score_player1=0, score_player2=0):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
        Match.MATCH_NUMBER += 1

    def __str__(self):
        return f"{self.name} opposant {self.player1} à {self.player2}"

