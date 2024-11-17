
from tkiteasy1 import *

dimMorpion = 800

class Morpion :
    def __init__(self):
        self.g = ouvrirFenetre(1532,800)
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
        self.menu()


    def menu(self):
        menu = self.g.afficherImage(0, 0, "./MenuPokemon.png")
        testjeusolo = self.g.dessinerRectangle(950,645,470,55,"white")
        testsetting = self.g.dessinerRectangle(950,710,470,55,"white")
        while True:
            cliquesouris = self.g.attendreClic()
            if 480 < cliquesouris.x < 1420 and 525 < cliquesouris.y < 635:
                self.g.supprimer(menu)
                self.initgraph()


    def initgraph(self):

        for i in range(1,3):
            self.g.dessinerLigne(i * dimMorpion/3, 0, i * dimMorpion/3, dimMorpion , "red")
            self.g.dessinerLigne(0,dimMorpion/3 * i, dimMorpion, dimMorpion/3 * i, "red")
        for i in range(3):
            for j in range(3):
                self.dessinerPetiteGrille(i, j)
        ligne1 = None
        ligne2 = None
        ligne3 = None
        ligne4 = None
        joueur = 1
        cliquable = None
        Text1 = self.g.afficherTexte("Joueur1", dimMorpion / 2 + 800, 10, "green")
        while True:


            clic = self.g.attendreClic()


            if 0 < clic.x < dimMorpion and 0 < clic.y < dimMorpion:


                grande_case, petite_case = self.determinerCase(clic.x, clic.y)

                if (grande_case == cliquable and ligne1 != None and ligne2 != None and ligne3 != None and ligne4 != None):
                    if self.lists[grande_case][petite_case-1]==0:

                        self.g.supprimer(ligne1)
                        self.g.supprimer(ligne2)
                        self.g.supprimer(ligne3)
                        self.g.supprimer(ligne4)
                        ligne1 = None
                        ligne2 = None
                        ligne3 = None
                        ligne4 = None


                if cliquable is not None and grande_case != cliquable:
                    print(f"Vous devez jouer dans la grande case {cliquable}.")

                    continue

                if self.RemplirGrille(grande_case, petite_case, joueur):
                    cliquable = self.Transfert(grande_case,petite_case)
                    if cliquable is not None:
                        (x0, y0,x1,y1) = self.dessinerEncadrement(cliquable)
                        ligne1 = self.g.dessinerLigne(x0, y0, x1, y0, "green")
                        ligne2 = self.g.dessinerLigne(x1, y0, x1, y1, "green")
                        ligne3 = self.g.dessinerLigne(x1, y1, x0, y1, "green")
                        ligne4 = self.g.dessinerLigne(x0, y1, x0, y0, "green")
                        joueur = 3 - joueur

                        self.g.supprimer(Text1)
                        if joueur == 1:
                            Text1 = self.g.afficherTexte("Joueur1", dimMorpion / 2 + 800, 10, "green")
                        else:
                            Text1 = self.g.afficherTexte("Joueur2", dimMorpion / 2 + 800, 10, "green")


    def dessinerEncadrement(self, grande_case):
        TaillGC = dimMorpion / 3
        colonne_grande = (grande_case - 1) % 3
        ligne_grande = (grande_case - 1) // 3
        x0 = colonne_grande * TaillGC
        y0 = ligne_grande * TaillGC
        x1 = x0 + TaillGC
        y1 = y0 + TaillGC

        return x0,y0,x1,y1


    def Affichage(self,grande_case,petite_case, joueur):
        taille_grande_case = dimMorpion / 3
        taille_petite_case = taille_grande_case / 3
        # Indices de la grande case
        ligne_grande = (grande_case - 1) // 3
        colonne_grande = (grande_case - 1) % 3
        # Indices de la petite case
        ligne_petite = (petite_case - 1) // 3
        colonne_petite = (petite_case - 1) % 3
        # Calcul des coordonnées du centre
        x = (colonne_grande * taille_grande_case + colonne_petite * taille_petite_case
             + taille_petite_case / 2)
        y = (ligne_grande * taille_grande_case + ligne_petite * taille_petite_case
             + taille_petite_case / 2)
        if joueur == 1 :
            self.g.afficherTexte("X",x,y, "blue")
        if joueur == 2 :
            self.g.afficherTexte("O",x,y, "red")

    def Transfert(self,grande_case, petite_case):
        liste = self.lists[petite_case]
        if all(i != 0 for i in liste):
            return None
        else :
            return petite_case

    def RemplirGrille(self,grande_case, petite_case,joueur):
        J = None
        if joueur % 2 == 0:
            J = 2
        else :
            J=1        #Verification
        if self.lists[grande_case][petite_case-1] == 0:
            self.lists[grande_case][petite_case-1] = joueur
            self.Affichage(grande_case,petite_case, joueur)
            return True
        else:
            print(f"Case {petite_case} dans la grande case {grande_case} déjà occupée !")
            return False


    def dessinerPetiteGrille(self, i, j):
        x0 = j * dimMorpion / 3
        y0 = i * dimMorpion / 3
        x1 = x0 + dimMorpion / 3
        y1 = y0 + dimMorpion / 3

        for k in range(1, 3):
            self.g.dessinerLigne(x0 + k * (dimMorpion / 9), y0, x0 + k * (dimMorpion / 9), y1, "blue")
            self.g.dessinerLigne(x0, y0 + k * (dimMorpion / 9), x1, y0 + k * (dimMorpion / 9), "blue")



    def determinerCase(self, x, y):
        taille_case_grande_x = dimMorpion / 3
        taille_case_grande_y = dimMorpion / 3
        taille_case_petite_x = dimMorpion / 9
        taille_case_petite_y = dimMorpion / 9

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

