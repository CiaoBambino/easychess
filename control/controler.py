import sys
from random import randint
from vue import vue
from models import tournament_model, player_model

class MainMenu:

    def __init__(self):
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()
        self.exit_easy_chess = Quit

    def __call__(self):
        self.clear()
        self.vue.menu()
        option = 0
        while option == 0:
            try:
                option = int(input("Entrez le nombre associé à l'option désirée"))
                if option == 1:
                    tournoi = CreateTournament

                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 5:
                    pass
                elif option == 6:
                    pass
                elif option == 7:
                    self.exit_easy_chess()
                else:
                    print("ERREUR : le nombre entré ne correspond à aucun menu ")
                    option = 0
            except ValueError:
                print("La fonction accepte uniquement les nombres entier")
                option = 0

class ChessColor:

    def color(self, player):
        color = ['Black', 'White']
        player_color = color[randint(0, 1)]
        return player_color

class CreatePlayer:

    def __init__(self):
        self.player = player_model.Player
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()

    def __call__(self):
        self.clear()
        self.vue.create_player_display()
        self.player.name =
        self.player.lastname =
        self.player.birthday =
        self.player.sexe =
        self.player.rank =
        self.player.score =
        self.player.player_id =


class CreateTournament:

    def __init__(self):
        self.tournament = tournament_model.Tournament
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()

    def __call__(self):
        self.clear()
        self.vue.create_tournament_display()
        self.tournament.name = self.add_tournament_name()
        self.tournament.place = input("Lieu du tournoi")
        self.tournament.date = input("date")
        self.tournament.number_of_rounds = input("nombre de tours")
        self.tournament.players = input("nombre de joueurs")
        self.tournament.mode = input("mode de jeu")
        self.tournament.description = input("Description du tournoi")

    def add_tournament_name(self):
        valid_name = False
        while valid_name is False:
            x = input("Saisissez le nom du tournoi: ")
            if x != "":
                break
            else:
                print("Vous devez entrer un nom")
        return x

    def add_tournament_player(self, players):
        for x in range(players):
            self.vue.add_player_choice()
            option = 0
            while option == 0:
                try:
                    option = int(input("Entrez le nombre associé à l'option désirée"))
                    if option == 1:
                        # ajouter depuis base de données

                    elif option == 2:
                        new_player = CreatePlayer
                        player_model.PlayerList.add_player(new_player)
                        self.tournament.player_list.append(new_player)


                    elif option == 3:
                        self.exit_easy_chess()
                    else:
                        print("ERREUR : le nombre entré ne correspond à aucun menu ")
                        option = 0
                except ValueError:
                    print("La fonction accepte uniquement les nombres entier")
                    option = 0



class StartTournament:
    pass

class RapportTournament:
    pass

class RapportPlayer:
    pass

class Quit:

    def __call__(self):
        sys.exit()