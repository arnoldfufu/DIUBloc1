##############################################################
#                       Corrigé du TP 01                     #
##############################################################

# Importation de la bibliothèque pygame
import pygame
from pygame.locals import * 
# importation des constantes de configuration
from configuration import *


# Initialisation de la fenètre pygame.
pygame.init()

fenetre = pygame.display.set_mode(TAILLE_FENETRE)
pygame.display.set_caption("TP1 souris coordonnées et pygame")

fenetre.fill(COULEUR_FENETRE)

continuer = True

# Boucle "infinie" de lecture des évènements pygame
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = False
                elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                print("Touche ECHAP")
                                continuer = False
                        else :
                                print("Autre touche")
                elif event.type == MOUSEBUTTONDOWN :
                        (xclic, yclic) = event.pos
                        print("Clic en ("+str(xclic)+", "+str(yclic)+")")
                        pygame.draw.circle(fenetre,(255, 255, 255),(xclic, yclic), 20, 0)
                elif event.type == MOUSEMOTION :
                        (x, y) = event.pos
                        pygame.draw.rect(fenetre, COULEUR_TRAIT, (x-5, y-4, 10, 8), 0)
        pygame.display.flip()
pygame.quit()
