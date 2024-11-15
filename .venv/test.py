
from tkiteasy1 import *

(longueur, largeur) = 600,600

class Morpion :
    def __init__(self):
        self.g = ouvrirFenetre(longueur,largeur)
        self.l1 = [0 for _ in range(9)]
        self.l2 = [0 for _ in range(9)]
        self.l3 = [0 for _ in range(9)]
        self.l4 = [0 for _ in range(9)]
        self.l5 = [0 for _ in range(9)]
        self.l6 = [0 for _ in range(9)]
        self.l7 = [0 for _ in range(9)]
        self.l8 = [0 for _ in range(9)]
        self.l9 = [0 for _ in range(9)]
        # Dictionnaire pour associer les grandes cases aux listes
        self.lists = {
            1: self.l1,
            2: self.l2,
            3: self.l3,
            4: self.l4,
            5: self.l5,
            6: self.l6,
            7: self.l7,
            8: self.l8,
            9: self.l9
        }
        self.MegaGrille = [0 for _ in range(9)]
        self.initgraph()

    def initgraph(self):
        for i in range(1,3):
            self.g.dessinerLigne(i * largeur/3, 0, i * largeur/3, longueur , "red")
            self.g.dessinerLigne(0,longueur/3 * i, largeur, longueur/3 * i, "red")
        for i in range(3):
            for j in range(3):
                self.dessinerPetiteGrille(i, j)

        joueur = 1
        while True:
            if joueur == 1:
                Text1 = self.g.afficherTexte("Joueur1", largeur/2 , 10, "green")
            else:
                Text1 = self.g.afficherTexte("Joueur2", largeur / 2, 10, "green")
            clic = self.g.attendreClic()
            grande_case, petite_case = self.determinerCase(clic.x, clic.y)
            print(f"Clic en ({clic.x}, {clic.y}) => Grande case {grande_case}, Petite case {petite_case}")

            if self.RemplirGrille(grande_case, petite_case, joueur):
                joueur = 3 - joueur
            self.g.supprimer(Text1)

    def Affichage(self,grande_case,petite_case, joueur):
        taille_grande_case = largeur / 3
        taille_petite_case = taille_grande_case / 3
        # Indices de la grande case
        ligne_grande = (grande_case - 1) // 3
        colonne_grande = (grande_case - 1) % 3
        # Indices de la petite case
        ligne_petite = (petite_case - 1) // 3
        colonne_petite = (petite_case - 1) % 3
        # Calcul des coordonnées
        x = colonne_grande * taille_grande_case + colonne_petite * taille_petite_case
        y = ligne_grande * taille_grande_case + ligne_petite * taille_petite_case
        if joueur == 1 :
            self.g.dessinerRectangle(x+0.1,y+0.1,largeur / 9 -0.15, longueur/9-0.15, "blue")
        if joueur == 2 :
            self.g.dessinerRectangle(x+0.1,y+0.1,largeur / 9 -0.15, longueur/9-0.15, "red")



    def RemplirGrille(self,grande_case, petite_case,joueur):
        J = None
        if joueur % 2 == 0:
            J = 2
        else :
            J=1
        liste = self.lists[grande_case]
        #Verification
        if liste[petite_case-1] == 0:
            liste[petite_case - 1] = joueur
            self.Affichage(grande_case,petite_case, joueur)
            return True
        else:
            print(f"Case {petite_case} dans la grande case {grande_case} déjà occupée !")
            return False


    def dessinerPetiteGrille(self, i, j):
        x0 = j * largeur / 3
        y0 = i * longueur / 3
        x1 = x0 + largeur / 3
        y1 = y0 + longueur / 3

        for k in range(1, 3):
            self.g.dessinerLigne(x0 + k * (largeur / 9), y0, x0 + k * (largeur / 9), y1, "blue")
            self.g.dessinerLigne(x0, y0 + k * (longueur / 9), x1, y0 + k * (longueur / 9), "blue")



    def determinerCase(self, x, y):
        taille_case_grande_x = largeur / 3
        taille_case_grande_y = longueur / 3
        taille_case_petite_x = largeur / 9
        taille_case_petite_y = longueur / 9

        # Trouver la grande case
        colonne_grande = int(x // taille_case_grande_x)
        ligne_grande = int(y // taille_case_grande_y)
        numero_grande_case = ligne_grande * 3 + colonne_grande + 1

        # Trouver la petite case dans la grande case
        x_relative = x % taille_case_grande_x
        y_relative = y % taille_case_grande_y
        colonne_petite = int(x_relative // taille_case_petite_x)
        ligne_petite = int(y_relative // taille_case_petite_y)
        numero_petite_case = ligne_petite * 3 + colonne_petite + 1

        return numero_grande_case, numero_petite_case




Morpion()

