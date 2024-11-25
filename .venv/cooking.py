import pandas as pds
from math import sqrt
from tkiteasy1 import *

longueur = 1532
largeur = 800
dimMorpion = 800


class Pokemon :

    def __init__(self,g):
        self.df = pds.read_csv('poke.csv', index_col="Name")
        self.g = g
        self.pokedex_joueur1 = []
        self.pokedex_joueur2 = []
        self.pokeplacer = {}  #pokemon placer sur le plteau, cle coordonnee, valeur nom du pokemon
        #self.init_pokedex()
        self.nbp = 42







    def JeuPoke(self):
        self.init_pokedex()
        self.afficherpokemon()
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
        self.ban = {}
        self.win = {}
        self.victoire = {}
        self.MegaGrille = [0 for _ in range(9)]

        for i in range(1,3):
            self.g.placerAuDessous(self.g.dessinerLigne(i * dimMorpion/3, 0, i * dimMorpion/3, dimMorpion , "white",ep=5))
            self.g.placerAuDessous(self.g.dessinerLigne(0,dimMorpion/3 * i, dimMorpion, dimMorpion/3 * i, "white",ep=5))
        for i in range(3):
            for j in range(3):
                self.g.placerAuDessous(self.dessinerPetiteGrille(i, j))
        self.g.placerAuDessous(self.g.dessinerLigne(dimMorpion,0,dimMorpion,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,dimMorpion,dimMorpion,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,0,0,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,0,dimMorpion,0,"white",ep=5))
        encadre = None
        joueur = 1
        cliquable = None
        Text1 = self.g.afficherTexte("Joueur1", dimMorpion / 2 + 800, 10, "green")
        while True:


            clic = self.g.attendreClic()
            self.win = {}

            if 0 < clic.x < dimMorpion and 0 < clic.y < dimMorpion:


                grande_case, petite_case = self.determinerCase(clic.x, clic.y)
                if grande_case in self.ban:
                    print(f"Vous devez jouer dans une autre grande case. La grande case {grande_case} est bannie.")
                    continue

                if (grande_case == cliquable and encadre!=None):
                    if self.lists[grande_case][petite_case-1]==0:

                        self.g.supprimer(encadre)
                        encadre = None


                if cliquable is not None and grande_case != cliquable :
                    print(f"Vous devez jouer dans la grande case {cliquable}.")

                    continue

                if self.RemplirGrille(grande_case, petite_case, joueur):
                    self.Regle(grande_case, joueur)
                    cliquable = self.Transfert(grande_case,petite_case)
                    joueur = 3 - joueur
                    self.g.supprimer(Text1)
                    if joueur == 1:
                        Text1 = self.g.afficherTexte("Joueur1", dimMorpion / 2 + 800, 10, "green")
                    else:
                        Text1 = self.g.afficherTexte("Joueur2", dimMorpion / 2 + 800, 10, "green")

                    if cliquable is not None :
                        xc,yc = self.dessinerEncadrement(cliquable)
                        encadre = self.g.dessinerRectangle(xc,yc,dimMorpion/3,dimMorpion/3,col="purple")
                        self.g.placerAuDessous(encadre)




    def Regle(self,grande_case,joueur):
        x = None
        if joueur ==1 :
            x =1
        else :
            joueur = 2
        liste = self.lists[grande_case]
        if ((liste[0] == liste[1] == liste[2]) and liste[0]!=0 ) or ((liste[3] == liste[4] == liste[5]) and liste[3]!=0 ) or ((liste[6] == liste[7] == liste[8]) and liste[6]!=0 ) or ((liste[0] == liste[4] == liste[8]) and liste[0]!=0 ) or ((liste[0] == liste[3] == liste[6]) and liste[0]!=0 ) or ((liste[1] == liste[4] == liste[7]) and liste[1]!=0) or ((liste[2] == liste[5] == liste[8]) and liste[2]!=0) or ((liste[6] == liste[4] == liste[2]) and liste[6]!=0)  :
            self.MegaGrille[grande_case-1] = joueur
            self.ban[grande_case] = self.lists[grande_case]
            self.win[grande_case] = self.lists[grande_case]
            self.victoire[grande_case] = joueur
            print(self.ban)
            self.dessinerCroix(grande_case, joueur)
            self.Finale()


    def Finale(self):
        if ((self.MegaGrille[0] == self.MegaGrille[1] == self.MegaGrille[2]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[3] == self.MegaGrille[4] == self.MegaGrille[5]) and self.MegaGrille[3]!=0 ) or ((self.MegaGrille[6] == self.MegaGrille[7] == self.MegaGrille[8]) and self.MegaGrille[6]!=0 ) or ((self.MegaGrille[0] == self.MegaGrille[4] == self.MegaGrille[8]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[0] == self.MegaGrille[3] == self.MegaGrille[6]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[1] == self.MegaGrille[4] == self.MegaGrille[7]) and self.MegaGrille[1]!=0) or ((self.MegaGrille[2] == self.MegaGrille[5] == self.MegaGrille[8]) and self.MegaGrille[2]!=0) or ((self.MegaGrille[6] == self.MegaGrille[4] == self.MegaGrille[2]) and self.MegaGrille[6]!=0) :
            self.g.afficherTexte("FINITOOOO", dimMorpion/2, dimMorpion/2,"purple")
            self.g.attendreClic()
            self.g.supprimerTout()

            self.menu()


    def dessinerCroix(self, grande_case, joueur):
        taille = dimMorpion / 3
        colonne = (grande_case -1) % 3
        ligne = (grande_case -1)  // 3
        x = (taille * colonne )
        y = (taille* ligne )
        x1 = x+taille
        y1 = y+taille
        yc= (y1+y)/2
        xc = (x1 + x) / 2
        couleur = "royalblue" if joueur == 1 else "tomato"
        forme = "x" if joueur ==1 else "o"
        self.g.dessinerRectangle(x+3,y+3,taille-5,taille-5, couleur)
        self.g.afficherTexte(forme,xc,yc-(taille/8),"white",sizefont = int(taille))


    def dessinerEncadrement(self, grande_case):
        TaillGC = dimMorpion / 3
        colonne_grande = (grande_case - 1) % 3
        ligne_grande = (grande_case - 1) // 3
        x0 = colonne_grande * TaillGC
        y0 = ligne_grande * TaillGC
        return x0,y0


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
        xc = x - taille_petite_case/2
        yc = y - taille_petite_case/2
        if joueur == 1 :
            self.g.afficherTexte("X",x,y, "white",sizefont = int(taille_petite_case/2))
            self.g.placerAuDessous(self.g.dessinerRectangle(xc,yc,taille_petite_case,taille_petite_case,"royalblue"))
        if joueur == 2 :
            self.g.afficherTexte("O",x,y, "white",sizefont = int(taille_petite_case/2))
            self.g.placerAuDessous(self.g.dessinerRectangle(xc,yc,taille_petite_case,taille_petite_case,"tomato"))

    def Transfert(self,grande_case, petite_case):
        liste = self.lists[petite_case]
        if petite_case in self.ban:
            return None
        if grande_case in self.win:
            return petite_case
        if grande_case in self.ban:
            return None
        if all(i != 0 for i in liste) :
            return None
        else :
            return petite_case

    def RemplirGrille(self, grande_case, petite_case, joueur):
        print("cest au tour du joueur",joueur)
        print(self.pokeplacer)
        J = None
        adv = None
        if joueur % 2 == 0:
            J = 2
            adv = 1
        else:
            J = 1
            adv = 2 # Verification
        if self.lists[grande_case][petite_case - 1] == (3 or 4):
            print(f"Case {petite_case} dans la grande case {grande_case} déjà remportée !")
            return False

        if self.lists[grande_case][petite_case - 1] == 0:
            self.lists[grande_case][petite_case - 1] = joueur
            self.placerpokemon(grande_case,petite_case,joueur)
            print(self.pokeplacer)
            self.Affichage(grande_case,petite_case, joueur)
            return True

        if self.lists[grande_case][petite_case - 1] == joueur:
            print("Vous occuper deja cette case")
            return False

        if self.lists[grande_case][petite_case - 1] == adv:
            attaquant = self.choixpoke(joueur)
            if self.combat(attaquant, grande_case, petite_case, joueur) == True:
                gagnant = 1
            else :
                gagnant = 2
            print("le gagnant est le pokemon du joueur",gagnant)
            self.Affichage(grande_case,petite_case,gagnant)

    def init_pokedex(self):
        self.dicopoke1 = {}
        self.dicopoke2 = {}
        joueur1_df = self.df.sample(n=self.nbp, random_state=1)  # Pokémon du joueur 1
        joueur2_df = self.df.sample(n=self.nbp, random_state=2)  # Pokémon du joueur 2

        self.numpokedexj1 = joueur1_df["#"].tolist()
        self.numpokedexj2 = joueur2_df["#"].tolist()

        # Stocker les noms des Pokémon
        self.pokedex_joueur1 = joueur1_df.index.tolist()
        self.pokedex_joueur2 = joueur2_df.index.tolist()

        self.dicopoke1[1] = self.numpokedexj1
        self.dicopoke2[1]= self.numpokedexj2

        print("Pokédex du Joueur 1 :")
        print(self.pokedex_joueur1)

        print("Pokédex du Joueur 2 :")
        print(self.pokedex_joueur2)

    def choixpoke(self, joueur):
        print(self.dicopoke1)
        poke = None
        if joueur == 1:
            print(self.pokedex_joueur1)
            poke = self.pokedex_joueur1
        else :
            print(self.pokedex_joueur2)
            poke = self.pokedex_joueur2
        pokemon = None
        while pokemon is None:
            clic = self.g.attendreClic()
            for (x,y) in self.dicopoke1[0]:
                if abs(clic.x - x)  + abs(clic.y - y) <= 20:
                    choix = self.dicopoke1[(x,y)]
                    print(choix)
            if choix in poke:
                return choix
            else :
                print("entrer un nom de pokemon valide")

    def afficherpokemon(self):
        entier = int(sqrt(self.nbp))
        if entier < sqrt(self.nbp):
            entier += 1
        diametre = ((largeur) * (15/ 16)) / (entier)
        cpt = 0
        cptpoke = 1
        for l in range(entier):
            for c in range(entier):
                if cpt < self.nbp:
                    #if cptpoke < 10:
                     #   cptpok = "00" + str(cptpoke)
                   # elif cptpoke < 100:
                    #    cptpok = "0" + str(cptpoke)
                    #else:
                     #   cptpok = str(cptpoke)

                    cptpok = str(self.numpokedexj1[cpt])
                    x1 = (10 / (entier ** (0.3)) + 5 + diametre * c)
                    y1 = (10 / (entier ** (0.3)) + 5 + diametre * l)
                    x = x1 - (3 / 40) * (x1 - 350)
                    y = y1 - (3 / 40) * (y1 - 350)
                    self.dicopoke1[(x,y)] = self.pokedex_joueur1[cpt]
                    self.dicopoke1[0] = (x,y)
                    self.g.afficherImage(x+800,y,f"./pokefront/{cptpok}.png",int(96/(entier**0.010)),int(96/(entier**0.010)))
                    cpt+=1
                cptpoke+=1



    def placerpokemon(self,grande_case,petite_case,joueur):  #Associe pokemon a une case
        pokemon = self.choixpoke(joueur)
        self.pokeplacer[(petite_case,grande_case)] = pokemon
        print("la case", (petite_case,grande_case), "est occupé par le pokemon", pokemon)


    def combat(self, attaquant_nom, grande_case, petite_case, joueur):
    # Récupérer le nom du Pokémon défenseur
        defenseur_nom = self.pokeplacer.get((grande_case, petite_case))
        if defenseur_nom is None:
            print(f"Aucun Pokémon trouvé dans la case {grande_case}, {petite_case}.")
        return False

        # Vérifier si les noms existent dans le DataFrame
        if attaquant_nom not in self.df.index or defenseur_nom not in self.df.index:
            print(f"Erreur : {attaquant_nom} ou {defenseur_nom} ne sont pas présents dans le DataFrame.")
            return False

        # Extraire les statistiques des Pokémon depuis le DataFrame
        attaquant_stats = self.df.loc[attaquant_nom]
        defenseur_stats = self.df.loc[defenseur_nom]

        attaque_hp = attaquant_stats['HP']
        defenseur_hp = defenseur_stats['HP']

        print(f"Combat : {attaquant_nom} (HP: {attaque_hp}) VS {defenseur_nom} (HP: {defenseur_hp})")

    # Boucle de combat
        while attaque_hp > 0 and defenseur_hp > 0:
        # Attaque de l'attaquant
            degats = max(0, attaquant_stats['Attack'] - defenseur_stats['Defense'])
            defenseur_hp -= degats
            print(f"{attaquant_nom} attaque {defenseur_nom} infligeant {degats} dégâts. HP restant de {defenseur_nom} : {max(0, defenseur_hp)}")

            if defenseur_hp <= 0:
                print(f"{defenseur_nom} est K.O.!")
                return True  # Attaquant gagne

        # Attaque du défenseur
            degats = max(0, defenseur_stats['Attack'] - attaquant_stats['Defense'])
            attaque_hp -= degats
            print(f"{defenseur_nom} attaque {attaquant_nom} infligeant {degats} dégâts. HP restant de {attaquant_nom} : {max(0, attaque_hp)}")

            if attaque_hp <= 0:
                print(f"{attaquant_nom} est K.O.!")
                return False  # Défenseur gagne

    def dessinerPetiteGrille(self, i, j):
        x0 = j * dimMorpion / 3
        y0 = i * dimMorpion / 3
        x1 = x0 + dimMorpion / 3
        y1 = y0 + dimMorpion / 3

        for k in range(1, 3):
            self.g.dessinerLigne(x0 + k * (dimMorpion / 9), y0, x0 + k * (dimMorpion / 9), y1, "white")
            self.g.dessinerLigne(x0, y0 + k * (dimMorpion / 9), x1, y0 + k * (dimMorpion / 9), "white")



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





