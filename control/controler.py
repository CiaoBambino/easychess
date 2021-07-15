import sys
from random import randint
from vue import vue

class MainMenu:

    def __init__(self):
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()


    def __call__(self):
        self.clear
        self.vue.menu()

class ChessColor:

    def color(self, player):
        color = ['Black', 'White']
        player_color = color[randint(0, 1)]
        return player_color

class CreatePlayer:

class PlayerList:

class RapportPlayer:

class CreateTournament:

class StartTournament:

class RapportTournament:

class Quit:

    def __call__(self):
        sys.exit()