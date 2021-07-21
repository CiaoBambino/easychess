import os
from models import player_model, tournament_model
from control import controler

class MenuDisplay:

    def menu(self):
        print("Bienvenue dans EasyChess\n\n")
        print("[1] Créer un tournoi"
              "[2] Ajouter un joueur"
              "[3] Modifier un joueur"
              "[4] Afficher un rapport"
              "[5] Options par défaut"
              "[6] Aide"
              "[7] QUITTER\n\n")

    def create_tournament_display(self):
        print("Saisissez les informations relatives au tournoi:"
              "nom, place, date, nombre de tours, mode de jeu et description"
              "Une valeur par défaut est déjà attribué"
              "Puis ajoutez les joueurs")

    def create_player_display(self):
        print("Saisissez les infortmations du joueur:")

    def ask_start_tournament(self):
        print("Les informations nécessaires ont été correctement rentré"
              "Démarrer le tournoi ?"
              "[OUI]/[NON]") #

    def add_player_choice(self):
        print("[1] Ajouter un joueur depuis la base de données"
              "[2] Créer un joueur"
              "[3] Quitter")

    def default_value_menu(self):
        print("VALEURS PAR DEFAUT"
              "[1] Nom du club"
              "[2] Nom des tournois"
              "[3] Format de la date"
              "[4] Menu principal")

    def tournament_gamemode(self):
        print("[1] Blitz"
              "[2] Bullet"
              "[3] Coup rapide"
              "[4] Retour")

class PlayerDisplay:

    def __call__(self, *args, **kwargs):
        pass

class TournamentDisplay:

    def __call__(self):


class RoundDisplay:

class MatchDisplay:

class RapportDisplay:


class ClearConsole:

        def __call__(self):
            os.system('cls' if os.name == 'nt' else 'clear')