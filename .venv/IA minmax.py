from tkiteasy1 import *
import random
dimMorpion = 800

class Morpion :

    def __init__(self):
        self.g = ouvrirFenetre(1532,800)
        self.modeJeu = 1
        self.nbp = 64
        self.menu()


    def menu(self):
        menu = self.g.afficherImage(0, 0, "./MenuPokemon.png")
        testjeusolo = self.g.dessinerRectangle(950,645,470,55,"white")
        #settings = self.g.afficherImage(1300, 700, "./Settings.png",150,75)
        while True:
            cliquesouris = self.g.attendreClic()
            if 950 < cliquesouris.x < 1420 and 585 < cliquesouris.y < 635:
                self.g.supprimerTout()
                if self.modeJeu == 1:
                    self.cooking.JeuPoke(self.nbp)
                else:
                    self.Jeu()

            if 950 < cliquesouris.x<1420 and 710<cliquesouris.y<765:
                self.g.supprimerTout()
                self.settings()

    def choixmode(self):
        if self.modeJeu == 1:
            texte = "Avec Pokémon"
        else:
            texte = "Sans Pokémon"
        return texte

    def settings(self):
        texte = self.choixmode()
        settings = self.g.afficherImage(0, 0, "./MenuSettings.png")
        choimode = self.g.afficherTexte(texte,770,310,col="darkblue",sizefont=25)
        nombrepokemon = self.g.afficherTexte(f"Nombre de Pokémon : {self.nbp}",770,410,col="beige",sizefont=25)
        self.g.dessinerRectangle(1000,295,35,35,col="darkblue")
        self.g.dessinerRectangle(505,295,35,35,col="darkblue")
        self.g.dessinerRectangle(505,395,35,35,col="beige")
        self.g.dessinerRectangle(1000,395,35,35,col="beige")
        while True:

            cliquesouris = self.g.attendreClic()
            if 14 < cliquesouris.x<75 and 629<cliquesouris.y<689:
                self.g.supprimerTout()
                self.menu()

            if 1000<cliquesouris.x<1035 and 295<cliquesouris.y<330:
                self.modeJeu = 3-self.modeJeu
                texte = self.choixmode()
                self.g.changerTexte(choimode,texte)

            if 505<cliquesouris.x<540 and 295<cliquesouris.y<330:
                self.modeJeu = 3-self.modeJeu
                texte = self.choixmode()
                self.g.changerTexte(choimode,texte)

            if 505<cliquesouris.x<540 and 395<cliquesouris.y<430 and self.nbp>42:
                self.nbp -= 1
                self.g.changerTexte(nombrepokemon,f"Nombre de Pokémon : {self.nbp}")

            if 1000<cliquesouris.x<1035 and 395<cliquesouris.y<430 and self.nbp<721:
                self.nbp+=1
                self.g.changerTexte(nombrepokemon,f"Nombre de Pokémon : {self.nbp}")


    def Jeu(self):
        self.g.dessinerDisque(1345,74,26,"white")
        self.g.afficherImage(1300,30,"./Home.png",90,90)
        self.joueur = self.g.afficherImage(1000,150,"./Joueur 1.png")
        self.j = self.g.afficherImage(1532-435,325,"./Tortank.png")
        #j2 = self.g.afficherImage(dimMorpion+5,325,"./dracaufeu.png")
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
        Fintour = False

        while True:  # Boucle principale du jeu
            if joueur == 1:  # Tour du joueur 1
                self.joueur = self.g.afficherImage(1000, 150, "./Joueur 1.png")
                while not Fintour:  # Boucle jusqu'à ce que le tour soit terminé
                    clic = self.g.attendreClic()
                    self.win = {}

                    if (((clic.x - 1345)) ** 2 + ((clic.y - 74)) ** 2) ** 0.5 <= 26:
                        self.g.supprimerTout()
                        self.menu()

                    if 0 < clic.x < dimMorpion and 0 < clic.y < dimMorpion:
                        grande_case, petite_case = self.determinerCase(clic.x, clic.y)

                        if grande_case in self.ban:
                            print(
                                f"Vous devez jouer dans une autre grande case. La grande case {grande_case} est bannie.")
                            continue

                        # Effacement de l'encadrement si le joueur souhaite changer la case
                        if grande_case == cliquable and encadre is not None:
                            if self.lists[grande_case][petite_case - 1] == 0:
                                self.g.supprimer(encadre)
                                encadre = None

                        # Vérifier que le joueur joue dans la bonne grande case
                        if cliquable is not None and grande_case != cliquable:
                            print(f"Vous devez jouer dans la grande case {cliquable}.")
                            continue

                        # Remplir la grille et gérer les règles
                        if self.RemplirGrille(grande_case, petite_case, joueur):
                            self.Regle(grande_case, joueur)
                            cliquable = self.Transfert(grande_case, petite_case)
                            joueur = 3 - joueur  # Passer à l'autre joueur
                            self.alterner(joueur)

                            if cliquable is not None:
                                xc, yc = self.dessinerEncadrement(cliquable)
                                encadre = self.g.dessinerRectangle(xc, yc, dimMorpion / 3, dimMorpion / 3, col="purple")
                                self.g.placerAuDessous(encadre)

                            Fintour = True  # Fin du tour pour le joueur 1

            if joueur == 2:  # Tour du joueur 2 (ou IA)
                self.joueur = self.g.afficherImage(1000, 150, "./Joueur 2.png")
                # Implémenter la logique pour le joueur 2 ou l'IA ici
                self.win = {}
                grille = []
                for i in range(1,10):
                    sous_grille = self.lists[i]
                    grille.append(sous_grille)
                print(grille)
                print("cliquable de base", cliquable)
                score, case = self.minimax( grille, 3, True, cliquable)
                print("case",case)
                grande_case, petite_case = case[0], case[1]
                if grande_case == cliquable and encadre is not None:
                    if self.lists[grande_case][petite_case - 1] == 0:
                        self.g.supprimer(encadre)
                        encadre = None
                print(Gcase,Pcase)
                self.RemplirGrille(Gcase, Pcase, joueur)
                cliquable = self.Transfert(Gcase, Pcase)
                joueur = 1  # Passer au joueur 1
                Fintour = True  # Fin du tour pour le joueur 2
                if cliquable is not None:
                    xc, yc = self.dessinerEncadrement(cliquable)
                    encadre = self.g.dessinerRectangle(xc, yc, dimMorpion / 3, dimMorpion / 3, col="purple")
                    self.g.placerAuDessous(encadre)
            # Réinitialisation de Fintour pour le prochain tour
            if Fintour:
                Fintour = False

    def alterner(self,joueur):
        if joueur == 1:
            self.g.supprimer(self.j)
            self.g.supprimer(self.joueur)
            self.j = self.g.afficherImage(1532-435,325,"./Tortank.png")
            self.joueur = self.g.afficherImage(1000,150,"./Joueur 1.png")
        else:
            self.g.supprimer(self.joueur)
            self.g.supprimer(self.j)
            self.j = self.g.afficherImage(dimMorpion+5,325,"./dracaufeu.png")
            self.joueur = self.g.afficherImage(1000,150,"./Joueur 2.png")

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

    def Finale(self,joueur):
        if ((self.MegaGrille[0] == self.MegaGrille[1] == self.MegaGrille[2]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[3] == self.MegaGrille[4] == self.MegaGrille[5]) and self.MegaGrille[3]!=0 ) or ((self.MegaGrille[6] == self.MegaGrille[7] == self.MegaGrille[8]) and self.MegaGrille[6]!=0 ) or ((self.MegaGrille[0] == self.MegaGrille[4] == self.MegaGrille[8]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[0] == self.MegaGrille[3] == self.MegaGrille[6]) and self.MegaGrille[0]!=0 ) or ((self.MegaGrille[1] == self.MegaGrille[4] == self.MegaGrille[7]) and self.MegaGrille[1]!=0) or ((self.MegaGrille[2] == self.MegaGrille[5] == self.MegaGrille[8]) and self.MegaGrille[2]!=0) or ((self.MegaGrille[6] == self.MegaGrille[4] == self.MegaGrille[2]) and self.MegaGrille[6]!=0) :

            self.g.supprimerTout()
            self.ecranvictoire(joueur)
            self.g.attendreClic()
            self.g.supprimerTout()
            self.menu()

        if all(i!=0 for i in self.MegaGrille):
            self.ecrangalite()
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

    def RemplirGrille(self,grande_case, petite_case,joueur):
        print(joueur)
        J = None
        if joueur % 2 == 0:
            J = 2
        else :
            J=1        #Verification
        print(grande_case,petite_case)
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

    def gameover(self, grille):
        print("grille:", grille)

        # Vérification des conditions de victoire
        if ((grille[0] == grille[1] == grille[2] and grille[0] != 0) or
                (grille[3] == grille[4] == grille[5] and grille[3] != 0) or
                (grille[6] == grille[7] == grille[8] and grille[6] != 0) or
                (grille[0] == grille[4] == grille[8] and grille[0] != 0) or
                (grille[2] == grille[4] == grille[6] and grille[2] != 0) or
                (grille[0] == grille[3] == grille[6] and grille[0] != 0) or
                (grille[1] == grille[4] == grille[7] and grille[1] != 0) or
                (grille[2] == grille[5] == grille[8] and grille[2] != 0)):
            print("Victoire détectée!")
            return True

        # Vérification si la grille est pleine (égalité ou fin du jeu)
        if all(cell != 0 for cell in grille):
            print("Grille pleine, égalité.")
            return True

        # Le jeu continue s'il y a encore des cases vides
        print("Le jeu continue.")
        return False

    def applymove(self, grille, move, joueur): #fonction qui actualise la grille en fonction du mouvement fait
        grande_case, petite_case = move
        print(grille)
        nouv_grille = [row[:] for row in grille]  # On fait une copie de chaque sous-grille
        nouv_grille[grande_case][petite_case] = joueur  # On place la marque du joueur dans la case correspondante
        return nouv_grille

    def minimax(self, grille, depth, is_maximizing, cliquable):
        """
        Fonction Minimax avec gestion de profondeur.
        Args:
        - board: état actuel de la grille.
        - depth: profondeur actuelle dans l'arbre.
        - is_maximizing: booléen indiquant si c'est au tour du joueur maximisant (IA).

        Retourne:
        - best_value: la valeur estimée du meilleur coup.
        - best_move: le meilleur coup trouvé.
        """
        # Vérifier si le jeu est terminé ou si la profondeur limite est atteinte
        if depth == 0:
            print("entree 2")
            return self.evaluer(grille, joueur=2), None  # Évaluer l'état de la grille
        print("cliquabel1",cliquable)
        cases = self.actions(grille, cliquable)  # Obtenir tous les coups possibles
        print("caseses :", cases)
        if is_maximizing:  # Tour de l'IA
            best_value = float('-inf') #-infini
            best_move = None
            for move in cases:
                nouvelle_grille = self.applymove(grille, move, 2)  # Simuler coup pour joueur 2, creer fonction qui renvoie une nouvelle grille
                grande_case, petite_case= move
                if petite_case not in self.ban :
                    nouveau_cliquable = petite_case
                value, _ = self.minimax(nouvelle_grille, depth - 1, is_maximizing=False, cliquable=nouveau_cliquable)  # Réduire la profondeur
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

        else:  # Tour du joueur minimisant (joueur 1)
            best_value = float('inf')
            best_move = None
            for move in cases:
                nouvelle_grille = self.applymove(grille, move, 1)  # Simuler coup pour joueur 1
                move = grande_case, petite_case
                if petite_case not in self.ban:
                    nouveau_cliquable = petite_case
                value, _ = self.minimax(nouvelle_grille, depth - 1, is_maximizing=True, cliquable= nouveau_cliquable)  # Réduire la profondeur
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

    def actions(self, grille, cliquable):
        coups_possibles = []

        if cliquable is not None and cliquable != 0:
  # Si une sous-grille spécifique est ciblée
            print("cliquable", cliquable, self.lists)
            liste_cases = self.lists[cliquable]
            petites_cases = [i for i in range(9) if liste_cases[i] == 0]  # Récupère les cases vides
            if petites_cases:  # Si des cases sont disponibles dans cette sous-grille
                for case in petites_cases:
                    coups_possibles.append((cliquable-1, case))  # On ajoute l'index de la case sans +1
            else:
                return coups_possibles  # Si aucune case n'est disponible, retourner la liste vide

        else:  # Si aucune sous-grille spécifique, vérifier toutes les sous-grilles
            grande_case = []
            for i in range(1, 10):  # On vérifie les sous-grilles disponibles (de 1 à 9)
                if i not in self.ban:  # Si la sous-grille n'est pas bannie
                    grande_case.append(i)

            if not grande_case:  # Si aucune sous-grille n'est disponible
                return None

            for case_grande in grande_case:  # Parcours des grandes cases
                liste_cases = self.lists[case_grande - 1]  # Accède à la sous-grille correcte
                petites_cases = [i for i in range(9) if
                                 liste_cases[i] == 0]  # Récupère les cases vides dans cette grande case
                for case in petites_cases:  # Pour chaque petite case vide
                    coups_possibles.append((case_grande-1 , case))  # On ajoute à coups_possibles sans +1 ou -1

        return coups_possibles

    def evaluer(self, grille, joueur):    #evaluation score pour trouver la meilleure case
        """
        Évalue l'état actuel de la grille et retourne un score pour le joueur donné.
        Args:
        - grille: l'état actuel de la grille.
        - joueur: le joueur pour lequel on calcule le score (1 ou 2).
        Returns:
        - score: une valeur numérique représentant l'évaluation de la grille.
        """
        score = 0
        adversaire = 1 if joueur == 2 else 2

        # 1. Évaluation des petites grilles
        for i, sous_grille in enumerate(grille):  # Parcourir chaque petite grille
            for ligne in self.get_lignes(sous_grille):  # Récupérer les lignes, colonnes et diagonales
                joueur_count = ligne.count(joueur)
                adversaire_count = ligne.count(adversaire)

                if joueur_count > 0 and adversaire_count == 0:  # Ligne favorable
                    score += 10 * joueur_count  # Bonus pour alignements possibles
                elif adversaire_count > 0 and joueur_count == 0:  # Ligne défavorable
                    score -= 8 * adversaire_count  # Pénalité pour alignements adverses

            # Bonus si la petite grille est gagnée
            if self.gameover(sous_grille) and any(case == joueur for case in sous_grille):
                score += 50  # Bonus significatif pour contrôle d'une grande case
            elif self.gameover(sous_grille) and any(case == adversaire for case in sous_grille):
                score -= 50  # Malus significatif si l'adversaire contrôle une grande case

        # 2. Évaluation de la grande grille (alignements dans MegaGrille)
        mega_grille = [self.get_winner(sous_grille) for sous_grille in grille]  # Récupérer l'état des grandes cases
        for ligne in self.get_lignes(mega_grille):  # Lignes, colonnes et diagonales
            joueur_count = ligne.count(joueur)
            adversaire_count = ligne.count(adversaire)

            if joueur_count > 0 and adversaire_count == 0:  # Alignement potentiel
                score += 30 * joueur_count  # Priorité plus élevée dans la grande grille
            elif adversaire_count > 0 and joueur_count == 0:  # Alignement potentiel de l'adversaire
                score -= 25 * adversaire_count

        # 3. Opportunités futures (restriction des choix)
        # Réduire les options adverses est avantageux

        # 4. Position centrale
        for i, sous_grille in enumerate(grille):
            if sous_grille[4] == joueur:  # Contrôle du centre
                score += 15
            elif sous_grille[4] == adversaire:
                score -= 15

        return score

    def get_lignes(self, sous_grille):
        """
        Retourne toutes les lignes, colonnes et diagonales d'une sous-grille.
        """
        return [
            sous_grille[0:3], sous_grille[3:6], sous_grille[6:9],  # Lignes
            sous_grille[0:9:3], sous_grille[1:9:3], sous_grille[2:9:3],  # Colonnes
            [sous_grille[0], sous_grille[4], sous_grille[8]],  # Diagonale principale
            [sous_grille[2], sous_grille[4], sous_grille[6]]  # Diagonale secondaire
        ]

    def get_winner(self,grille):
        """
        Vérifie si un joueur a gagné dans une grille 3x3.
        Args:
        - grille : liste de 9 éléments représentant une grille 3x3.

        Returns:
        - 1 si le joueur 1 a gagné,
        - 2 si le joueur 2 a gagné,
        - 0 si aucune victoire n'est détectée.
        """
        lignes = [
            grille[0:3],  # Ligne 1
            grille[3:6],  # Ligne 2
            grille[6:9],  # Ligne 3
            grille[0:9:3],  # Colonne 1
            grille[1:9:3],  # Colonne 2
            grille[2:9:3],  # Colonne 3
            [grille[0], grille[4], grille[8]],  # Diagonale principale
            [grille[2], grille[4], grille[6]]  # Diagonale secondaire
        ]

        for ligne in lignes:
            if ligne.count(1) == 3:  # Si toutes les cases appartiennent au joueur 1
                return 1
            elif ligne.count(2) == 3:  # Si toutes les cases appartiennent au joueur 2
                return 2

        return 0

    def is_restricted(self, cliquable):
        """
        Vérifie si une restriction est appliquée et si elle est toujours valide.

        Args:
        - cliquable : indice de la sous-grille dans laquelle le joueur doit jouer (peut être None si aucune restriction).

        Returns:
        - True si le joueur est effectivement restreint à une sous-grille valide.
        - False si aucune restriction ou si la restriction n'est plus applicable.
        """
        if cliquable is None:  # Aucune restriction
            return False

        # Vérifier si la sous-grille est bannie ou pleine
        if cliquable in self.ban:
            return False

        # Vérifier si des cases sont encore disponibles dans la sous-grille
        petite_grille = self.lists[cliquable]  # Accéder à la sous-grille correspondante
        if any(case == 0 for case in petite_grille):  # Si au moins une case est libre
            return True

        # Sinon, la restriction n'est plus valable
        return False


Morpion()