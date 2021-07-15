import os
from models import player_model, tournament_model
from control import controler

class MenuDisplay:

    def menu(self):
        print("Bienvenue dans EasyChess\n\n")
        print("[1] Créer un tournoi"
              "[2] Ajouter un joueur"
              "[3] Modifier un joueur"
              "[4] Afficher un rapport\n\n")
        answer = False
        while answer is not True:
            try:
                option = int(input("Entrez le nombre associé à l'option désiré")
                if option == 1:
                    answer = True
                elif option == 2:
                    answer = True
                elif option == 3:
                    answer = True
                elif option == 4:
                    answer = True
                else:
                    print("ERREUR : le nombre entré ne correspond à aucun menu ")
                    option = int(input("Entrez le nombre associé à l'option désiré")
            except ValueError:
                option = int(input("La fonction accepte un nombre entier uniquement")

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
