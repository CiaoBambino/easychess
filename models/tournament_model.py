import datetime
from tinydb import TinyDB
import player_model

class Tournament:

    TOURNAMENT_COUNTER = 1
    DATE = datetime.datetime.now()
    DEFAULT_PLACE = "Club d'échecs de Paname"
    DEFAULT_NAME = "Tournoi n°%s du %s" % (TOURNAMENT_COUNTER, DATE)
    NEW_DEFAULT_NAME = "NEW_DEFAULT_NAME"
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    # mm/dd/y
    d3 = today.strftime("%m/%d/%y")
    # Month abbreviation, day and year
    d4 = today.strftime("%b-%d-%Y")

    """
    d1 = 16/09/2019
    d2 = September 16, 2019
    d3 = 09/16/19
    d4 = Sep-16-2019
    """

    def __init__(self,
                 name=DEFAULT_NAME,
                 place=DEFAULT_PLACE,
                 date=DATE,
                 number_of_rounds=4,
                 players=8,
                 players_id=[],
                 player_list=[],
                 mode=blitz,
                 description=None):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.players = players
        self.players_id = players_id
        self.player_list = player_list
        self.mode = mode
        self.description = description

    def __call__(self, *args, **kwargs):
        Tournament.TOURNAMENT_COUNTER += 1

    def serializer(self): # ajouter variable a serialiser et deserialiser
        serialized_tournament = {
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'number_of_rounds': self.number_of_rounds,
            'players': self.players,
            'mode': self.mode,
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

    def matchmaking(self):
        """
1.	Au début du premier tour, triez tous les joueurs en fonction de leur classement.
2.	Divisez les joueurs en deux moitiés, une supérieure et une inférieure. Le meilleur
    joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure,
    et ainsi de suite. Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé
    avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points.
    Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
4.	Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite.
    Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
5.	Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.
 
        """

class Round:

    ROUND_NUMBER = 1

    def __init__(self, name, start_time, end_time, matchmaking):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matchmaking = matchmaking

    def __call__(self):
        pass

    def create_match_list(self):
        pass

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

class GameMode:

    def blitz(self):

    def bullet(self):

    def coup_rapide(self):
