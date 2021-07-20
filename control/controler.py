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
                    self.tournoi = CreateTournament

                elif option == 2:
                    self.player = CreatePlayer
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 5:
                    self.default_value_modifier = DefaultValueModifier
                    self.default_value_modifier()
                elif option == 6:
                    pass
                elif option == 7:
                    self.exit_easy_chess()
                else:
                    print("ERREUR : le nombre entré ne correspond à aucun menu ")
                    option = 0
            except ValueError: # placer la bonne exception
                print("La fonction accepte uniquement les nombres entier")
                option = 0

class ChessColor:

    def color(self, player):
        color = ['Black', 'White']
        player_color = color[randint(0, 1)]
        return player_color

class CreateTournament:

    def __init__(self):
        self.tournament = tournament_model.Tournament
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()

    def __call__(self):
        self.clear()
        self.vue.create_tournament_display()
        self.tournament.name = self.add_tournament_name()
        self.tournament.place = self.add_tournament_place()
        self.tournament.date = self.add_tournament_date()
        self.tournament.number_of_rounds = self.add_number_of_rounds()
        self.tournament.players = self.add_tournament_players_number()
        self.tournament.mode = self.add_tournament_gamemode()
        self.tournament.description = self.add_tournament_description()
        self.tournament.player_list = self.add_tournament_player(self.tournament.players)
        self.clear()
        response = self.ask_start_tournament()
        if response is True:
            start = StartTournament
            start()
        else:
            pass

    def add_tournament_name(self):
        valid_value = False
        x = tournament_model.Tournament.DEFAULT_NAME
        while valid_value is False:
            x = input("Saisissez le nom du tournoi, Si vous n'insérez \
                       rien la valeur par défaut sera attribuée comme nom")
            if x != "":
                break
            else:
                print("La valeur par défaut sera attribuée comme nom")
                response = input("[oui]/[non]")
                if response == "oui" or response == "o":
                    x = tournament_model.Tournament.DEFAULT_NAME
                    break
                else:
                    pass
        return x

    def add_tournament_place(self):
        valid_value = False
        x = tournament_model.Tournament.DEFAULT_PLACE
        while valid_value is False:
            x = input("Saisissez le lieu du tournoi, Si vous n'insérez \
                              rien la valeur par défaut sera attribuée comme nom")
            if x != "":
                break
            else:
                print("La valeur par défaut sera attribuée comme nom")
                response = input("[oui]/[non]")
                if response == "oui" or response == "o":
                    x = tournament_model.Tournament.DEFAULT_PLACE
                    break
                else:
                    pass
        return x

    def add_tournament_date(self):
        valid_value = False
        x = tournament_model.Tournament.DATE
        while valid_value is False:
            x = input("Saisissez la date du tournoi, Si vous n'insérez \
                       rien la date au format par défaut sera utilisé")
            if x != "":
                break
            else:
                print("La valeur par défaut sera attribuée comme date")
                response = input("[oui]/[non]")
                if response == "oui" or response == "o":
                    x = tournament_model.Tournament.DATE
                    break
                else:
                    pass
        return x

    def add_number_of_rounds(self):
        option = 0
        while option == 0:
            try:
                option = int(input("Saisissez le nombre de round désiré, Si vous n'insérez \
                                    rien la date au format par défaut sera utilisé"))
                if option != 0:
                    break
                else:
                    print("La valeur par défaut (4) sera attribuée")
                    response = input("[oui]/[non]")
                    if response == "oui" or response == "o":
                        option = 4
                        break
                    else:
                        pass
            except ValueError: # placer la bonne exception
                print("La fonction accepte uniquement les nombres entier")
                option = 0
        return option

    def add_tournament_players_number(self):
        valid_value = False
        x = 8
        while valid_value is False:
            x = input("Saisissez le nombre de joueurs dans le tournois, Si vous n'insérez \
                       rien le nombre sera fixé à 8")
            if x != "":
                break
            else:
                print("La valeur par défaut sera attribuée comme date")
                response = input("[oui]/[non]")
                if response == "oui" or response == "o":
                    x = 8
                    break
                else:
                    pass
        return x

    def add_tournament_gamemode(self):
        option = 0
        while option == 0:
            try:
                option = int(input("Entrez le nombre associé à l'option désirée"))
                if option == 1:
                    return str("blitz")
                elif option == 2:
                    return str("bullet")
                elif option == 3:
                    return str("coup rapide")
                elif option == 4:
                    self.vue.create_tournament_display()
                else:
                    print("ERREUR : le nombre entré ne correspond à aucun menu ")
                    option = 0
            except ValueError:  # placer la bonne exception
                print("La fonction accepte uniquement les nombres entier")
                option = 0

    def add_tournament_description(self):
        valid_value = False
        x = "aucune description"
        while valid_value is False:
            x = input("Saisissez la description du tournoi , Si vous n'insérez \
                               rien aucune description ne sera retenu")
            if x != "":
                break
            else:
                print("La valeur par défaut sera attribuée comme date")
                response = input("[oui]/[non]")
                if response == "oui" or response == "o":
                    x = "aucune description"
                    break
                else:
                    pass
        return x

    def add_tournament_player(self, players):
        player_list = []
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
                        player_list.append(new_player)
                    elif option == 3:
                        pass # option QUITTER
                    else:
                        print("ERREUR : le nombre entré ne correspond à aucun menu ")
                        option = 0
                except ValueError:
                    print("La fonction accepte uniquement les nombres entier")
                    option = 0
        return player_list

    def ask_start_tournament(self):
        self.vue.ask_start_tournament()
        response = input("")
        if response == "oui" or response == "o":
            return True
        else:
            return False

class CreatePlayer:

    def __init__(self):
        self.player = player_model.Player
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()

    def __call__(self):
        self.clear()
        self.vue.create_player_display()
        self.player.name = add_player_name()
        self.player.lastname = add_player_lastname()
        self.player.birthday = add_player_birthday()
        self.player.sexe = add_player_sexe()
        self.player.rank = add_player_rank()
        self.player.score = add_player_score()
        self.player.player_id = add_player_id()

    def add_player_name(self):
        valid_value = False
        x = "vide"
        while valid_value is False:
            x = input("Saisissez le nom du joueur")
            if x != "":
                break
            else:
                print("Vous devez saisir un nom")
        return x

    def add_player_lastname(self):
        valid_value = False
        x = "vide"
        while valid_value is False:
            x = input("Saisissez le nom de famille du joueur")
            if x != "":
                break
            else:
                print("Vous devez saisir un nom")
        return x

    def add_player_bithday(self):
        valid_value = False
        x = "00/00/0000"
        while valid_value is False:
            x = input("Saisissez la date de naissance au format voulu")
            if x != "":
                break
            else:
                print("Vous devez saisir une date")
        return x

    def add_player_sexe(self):
        valid_value = False
        x = "homme"
        while valid_value is False:
            x = input("Saisissez le sexe du joueur")
            if x != "":
                break
            else:
                print("Vous devez saisir quelque chose")
        return x

    def add_player_rank(self):
        valid_value = False
        x = "1"
        while valid_value is False:
            x = input("Saisissez le classement du joueur")
            if x != "":
                break
            else:
                print("Vous devez saisir quelque chose")
        return x

    def add_player_score(self):
        valid_value = False
        x = "0"
        while valid_value is False:
            x = input("Saisissez le score du joueur")
            if x != "":
                break
            else:
                print("Vous devez saisir quelque chose")
        return x

    def add_player_id(self):
        pass

class StartTournament:

    def __call__(self):


class RapportTournament:
    pass

class RapportPlayer:
    pass

class DefaultValueModifier:

    def __init__(self):
        self.vue = vue.MenuDisplay()
        self.clear = vue.ClearConsole()

    def __call__(self):
        self.clear()
        self.vue.default_value_menu()
        option = 0
        while option == 0:
            try:
                option = int(input("Entrez le nombre associé à l'option désirée"))
                if option == 1:
                    # nom du club
                elif option == 2:
                    # nom des tournois
                elif option == 3:
                    # format de la date
                elif option == 4:
                    self.menu = MainMenu()
                    self.menu()
                else:
                    print("ERREUR : le nombre entré ne correspond à aucun menu ")
                    option = 0
            except ValueError:
                print("La fonction accepte uniquement les nombres entier")
                option = 0

class Quit:

    def __call__(self):
        sys.exit()