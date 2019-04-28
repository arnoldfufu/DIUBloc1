##############################################################
#           Corrigé du TP 01  Version avec liste             #
##############################################################

import pygame
import traceback 
from pygame.locals import *

# importation des constantes de configuration
from configuration import *

pygame.init()

try:
    fenetre=pygame.display.set_mode(TAILLE_FENETRE)
    pygame.display.set_caption("Test souris et clavier de pygame")

    #pygame.key.set_repeat(500, 200)
    
    rouge = 0
    bleu = 255
    vert = 0

    fenetre.fill((rouge, vert, bleu))
    liste = []
    continuer = True
    
    xclic, yclic = -100, -100

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    rouge += 16
                    if rouge > 255:
                        rouge = 0
                    print("flèche vers le haut, rouge =",rouge)
                elif event.key == K_DOWN:
                    bleu -= 16
                    if bleu < 0:
                        bleu = 255
                    print("flèche vers le bas, bleu =",bleu)
                elif event.key == K_ESCAPE:
                    print("touche Escape")
                    continuer = False
                else :
                    print("autre touche")
                fenetre.fill((rouge, 0, bleu))
            elif event.type == MOUSEBUTTONDOWN :
                (xclic,yclic) = event.pos
                print("clic en ("+str(xclic)+","+str(yclic)+")")

            elif event.type == MOUSEMOTION :
                (x, y) = event.pos
                liste.append((x, y))
                

        fenetre.fill((rouge, 0, bleu))
       
        for centre in liste[-100:] :
            pygame.draw.rect(fenetre, COULEUR_TRAIT, (centre[0]-5,
                                                      centre[1]-5, 10, 10), 0)
        pygame.draw.circle(fenetre, COULEUR_CERCLE, (xclic, yclic), 20, 0)
        pygame.display.flip()
        
except:
   #ce bloc permet de récupérer des infos en cas d'erreur
   traceback.print_exc()
finally:
    pygame.quit()
