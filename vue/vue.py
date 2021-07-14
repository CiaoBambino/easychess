import os
from models import player_model, tournament_model

class MenuDisplay:

    def menu(self):
        print("Bienvenue dans EasyChess\n")

class ClearConsole:

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')

class PlayerDisplay:

    def __call__(self, *args, **kwargs):
        pass

class TournamentDisplay:

    def __call__(self):


class RoundDisplay:

class MatchDisplay:

class RapportDisplay:
