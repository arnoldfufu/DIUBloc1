from random import randrange, choice
import pygame
from constantes import *

taille = TAILLE

###### Version POO ####
class Carte:
    """Classe carte"""

    def __init__(self, largeur, hauteur):
        """Génère une carte pleine de 1"""
        pygame.init()
        self.largeur = LARGEUR
        self.hauteur = HAUTEUR
        self.fenetre = pygame.display.set_mode((self.largeur * taille, self.hauteur * taille))
        self.carte = []
        grille = []
        for ligne in range(hauteur):
            grille.append([])
            for colonne in range(largeur):
                grille[ligne].append(1)
        self.carte = grille

    def affiche_carte(self):
        """Méthode d'affichage de la carte en console"""
        for ligne in range(self.hauteur):
            for colonne in range(self.largeur):
                print(self.carte[ligne][colonne], end='')
            print()
        print()

    def origine_initiale(self):
        """ Point de départ aléatoire"""
        x = randrange(self.largeur // 2)
        y = randrange(self.hauteur // 2)
        return 2 * x + 1, 2 * y + 1

    def creuse_autour(self, x, y):  # Méthode non utilisée pour le moment
        """Méthode pour creuser autour du point (x,y)"""
        if x + 1 < self.largeur - 1: self.carte[y][x + 1] = 0
        if x - 1 > 0: self.carte[y][x - 1] = 0
        if y + 1 < self.hauteur - 1: self.carte[y + 1][x] = 0
        if y - 1 > 0: self.carte[y - 2][x] > 0

    def nb_cases_encore_a_creuser(self):
        """Nombre de cases qu'il reste à creuser"""
        somme = 0
        for x in range(self.largeur // 2):
            for y in range(self.hauteur // 2):
                somme += self.carte[2 * y + 1][2 * x + 1]
        return somme

    def destinations_possibles(self, x, y):
        liste = []
        if x + 2 < self.largeur - 1 and self.carte[y][x + 2] > 0:
            liste.append(0)
        if x - 2 > 0 and self.carte[y][x - 2] > 0:
            liste.append(2)
        if y + 2 < self.hauteur - 1 and self.carte[y + 2][x] > 0:
            liste.append(3)
        if y - 2 > 0 and self.carte[y - 2][x] > 0:
            liste.append(1)
        return liste

    def copie_carte(self, c):
        copie = []
        for ligne in range(self.hauteur):
            copie.append([])
            for colonne in range(self.largeur):
                copie[ligne].append(c[ligne][colonne])
        return copie

    def nouveau_chemin_depuis(self, x, y, t):
        self.carte[y][x] = 0
        liste = self.destinations_possibles(x, y)
        if len(liste) == 0:
            # creuse encore un coup pour débugger
            # creuseAutour(carte,x,y,largeur,hauteur)
            return
        else:
            choix = choice(liste)
            if choix == 0:
                self.carte[y][x + 1] = 0
                self.carte[y][x + 2] = 0
                x, y = x + 2, y
            elif choix == 2:
                self.carte[y][x - 1] = 0
                self.carte[y][x - 2] = 0
                x, y = x - 2, y
            elif choix == 1:
                self.carte[y - 1][x] = 0
                self.carte[y - 2][x] = 0
                x, y = x, y - 2
            else:
                self.carte[y + 1][x] = 0
                self.carte[y + 2][x] = 0
                x, y = x, y + 2
            # basculer
            self.affichage_graphique()
            if t > 0:
                self.nouveau_chemin_depuis(x, y, t - 1)
            else:
                return
    def new_carte(self):
        """génère le lab"""
        if self.nb_cases_encore_a_creuser() > 0:
            x0, y0 = self.origine_initiale()
            t = ((self.largeur) // 2 * (self.hauteur) // 2) // 3
            self.nouveau_chemin_depuis(x0, y0, t)
        # afficheCarte(carte,largeur,hauteur)
        while self.nb_cases_encore_a_creuser() > 0:
            self.nouveau_chemin_jusque_zero_pas_dans_chemin_en_cours(x0, y0)
            # afficheCarte(carte,largeur,hauteur)
        return self.carte

    def nouveau_chemin_jusque_zero_pas_dans_chemin_en_cours(self, x0, y0):
        x, y = x0, y0  # pour rentrer dans while
        while self.carte[y][x] == 0:
            x, y = self.origine_initiale()
        ancienne = self.copie_carte(self.carte)
        while self.carte[y][x] > 0 or not ancienne[y][x] == 0:
            self.carte[y][x] = 0
            # print("debut chemin en",x,y)
            # afficheCarte(carte,largeur,hauteur)
            liste = self.destinations_possibles_avec_zero(x, y)
            choix = choice(liste)
            # print(choix)
            if choix == 0:
                self.carte[y][x + 1] = 0
                x, y = x + 2, y
            elif choix == 2:
                self.carte[y][x - 1] = 0
                x, y = x - 2, y
            elif choix == 1:
                self.carte[y - 1][x] = 0
                x, y = x, y - 2
            else:
                self.carte[y + 1][x] = 0
                x, y = x, y + 2
            # basculer
            self.affichage_graphique()

    def destinations_possibles_avec_zero(self, x, y):
        liste = []
        if x + 2 < self.largeur - 1:
            liste.append(0)
        if x - 2 > 0:
            liste.append(2)
        if y + 2 < self.hauteur - 1:
            liste.append(3)
        if y - 2 > 0:
            liste.append(1)
        return liste
    def affichage_graphique(self):
        """Affichage graphique"""

        for l in range(self.hauteur):
            for c in range(self.largeur):
                pygame.draw.rect(self.fenetre, (0, 0, 255 * self.carte[l][c]), (taille * c, taille * l, taille, taille), 0)
        pygame.display.flip()
        pygame.time.delay(200)

#### FIN VErsion POO
##########################################################################################
def newCarteAvecDepartEtArrivee(largeur, hauteur):
    nouvelle = newCarte(largeur, hauteur)
    x, y = 2 * randrange(largeur // 2) + 1, 0
    nouvelle[y][x] = 3
    x, y = 2 * randrange(hauteur // 2) + 1, hauteur - 1
    nouvelle[y][x] = 4252
    return nouvelle

carteobjet = Carte(LARGEUR, HAUTEUR)
carteobjet.new_carte()

pygame.quit()




