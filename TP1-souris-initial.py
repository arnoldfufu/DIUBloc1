import pygame
from pygame.locals import * 

pygame.init()

fenetre=pygame.display.set_mode((600,300))
pygame.display.set_caption("TP1 souris coordonnées et pygame")

fenetre.fill((0,0,255))

continuer=True

while continuer:

        for event in pygame.event.get():

                if event.type==QUIT:
                        continuer=False

                elif event.type==KEYDOWN:   
                        if  event.key==K_ESCAPE:
                                print("touche Escape")
                                continuer=False
                        else :
                                print("autre touche")
                        
                elif event.type==MOUSEBUTTONDOWN :
                        (xclic,yclic)=event.pos
                        print("clic en ("+str(xclic)+","+str(yclic)+")")
                        pygame.draw.circle(fenetre,(255,255,255),(xclic,yclic),20,0)

                elif event.type==MOUSEMOTION :
                        (x,y)=event.pos
                        pygame.draw.rect(fenetre,(0,255,0),(x-5,y-4,10,8),0)
                         
        pygame.display.flip()

pygame.quit()
