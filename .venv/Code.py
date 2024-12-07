import pandas as pds
from math import sqrt
from tkiteasy1 import *
import random

longueur = 1532
largeur = 800
dimMorpion = 800
type = {
    'Normal': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 1,
               'Ground': 1,
               'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 0.5, 'Ghost': 0, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5,
               'Fairy': 1},

    'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2, 'Ice': 2, 'Fighting': 1, 'Poison': 1,
             'Ground': 1,
             'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 2,
             'Fairy': 1},

    'Water': {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Electric': 1, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 1,
              'Ground': 2,
              'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1,
              'Fairy': 1},

    'Electric': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1,
                 'Poison': 1, 'Ground': 0,
                 'Flying': 2, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1,
                 'Fairy': 1},

    'Grass': {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Electric': 1, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 0.5,
              'Ground': 2,
              'Flying': 0.5, 'Psychic': 1, 'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 0.5,
              'Fairy': 1},

    'Ice': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2, 'Ice': 0.5, 'Fighting': 1, 'Poison': 1,
            'Ground': 2,
            'Flying': 2, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5,
            'Fairy': 1},

    'Fighting': {'Normal': 2, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 2, 'Fighting': 1, 'Poison': 0.5,
                 'Ground': 1,
                 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2, 'Ghost': 0, 'Dragon': 1, 'Dark': 2, 'Steel': 2,
                 'Fairy': 0.5},

    'Poison': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 2, 'Ice': 1, 'Fighting': 1, 'Poison': 0.5,
               'Ground': 0.5,
               'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 0.5, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 1, 'Steel': 0,
               'Fairy': 2},

    'Ground': {'Normal': 1, 'Fire': 2, 'Water': 1, 'Electric': 2, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 2,
               'Ground': 1,
               'Flying': 0, 'Psychic': 1, 'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 2,
               'Fairy': 1},

    'Flying': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 0.5, 'Grass': 2, 'Ice': 1, 'Fighting': 2, 'Poison': 1,
               'Ground': 1,
               'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5,
               'Fairy': 1},

    'Psychic': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 2,
                'Ground': 1,
                'Flying': 1, 'Psychic': 0.5, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 0, 'Steel': 0.5,
                'Fairy': 1},

    'Bug': {'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Electric': 1, 'Grass': 2, 'Ice': 1, 'Fighting': 0.5, 'Poison': 0.5,
            'Ground': 1,
            'Flying': 0.5, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 2, 'Steel': 0.5,
            'Fairy': 0.5},

    'Rock': {'Normal': 1, 'Fire': 2, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 2, 'Fighting': 0.5, 'Poison': 1,
             'Ground': 0.5,
             'Flying': 2, 'Psychic': 1, 'Bug': 2, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5,
             'Fairy': 1},

    'Ghost': {'Normal': 0, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 1,
              'Ground': 1,
              'Flying': 1, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0.5, 'Steel': 1,
              'Fairy': 1},

    'Dragon': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 1,
               'Ground': 1,
               'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5,
               'Fairy': 0},

    'Dark': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 0.5, 'Poison': 1,
             'Ground': 1,
             'Flying': 1, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0.5, 'Steel': 1,
             'Fairy': 0.5},

    'Steel': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 1, 'Ice': 2, 'Fighting': 1,
              'Poison': 1, 'Ground': 1,
              'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5,
              'Fairy': 2},

    'Fairy': {'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 0.5,
              'Ground': 1,
              'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 2, 'Steel': 0.5,
              'Fairy': 1}
}


class IAPOKEBETE :

    def __init__(self,morpion,g):
        self.morpion = morpion
        self.g = g
        self.df = pds.read_csv('poke.csv', index_col="Name")
        print(self.df)
          #pokemon placer sur le plteau, cle coordonnee, valeur nom du pokemon






    def JeuPoke(self,nbp):
        self.nbp = nbp
        self.pokedex_joueur1 = []
        self.pokedex_joueur2 = []
        self.pokeplacer = {}
        self.init_pokedex()
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
        self.g.dessinerLigne(dimMorpion,635,1532,635,"white",ep=5)
        self.g.placerAuDessous(self.g.dessinerLigne(dimMorpion,0,dimMorpion,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,dimMorpion,dimMorpion,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,0,0,dimMorpion,"white",ep=5))
        self.g.placerAuDessous(self.g.dessinerLigne(0,0,dimMorpion,0,"white",ep=5))
        self.g.placerAuDessous(self.g.afficherImage(dimMorpion, 0, "./fondjeu.png", 1532 - dimMorpion, dimMorpion))

        encadre = None
        joueur = 1
        cliquable = None
        Text1 = self.g.afficherTexte("Joueur1", dimMorpion / 2 + 800, 10, "green")
        cpt = 0
        self.pokemon = []
        condition = False
        cond = False
        condi = False
        self.afficherpokemon2(cpt)
        carrénoir = self.g.afficherImage(805, 0,"./fond pc.png" ,1532 - 805, 635)
        self.joueur = self.g.afficherImage(970,20,"./Joueur 1.png",400,60)
        self.j = self.g.afficherImage(1355,-10,"./pokefront/160.png",96,96)
        self.afficherpokemon(cpt)
        self.rond = self.g.dessinerDisque(930,50,29,"white")
        self.home = self.g.afficherImage(885, 5, "./Home.png",90,90)
        self.loupe = self.g.afficherImage(1455,10,"./Loupe.png",70,70)
        self.stat = None
        self.f = None
        while True:


            if condition == True:
                if joueur ==1 and len(self.dicoimage1)!=0:
                    self.g.placerAuDessus(carrénoir)
                    self.rond = self.g.dessinerDisque(930, 50, 29, "white")
                    self.home = self.g.afficherImage(885, 5, "./Home.png", 90, 90)
                    self.g.supprimer(self.joueur)
                    self.g.supprimer(self.j)
                    self.j = self.g.afficherImage(1355, -10, "./pokefront/160.png", 96, 96)
                    self.joueur = self.g.afficherImage(970,20,"./Joueur 1.png",400,60)
                    for i in self.dicoimage1:
                        self.g.placerAuDessus(i)

                    condition = False
                if joueur ==2 and len(self.dicoimage2) !=0:
                    self.g.placerAuDessus(carrénoir)
                    self.rond = self.g.dessinerDisque(930, 50, 29, "white")
                    self.home = self.g.afficherImage(885, 5, "./Home.png", 90, 90)
                    self.g.supprimer(self.joueur)
                    self.g.supprimer(self.j)
                    self.j = self.g.afficherImage(1355,-10,"./pokefront/157.png",96,96)
                    self.joueur = self.g.afficherImage(970, 20, "./Joueur 2.png", 400, 60)
                    for i in self.dicoimage2:
                        self.g.placerAuDessus(i)
                    condition = False

            for i in range(1, 3):
                self.g.placerAuDessus(
                    self.g.dessinerLigne(i * dimMorpion / 3, 0, i * dimMorpion / 3, dimMorpion, "white", ep=5))
                self.g.placerAuDessus(
                    self.g.dessinerLigne(0, dimMorpion / 3 * i, dimMorpion, dimMorpion / 3 * i, "white", ep=5))
            self.g.placerAuDessus(self.g.dessinerLigne(dimMorpion, 0, dimMorpion, dimMorpion, "white", ep=5))
            self.g.placerAuDessus(self.g.dessinerLigne(0, dimMorpion, dimMorpion, dimMorpion, "white", ep=5))
            self.g.placerAuDessus(self.g.dessinerLigne(0, 0, 0, dimMorpion, "white", ep=5))
            self.g.placerAuDessus(self.g.dessinerLigne(0, 0, dimMorpion, 0, "white", ep=5))

            if joueur == 1:
                clic = self.g.attendreClic()
            elif joueur != 1:
                clic.x, clic.y = random.uniform(0, 1532), random.uniform(0, 1532)

            self.win = {}

            if joueur==1:
                if (((clic.x - 930)) ** 2 + ((clic.y - 50)) ** 2) ** 0.5 <= 29:
                    self.g.supprimerTout
                    self.morpion.menu()



            if 0 < clic.x < dimMorpion and 0 < clic.y < dimMorpion:


                grande_case, petite_case = self.determinerCase(clic.x, clic.y)
                if grande_case in self.ban:
                    print(f"Vous devez jouer dans une autre grande case. La grande case {grande_case} est bannie.")
                    continue

                if (grande_case == cliquable and encadre!=None and len(self.pokemon)!=0):
                    if self.lists[grande_case][petite_case-1]==0 or 3-joueur:

                        self.g.supprimer(encadre)
                        encadre = None


                if cliquable is not None and grande_case != cliquable :
                    print(f"Vous devez jouer dans la grande case {cliquable}.")

                    continue

                if len(self.pokemon)!=0 and self.RemplirGrille(grande_case, petite_case, joueur) :

                    self.Regle(grande_case, joueur)
                    cliquable = self.Transfert(grande_case,petite_case)
                    joueur = 3 - joueur
                    condi = False
                    condition = True

                    self.pokemon = []
                    self.g.supprimer(Text1)
                    cpt+=1
                    if joueur == 1:
                        Text1 = self.g.afficherTexte("Joueur1", dimMorpion / 2 + 800, 10, "green")
                    else:
                        Text1 = self.g.afficherTexte("Joueur2", dimMorpion / 2 + 800, 10, "green")

                    if cliquable is not None :
                        xc,yc = self.dessinerEncadrement(cliquable)
                        encadre = self.g.dessinerRectangle(xc,yc,dimMorpion/3,dimMorpion/3,col="purple")
                        self.g.placerAuDessous(encadre)

            else:
                if joueur == 1:
                    if 1455 < clic.x < 1525 and 10 < clic.y < 80:
                        condi = self.filtre(joueur)

                    if condi != False:
                        cond = self.choixfiltre(joueur,clic,cond,condi)
                    if condi == False:
                        cond = self.choixpoke(joueur,clic,cond)
                else:
                    cond = self.choixpoke(joueur, clic, cond)

    def choixfiltre(self,joueur,clic,condition,Type):
        self.pokemon = []
        self.select = []

        if joueur == 1:
            print(self.pokedex_joueur1)
            poke = self.pokedex_joueur1
            dico = self.dicopoke1
            num = self.numpokedexj1
            dfj = self.joueur1_df
        else:
            print(self.pokedex_joueur2)
            poke = self.pokedex_joueur2
            dico = self.dicopoke2
            num = self.numpokedexj2
            dfj = self.joueur2_df

        nb_pokemon = self.nbp
        entier = int(sqrt(nb_pokemon))
        if entier < sqrt(nb_pokemon):
            entier += 1
        largeur_cellule = 732 / entier  # Largeur des cellules
        hauteur_cellule = 600 / entier  # Hauteur des cellules
        for cle in dico:
            if cle != 1:
                x, y = cle

                x_min = x - largeur_cellule / 2
                x_max = x + largeur_cellule / 2
                y_min = y - hauteur_cellule / 2
                y_max = y + hauteur_cellule / 2

                if x_min < clic.x < x_max and y_min < clic.y < y_max:
                    choix = dico[cle]
                    pokestat = dfj.loc[choix]
                    if pokestat['Type 1'] == Type or pokestat['Type 2'] == Type:
                        self.i = poke.index(choix)
                        self.select.append(num[self.i])
                        self.pokemon.append(choix)
                        self.co = (x, y)

                        if condition == True:
                            self.g.supprimer(self.stat)
                            self.g.supprimer(self.type1)
                            self.g.supprimer(self.hp)
                            self.g.supprimer(self.attaque)
                            self.g.supprimer(self.defense)
                            self.g.supprimer(self.vitesse)
                            self.g.supprimer(self.attspe)
                            self.g.supprimer(self.defspe)
                            self.g.supprimer(self.level)
                            if self.type2:
                                self.g.supprimer(self.type2)
                        self.level = self.g.afficherTexte(f"Niveau : {pokestat['Level']}", 1395, 750, col="white",
                                                          sizefont=18)
                        self.defspe = self.g.afficherTexte(f"Def Spe : {pokestat['Sp. Def']}", 1200, 750, col="white",
                                                           sizefont="18")
                        self.attspe = self.g.afficherTexte(f"Atk Spe : {pokestat['Sp. Atk']}", 1200, 710, col="white",
                                                           sizefont="18")
                        self.vitesse = self.g.afficherTexte(f"Vitesse : {pokestat['Speed']}", 1200, 670, col="white",
                                                            sizefont="18")
                        self.defense = self.g.afficherTexte(f"Defense : {pokestat['Defense']}", 1000, 750, col="white",
                                                            sizefont="18")
                        self.attaque = self.g.afficherTexte(f"Attaque : {pokestat['Attack']}", 1000, 710, col="white",
                                                            sizefont="18")
                        self.hp = self.g.afficherTexte(f"Hp : {pokestat['HP']}", 1000, 670, col="white", sizefont="18")
                        self.stat = self.g.afficherImage(805, 660, f"./pokefront/{num[self.i]}.png", 96, 96)
                        self.type1 = self.g.afficherImage(1320, 655, f"./Type/{pokestat['Type 1']}.png", 150, 30)
                        if pokestat['Type 2'] in type:
                            self.type2 = self.g.afficherImage(1320, 695, f"./Type/{pokestat['Type 2']}.png", 150, 30)
                        else:
                            self.type2 = None
                        return True

        if self.stat != None:
            return True
        else:
            return False



    def filtre(self,joueur):
        if joueur == 1:
            dfj = self.joueur1_df
            dico = self.dicopoke1

        else:
            dico = self.dicopoke2
            dfj = self.joueur2_df

        self.type = {}
        filtre = self.g.dessinerRectangle(815,110,700,400,"beige")
        annuler = self.g.afficherTexte("Annuler",900,485,"darkblue",sizefont=24)
        confirmer = self.g.afficherTexte("Confirmer",1385,485,"darkblue",sizefont=24)
        cond = False
        choix = None
        choixt=None
        image = []
        x=880
        y=135
        for cle in type:
            if x > 1400:
                x=880
                y += 50
            image.append(self.g.afficherImage(x,y,f"./Type/{cle}.png",150,30))
            self.type[(x,y)] = cle
            x+=200

        while cond == False:
            if joueur ==1:
                clic = self.g.attendreClic()
            elif joueur != 1:
                clic.x, clic.y = random.uniform(800, 1532), random.uniform(800, 1532)

            for cle in self.type:
                x,y = cle
                if x<clic.x<x+150 and y<clic.y<y+30:
                    if choixt!=None:
                        self.g.supprimer(choixt)
                    choix = self.type[(x,y)]
                    choixt = self.g.afficherImage(1077, 465, f"./Type/{choix}.png", 150, 30)
                    print(f"Le choix du type a filtrer est {choix}")

            if 820<clic.x<1000 and 465<clic.y<505:
                self.g.supprimer(filtre)
                self.g.supprimer(confirmer)
                self.g.supprimer(annuler)
                for i in range(len(image)):
                    self.g.supprimer(image[i])
                if self.f !=None:
                    self.g.supprimer(self.f)
                    self.f = None
                if choixt != None:
                    self.g.supprimer(choixt)
                cond = True
                return False
            if 1300<clic.x<1480 and 465<clic.y<505:
                if choix==None:
                    self.g.supprimer(annuler)
                    self.g.supprimer(filtre)
                    self.g.supprimer(confirmer)
                    for i in range(len(image)):
                        self.g.supprimer(image[i])
                    if self.f !=None:
                        self.g.supprimer(self.f)
                        self.f = None
                    if choixt!=None:
                        self.g.supprimer(choixt)
                    cond = True
                    return False
                if choix !=None:
                    self.g.supprimer(annuler)
                    self.g.supprimer(filtre)
                    self.g.supprimer(confirmer)
                    self.g.supprimer(choixt)
                    for i in range(len(image)):
                        self.g.supprimer(image[i])
                    if self.f !=None:
                        self.g.supprimer(self.f)
                    self.f = self.g.afficherImage(805,102,"./fondfiltre.png")
                    for cle in dico:
                        if cle != 1:
                            x,y = cle
                            df = dfj.loc[dico[(x,y)]]
                            print(df)
                            if df['Type 1'] == choix or df['Type 2']==choix:
                                self.g.afficherImage(cle[0]-self.largeur_cellule/2,cle[1]-self.hauteur_cellule/2,f"./pokefront/{df['#']}.png",self.taille_image,self.taille_image)
                    return choix

        return False


    def Regle(self,grande_case,joueur):
        x = None
        if joueur ==1 :
            x =1
        else :
            joueur = 2
        liste = self.lists[grande_case]
        if ((liste[0] % 2 == liste[1] % 2 == liste[2] % 2 and liste[0] != 0 and liste[1] != 0 and liste[2] != 0) or (liste[3] % 2 == liste[4] % 2 == liste[5] % 2 and liste[3] != 0 and liste[4] != 0 and liste[5] != 0) or (liste[6] % 2 == liste[7] % 2 == liste[8] % 2 and liste[6] != 0 and liste[7] != 0 and liste[8] != 0) or (liste[0] % 2 == liste[4] % 2 == liste[8] % 2 and liste[0] != 0 and liste[4] != 0 and liste[8] != 0) or (liste[0] % 2 == liste[3] % 2 == liste[6] % 2 and liste[0] != 0 and liste[3] != 0 and liste[6] != 0) or (liste[1] % 2 == liste[4] % 2 == liste[7] % 2 and liste[1] != 0 and liste[4] != 0 and liste[7] != 0) or (liste[2] % 2 == liste[5] % 2 == liste[8] % 2 and liste[2] != 0 and liste[5] != 0 and liste[8] != 0) or (liste[6] % 2 == liste[4] % 2 == liste[2] % 2 and liste[6] != 0 and liste[4] != 0 and liste[2] != 0)):
            self.MegaGrille[grande_case-1] = joueur
            self.ban[grande_case] = self.lists[grande_case]
            self.win[grande_case] = self.lists[grande_case]
            self.victoire[grande_case] = joueur
            print(self.ban)
            self.dessinerCroix(grande_case, joueur)
            self.Finale(joueur)

    def ecranvictoire(self,joueur):

        self.g.afficherImage(0,0,"./fondviictoire.png")
        if joueur == 1:
            self.g.afficherImage(600,150,"./Joueur 1.png")
        else:
            self.g.afficherImage(600,150,"./Joueur 2.png")
        self.g.afficherImage(600,300,"./gagne.png")

    def ecrangalite(self):
        self.g.afficherImage(0,0,"./fondviictoire.png")
        self.g.afficherImage(600,300,"./egalite.png")

    def Finale(self, joueur):
        if ((self.MegaGrille[0] == self.MegaGrille[1] == self.MegaGrille[2]) and self.MegaGrille[0] != 0) or ((self.MegaGrille[3] == self.MegaGrille[4] == self.MegaGrille[5]) and self.MegaGrille[3] != 0) or ((self.MegaGrille[6] == self.MegaGrille[7] == self.MegaGrille[8]) and self.MegaGrille[6] != 0) or ((self.MegaGrille[0] == self.MegaGrille[4] == self.MegaGrille[8]) and self.MegaGrille[0] != 0) or ((self.MegaGrille[0] == self.MegaGrille[3] == self.MegaGrille[6]) and self.MegaGrille[0] != 0) or ((self.MegaGrille[1] == self.MegaGrille[4] == self.MegaGrille[7]) and self.MegaGrille[1] != 0) or ((self.MegaGrille[2] == self.MegaGrille[5] == self.MegaGrille[8]) and self.MegaGrille[2] != 0) or ((self.MegaGrille[6] == self.MegaGrille[4] == self.MegaGrille[2]) and self.MegaGrille[6] != 0):
            self.g.supprimerTout()
            self.ecranvictoire(joueur)
            self.g.attendreClic()
            self.g.supprimerTout()
            self.morpion.menu()

        if all(i != 0 for i in self.MegaGrille):
            self.ecrangalite()
            self.g.attendreClic()
            self.g.supprimerTout()
            self.morpion.menu()


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
            if self.lists[grande_case][petite_case-1] == 1:
                self.g.afficherImage(xc+10,yc+5, f"./pokefront/{self.select[0]}.png",70,70)
                self.g.placerAuDessous(self.g.dessinerRectangle(xc,yc,taille_petite_case,taille_petite_case,"royalblue"))
            elif self.lists[grande_case][petite_case-1] == 3:
                self.g.dessinerRectangle(xc+1, yc+1, taille_petite_case-1, taille_petite_case-1, "royalblue")
                self.g.afficherTexte("X", x, y, "white", sizefont=int(taille_petite_case / 2))
        if joueur == 2 :
            if self.lists[grande_case][petite_case - 1] == 2:
                self.g.afficherImage(xc+10,yc+5, f"./pokefront/{self.select[0]}.png",70,70)
                self.g.placerAuDessous(self.g.dessinerRectangle(xc,yc,taille_petite_case,taille_petite_case,"tomato"))
            elif self.lists[grande_case][petite_case-1]==4:
                self.g.dessinerRectangle(xc+1, yc+1, taille_petite_case-1, taille_petite_case-1, "tomato")
                self.g.afficherTexte("O", x, y, "white", sizefont=int(taille_petite_case / 2))

    def Transfert(self,grande_case, petite_case):
        liste = self.lists[petite_case]
        if petite_case in self.ban:
            return None
        if grande_case in self.win:
            return petite_case
        if grande_case in self.ban:
            return None
        if all(i !=0 for i in liste) :
            return None
        else :
            return petite_case

    def RemplirGrille(self, grande_case, petite_case, joueur):
        print("cest au tour du joueur",joueur)
        print(self.pokeplacer)
        J = None
        adv = None

        if joueur == 1:
            self.dicojeu1[self.pokemon[0]] = [self.co, self.i,self.select[0]]


        if joueur == 2:
            self.dicojeu2[self.pokemon[0]] = [self.co, self.i,self.select[0]]



        if joueur % 2 == 0:
            dicoim = self.dicoimage2
            dico = self.dicojeu2
            dicopoke = self.dicopoke2
            dfj = self.joueur2_df
            dfjadv = self.joueur1_df
            dicoadv = self.dicojeu1
            dicoimadv = self.dicoimage1
            dicopokeadv = self.dicopoke1
            J = 2
            adv = 1
        else:
            dfj = self.joueur1_df
            dicoim = self.dicoimage1
            dico = self.dicojeu1
            dicopoke = self.dicopoke1
            dfjadv = self.joueur2_df
            dicoadv = self.dicojeu2
            dicoimadv = self.dicoimage2
            dicopokeadv = self.dicopoke2
            J = 1
            adv = 2 # Verification
        if self.lists[grande_case][petite_case - 1] == (3 or 4):
            print(f"Case {petite_case} dans la grande case {grande_case} déjà remportée !")
            return False

        if self.lists[grande_case][petite_case - 1] == 0:
            self.lists[grande_case][petite_case - 1] = joueur
            self.placerpokemon(grande_case,petite_case,joueur)
            self.g.supprimer(dicoim[self.i])
            del dicopoke[self.co]

            print(self.pokeplacer)
            self.Affichage(grande_case,petite_case, joueur)
            return True

        if self.lists[grande_case][petite_case - 1] == joueur:
            print("Vous occuper deja cette case")
            return False

        if self.lists[grande_case][petite_case - 1] == adv:
            attaquant = self.pokemon[0]
            if self.combat(attaquant, grande_case, petite_case, joueur) == True:
                self.lists[grande_case][petite_case-1] = J+2
                gagnant = J
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'Level'] += 1
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'HP'] += 5
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'Attack'] += 5
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'Defense'] += 5
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'Sp. Atk'] += 5
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'Sp. Def'] += 5
                dfjadv.loc[self.pokeplacer[(grande_case,petite_case)], 'Speed'] += 5

                dicoimadv[dicoadv[self.pokeplacer[(grande_case,petite_case)]][1]] = self.g.afficherImage(dicoadv[self.pokeplacer[(grande_case,petite_case)]][0][0]-self.largeur_cellule/2,dicoadv[self.pokeplacer[(grande_case,petite_case)]][0][1]-self.hauteur_cellule/2,f"./pokefront/{dicoadv[self.pokeplacer[(grande_case,petite_case)]][2]}.png",self.taille_image,self.taille_image)
                print(dicoimadv[dicoadv[self.pokeplacer[(grande_case,petite_case)]][1]])
                dicopokeadv[dicoadv[self.pokeplacer[(grande_case,petite_case)]][0]] = self.pokeplacer[(grande_case,petite_case)]
                self.g.supprimer(dicoim[self.i])
                del dicopoke[self.co]
            else :
                dfj.loc[attaquant, 'Level'] += 1
                dfj.loc[attaquant, 'HP'] += 5
                dfj.loc[attaquant, 'Attack'] += 5
                dfj.loc[attaquant, 'Defense'] += 5
                dfj.loc[attaquant, 'Sp. Atk'] += 5
                dfj.loc[attaquant, 'Sp. Def'] += 5
                dfj.loc[attaquant, 'Speed'] += 5
                self.lists[grande_case][petite_case-1] = adv+2
                dico[attaquant] = [self.co, self.i,self.select[0]]
                dicoim[dico[attaquant][1]] = self.g.afficherImage(dico[attaquant][0][0]-self.largeur_cellule/2,dico[attaquant][0][1]-self.hauteur_cellule/2,f"./pokefront/{dico[attaquant][2]}.png",self.taille_image,self.taille_image)
                dicopoke[dico[attaquant][0]] = attaquant
                print(dicopoke[dico[attaquant][0]])
                gagnant = adv
            print("le gagnant est le pokemon du joueur",gagnant)
            self.Affichage(grande_case,petite_case,gagnant)
            return True

    def verifpokedex(self,moyj1,df):
        binf = moyj1*0.95
        bsup = moyj1*1.05
        moyj2 = df['Total'].mean()
        if binf<=moyj2<=bsup:
            return True
        else:
            return None

    def nbtype(self,nbpoketype):
        df2=pds.DataFrame()
        for type in nbpoketype:
            dftype = self.df[self.df['Type 1']==type]
            df2 = pds.concat([df2,dftype.sample(n=nbpoketype[type],replace=False)])
        if len(df2)<self.nbp:
            complete = self.nbp-len(df2)
            dfsansdf2 = self.df.drop(df2.index)
            df2=pds.concat([df2,dfsansdf2.sample(n=complete,replace=False)])
        return df2

    def init_pokedex(self):
        self.dicopoke1 = {}
        self.dicopoke2 = {}
        self.dicojeu1 = {}
        self.dicojeu2 = {}
        self.joueur1_df = self.df.sample(n=self.nbp,replace=False)# Pokémon du joueur 1
        moyj1 = self.joueur1_df['Total'].mean()
        nbpoketypej1 = {}
        for type in self.joueur1_df['Type 1']:
            if type in nbpoketypej1:
                nbpoketypej1[type]+=1
            else:
                nbpoketypej1[type] = 1
        cond = False
        while cond ==False:
            self.joueur2_df = self.nbtype(nbpoketypej1)
            if self.verifpokedex(moyj1,self.joueur2_df) == True:
                cond = True
        #self.joueur2_df = self.df.sample(n=self.nbp,random_state=2)  # Pokémon du joueur 2
        moyj2 = self.joueur2_df['Total'].mean()
        print(f"Moyenne du pokedex 1 : {moyj1}")
        print(f"Moyenne du pokedex 2 : {moyj2}")
        self.numpokedexj1 = self.joueur1_df["#"].tolist()
        self.numpokedexj2 = self.joueur2_df["#"].tolist()

        # Stocker les noms des Pokémon
        self.pokedex_joueur1 = self.joueur1_df.index.tolist()
        self.pokedex_joueur2 = self.joueur2_df.index.tolist()

        self.dicopoke1[1] = self.numpokedexj1
        self.dicopoke2[1]= self.numpokedexj2
        print(self.dicopoke1[1],self.dicopoke1)
        print("Pokédex du Joueur 1 :")
        print(self.pokedex_joueur1)

        print("Pokédex du Joueur 2 :")
        print(self.pokedex_joueur2)

    def choixpoke(self, joueur,clic,condition):
        self.pokemon = []
        self.select = []


        if joueur == 1:
            print(self.pokedex_joueur1)
            poke = self.pokedex_joueur1
            dico = self.dicopoke1
            num = self.numpokedexj1
            dfj = self.joueur1_df
        else:
            print(self.pokedex_joueur2)
            poke = self.pokedex_joueur2
            dico = self.dicopoke2
            num = self.numpokedexj2
            dfj = self.joueur2_df

        nb_pokemon = self.nbp
        entier = int(sqrt(nb_pokemon))
        if entier < sqrt(nb_pokemon):
            entier += 1
        largeur_cellule = 732 / entier  # Largeur des cellules
        hauteur_cellule = 600 / entier  # Hauteur des cellules
        for cle in dico:
            if cle != 1:
                x, y = cle

                x_min = x - largeur_cellule / 2
                x_max = x + largeur_cellule / 2
                y_min = y - hauteur_cellule / 2
                y_max = y + hauteur_cellule / 2

                if x_min < clic.x < x_max and y_min < clic.y < y_max:
                    choix=dico[cle]
                    pokestat = dfj.loc[choix]
                    self.i = poke.index(choix)
                    self.select.append(num[self.i])
                    self.pokemon.append(choix)
                    self.co = (x,y)

                    if condition==True:
                        self.g.supprimer(self.stat)
                        self.g.supprimer(self.type1)
                        self.g.supprimer(self.hp)
                        self.g.supprimer(self.attaque)
                        self.g.supprimer(self.defense)
                        self.g.supprimer(self.vitesse)
                        self.g.supprimer(self.attspe)
                        self.g.supprimer(self.defspe)
                        self.g.supprimer(self.level)
                        if self.type2:
                            self.g.supprimer(self.type2)
                    self.level = self.g.afficherTexte(f"Niveau : {pokestat['Level']}",1395,750,col="white",sizefont=18)
                    self.defspe = self.g.afficherTexte(f"Def Spe : {pokestat['Sp. Def']}",1200,750,col="white",sizefont="18")
                    self.attspe = self.g.afficherTexte(f"Atk Spe : {pokestat['Sp. Atk']}",1200,710,col="white",sizefont="18")
                    self.vitesse = self.g.afficherTexte(f"Vitesse : {pokestat['Speed']}",1200,670,col="white",sizefont="18")
                    self.defense = self.g.afficherTexte(f"Defense : {pokestat['Defense']}",1000,750,col="white",sizefont="18")
                    self.attaque = self.g.afficherTexte(f"Attaque : {pokestat['Attack']}",1000,710,col="white",sizefont="18")
                    self.hp = self.g.afficherTexte(f"Hp : {pokestat['HP']}",1000,670,col="white",sizefont="18")
                    self.stat = self.g.afficherImage(805,660,f"./pokefront/{num[self.i]}.png",96,96)
                    self.type1 = self.g.afficherImage(1320,655,f"./Type/{pokestat['Type 1']}.png",150,30)
                    if pokestat['Type 2'] in type:
                        self.type2 = self.g.afficherImage(1320,695,f"./Type/{pokestat['Type 2']}.png",150,30)
                    else:
                        self.type2 = None
                    return True

        if self.stat != None:
            return True
        else:
            return False





    def afficherpokemon(self,indice):
        self.dicoimage1 = []

        espace_droit = 700  # Largeur disponible à droite de la grille
        hauteur_totale = 500
        nb_pokemon = self.nbp

        entier = int(sqrt(nb_pokemon))
        if entier < sqrt(nb_pokemon):
            entier += 1

        self.largeur_cellule = espace_droit / entier
        self.hauteur_cellule = hauteur_totale / entier

        self.taille_image = int(min(self.largeur_cellule, self.hauteur_cellule))

        cpt = 0
        for l in range(entier):
            for c in range(entier):
                if cpt < nb_pokemon and cpt - indice < len(self.pokedex_joueur1):
                    x = 810 + (c+0.1)* self.largeur_cellule
                    y = 100 + (l + 0.5) * self.hauteur_cellule
                    self.dicopoke1[(x+self.largeur_cellule/2, y+self.hauteur_cellule/2)] = self.pokedex_joueur1[cpt-indice]
                    self.dicoimage1.append(self.g.afficherImage(x, y,f"./pokefront/{self.dicopoke1[1][cpt]}.png",self.taille_image, self.taille_image))

                    cpt += 1

        return True



    def afficherpokemon2(self, indice):
        self.dicoimage2 = []
        espace_droit = 700  # Largeur disponible à droite de la grille
        hauteur_totale = 500
        nb_pokemon = self.nbp

        entier = int(sqrt(nb_pokemon))
        if entier < sqrt(nb_pokemon):
            entier += 1

        self.largeur_cellule = espace_droit / entier
        self.hauteur_cellule = hauteur_totale / entier

        self.taille_image = int(min(self.largeur_cellule, self.hauteur_cellule))

        cpt = 0
        for l in range(entier):
            for c in range(entier):
                if cpt < nb_pokemon and cpt - indice < len(self.pokedex_joueur2):
                    x = 810 + (c + 0.1) * self.largeur_cellule
                    y = 100 + (l + 0.5) * self.hauteur_cellule

                    self.dicopoke2[(x + self.largeur_cellule / 2, y + self.hauteur_cellule / 2)] = self.pokedex_joueur2[cpt-indice]
                    self.dicoimage2.append(self.g.afficherImage(x, y,
                                         f"./pokefront/{self.dicopoke2[1][cpt]}.png",
                                         self.taille_image, self.taille_image))

                    cpt += 1

        return True

    def placerpokemon(self,grande_case,petite_case,joueur):  #Associe pokemon a une case
        #pokemon = self.choixpoke(joueur)
        pokemon = self.pokemon[0]
        self.pokeplacer[(grande_case,petite_case)] = pokemon
        print("la case", (grande_case,petite_case), "est occupé par le pokemon", pokemon)

    def multiplicateur(self,pokeatt,pokedef):
        multiplicateur=1
        typeatt = pokeatt['Type 1']
        typedef1 = pokedef['Type 1']
        typedef2 = pokedef['Type 2']
        multiplicateur *= type[typeatt][typedef1]
        if pokedef['Type 2'] in type:
            multiplicateur*=type[typeatt][typedef2]
        return multiplicateur

    def esquive(self,pokstat):
        esquive = int(pokstat['Speed']/5)+1
        print(f"Pourcentage esquive : {esquive}%")
        chance = random.randint(0,100)
        print(f"Chance = {chance}")
        return 0 if chance<esquive else 1

    def combat(self, pokeatt, grande_case, petite_case, joueur):
    # Récupérer le nom du Pokémon défenseur
        pokedef = self.pokeplacer.get((grande_case, petite_case))
        if pokedef is None:
            print(f"Aucun Pokémon trouvé dans la case {grande_case}, {petite_case}.")
            return False

        if joueur == 1:
            dfj = self.joueur1_df
            dfjadv = self.joueur2_df
        else:
            dfj = self.joueur2_df
            dfjadv = self.joueur1_df
        # Extraire les statistiques des Pokémon depuis le DataFrame
        pokeattstat = dfj.loc[pokeatt]
        pokedefstat = dfjadv.loc[pokedef]

        pokeattHP = pokeattstat['HP']
        pokedefHP = pokedefstat['HP']


        multiatt = self.multiplicateur(pokeattstat,pokedefstat)
        multidef = self.multiplicateur(pokedefstat,pokeattstat)
        print(f"Multiplicateur Charizard => Mawile {multiatt}")
        print(f"Multiplicateur Mawile =>  Charizard {multidef}")
        pokeattatt = max(pokeattstat['Attack'],pokeattstat['Sp. Atk'])
        pokedefatt = max(pokedefstat['Attack'],pokedefstat['Sp. Atk'])

        if pokedefatt == pokedefstat['Attack']:
            pokeattdef = pokeattstat['Defense']
        else:
            pokeattdef = pokeattstat['Sp. Def']

        if pokeattatt == pokeattstat['Attack']:
            pokedefdef = pokedefstat['Defense']
        else:
            pokedefdef = pokedefstat['Sp. Def']

        print(pokedefatt)
        print(pokedefdef)
        print(pokeattatt)
        print(pokeattdef)
        cpttour = 0

        while pokeattHP > 0 and pokedefHP > 0:
            esquiveatt = self.esquive(pokeattstat)
            print(f"Le % d'esquive attaquant est de : {esquiveatt}")
            esquivedef = self.esquive(pokedefstat)
            print(f"Le % d'esquive def est de : {esquivedef}")
            if cpttour>30:
                pokeattHP = 0
            cpttour +=1
        # Attaque de l'attaquant
            degats = (((((50*0.4)+2)*pokeattatt*80)/pokedefdef)/50 +2)*multiatt*esquivedef
            pokedefHP -= degats
            print(f"{pokeatt} attaque {pokedef} infligeant {degats} dégâts. HP restant de {pokedef} : {max(0, pokedefHP)}")



        # Attaque du défenseur
            degats = (((((50*0.4)+2)*pokedefatt*80)/pokeattdef)/50 +2)*multidef*esquiveatt
            pokeattHP -= degats
            print(f"{pokedef} attaque {pokeatt} infligeant {degats} dégâts. HP restant de {pokeatt} : {max(0, pokeattHP)}")

        if pokedefHP <=0 and pokeattHP <=0:
            return False

        if pokedefHP <= 0:
            print(f"{pokedef} est K.O.!")
            return True

        if pokeattHP <= 0:
            print(f"{pokeatt} est K.O.!")
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