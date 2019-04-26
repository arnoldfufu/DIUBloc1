from random import randrange,choice
import pygame
from pygame.locals import * 

largeur = 21
hauteur = 13
taille = 60

pygame.init()

fenetre=pygame.display.set_mode((largeur*taille,hauteur*taille))
pygame.display.set_caption("Creuser !")

continuer=True

carte=[]

def bascule():
        global carte
        for l in range(hauteur):
                for c in range(largeur):
                        pygame.draw.rect(fenetre,(0,0,255*carte[l][c]),(taille*c,taille*l,taille,taille),0)
        pygame.display.flip()
        pygame.time.delay(200)


def cartePLeineDeUns(largeur,hauteur):
    # une carte pleine de 1
    grille=[]
    for ligne in range(hauteur):
        grille.append([])
        for colonne in range(largeur):
            grille[ligne].append(1)
    return grille

def copieCarte(c,largeur,hauteur):
    copie=[]
    for ligne in range(hauteur):
        copie.append([])
        for colonne in range(largeur):
            copie[ligne].append(c[ligne][colonne])
    return copie

def origineInitiale(carte,largeur,hauteur):
    x=randrange(largeur//2)
    y=randrange(hauteur//2)
    return 2*x+1,2*y+1

def afficheCarte(carte,largeur,hauteur):
    for ligne in range(hauteur):
        for colonne in range(largeur):
            print(carte[ligne][colonne],end='')
        print()
    print()

def nbreCasesEncoreACreuser(carte,largeur,hauteur):
    somme=0
    for x in range(largeur//2) :
        for y in range(hauteur//2) :
            somme+=carte[2*y+1][2*x+1]
    return somme

def destinationsPossibles(carte,x,y,largeur,hauteur):
    liste=[]
    if x+2<largeur-1 and carte[y][x+2]>0 :
        liste.append(0)
    if x-2>0 and carte[y][x-2]>0 :
        liste.append(2)
    if y+2<hauteur-1 and carte[y+2][x]>0 :
        liste.append(3)
    if y-2>0 and carte[y-2][x]>0 :
        liste.append(1)
    return liste

def destinationsPossiblesAvecZero(carte,x,y,largeur,hauteur):
    liste=[]
    if x+2<largeur-1 :
        liste.append(0)
    if x-2>0 :
        liste.append(2)
    if y+2<hauteur-1 :
        liste.append(3)
    if y-2>0 :
        liste.append(1)
    return liste

def creuseAutour(carte,x,y,largeur,hauteur) :
    if x+1<largeur-1 : carte[y][x+1]=0
    if x-1>0: carte[y][x-1]=0
    if y+1<hauteur-1 : carte[y+1][x]=0
    if y-1>0 : carte[y-2][x]>0

def nouveauCheminDepuis(carte,x,y,largeur,hauteur,t):
    carte[y][x]=0
    liste=destinationsPossibles(carte,x,y,largeur,hauteur)
    if len(liste)==0:
        #creuse encore un coup pour débugger
        #creuseAutour(carte,x,y,largeur,hauteur)
        return
    else :
        choix=choice(liste)
        if choix==0:
            carte[y][x+1]=0
            carte[y][x+2]=0
            x,y=x+2,y
        elif choix==2:
            carte[y][x-1]=0
            carte[y][x-2]=0
            x,y=x-2,y
        elif choix==1:
            carte[y-1][x]=0
            carte[y-2][x]=0
            x,y=x,y-2
        else :
            carte[y+1][x]=0
            carte[y+2][x]=0
            x,y=x,y+2
        #basculer
        bascule()
        if t>0 : nouveauCheminDepuis(carte,x,y,largeur,hauteur,t-1)
        else : return
    
#ne marche pas  
def nouveauCheminJusqueZeroPasDansCheminEnCours(carte,x0,y0,largeur,hauteur):
    x,y=x0,y0 #pour rentrer dans while
    while carte[y][x]==0 :
        x,y=origineInitiale(carte,largeur,hauteur)
    ancienne=copieCarte(carte,largeur,hauteur)
    while carte[y][x]>0 or not ancienne[y][x]==0:
        carte[y][x]=0
        #print("debut chemin en",x,y)
        #afficheCarte(carte,largeur,hauteur)
        liste=destinationsPossiblesAvecZero(carte,x,y,largeur,hauteur)
        choix=choice(liste)
        #print(choix)
        if choix==0:
            carte[y][x+1]=0
            x,y=x+2,y
        elif choix==2:
            carte[y][x-1]=0
            x,y=x-2,y
        elif choix==1:
            carte[y-1][x]=0
            x,y=x,y-2
        else :
            carte[y+1][x]=0
            x,y=x,y+2
        #basculer
        bascule()
        
def newCarte(largeur,hauteur):      
    global carte
    carte=cartePLeineDeUns(largeur,hauteur)
    #afficheCarte(carte,largeur,hauteur)
    if nbreCasesEncoreACreuser(carte,largeur,hauteur) >0 :
        x0,y0=origineInitiale(carte,largeur,hauteur)
        t=((largeur)//2*(hauteur)//2)//3
        nouveauCheminDepuis(carte,x0,y0,largeur,hauteur,t)
    #afficheCarte(carte,largeur,hauteur)
    while nbreCasesEncoreACreuser(carte,largeur,hauteur) >0 :
        nouveauCheminJusqueZeroPasDansCheminEnCours(carte,x0,y0,largeur,hauteur)
        #afficheCarte(carte,largeur,hauteur)

    return carte

def newCarteAvecDepartEtArrivee(largeur,hauteur):
    nouvelle=newCarte(largeur,hauteur)
    x,y=2*randrange(largeur//2)+1,0
    nouvelle[y][x]=3
    x,y=2*randrange(hauteur//2)+1,hauteur-1
    nouvelle[y][x]=4252
    return nouvelle

carte=newCarte(largeur,hauteur)

pygame.quit()

