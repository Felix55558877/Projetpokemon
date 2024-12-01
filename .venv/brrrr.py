from tkiteasy1 import *
from cooking import Pokemon
from playsound import playsound
import threading
import random

dimMorpion = 800

class Morpion :

    def __init__(self):
        #threading.Thread(target=self.play_music_loop, daemon=True).start()
        self.g = ouvrirFenetre(1532,800)
        self.modeJeu = 0
        self.cooking = Pokemon(self,self.g)
        self.nbp = 64
        self.menu()

    def play_music_loop(self):
        # Boucle de lecture infinie avec playsound
        while True:
            playsound("./theme.mp3")


    def menu(self):
        menu = self.g.afficherImage(0, 0, "./MenuPokemon.png")
        #testjeusolo = self.g.dessinerRectangle(950,645,470,55,"white")
        #settings = self.g.afficherImage(1300, 700, "./Settings.png",150,75)
        while True:
            cliquesouris = self.g.attendreClic()
            if 950 < cliquesouris.x < 1420 and 585 < cliquesouris.y < 635:
                self.g.supprimerTout()
                if self.modeJeu == 1:
                    self.cooking.JeuPoke(self.nbp)
                else:
                    self.Jeuautiste()

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


    def Jeuautiste(self):
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

        while True:

            if joueur == 1:
                clic = self.g.attendreClic()
            elif joueur != 1:
                if cliquable:
                    _, petite_case = self.CalculerMeilleurCoup(cliquable, depth=1, joueur=joueur)
                    clic.x, clic.y = self.determinerCoordonnees(cliquable, petite_case)


            self.win = {}

            if (((clic.x - 1345)) ** 2 + ((clic.y - 74)) ** 2) ** 0.5 <= 26:
                self.g.supprimerTout()
                self.menu()

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
                    self.alterner(joueur)


                    if cliquable is not None :
                        xc,yc = self.dessinerEncadrement(cliquable)
                        encadre = self.g.dessinerRectangle(xc,yc,dimMorpion/3,dimMorpion/3,col="purple")
                        self.g.placerAuDessous(encadre)


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
        if joueur == 1 :
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
        if self.lists[grande_case][petite_case-1] == 0:
            self.lists[grande_case][petite_case-1] = joueur
            self.Affichage(grande_case,petite_case, joueur)
            return True
        else:
            print(f"Case {petite_case} dans la grande case {grande_case} déjà occupée !")
            raise SystemExit


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

    def determinerCoordonnees(self, grande_case, petite_case):
        """
        Convertit une grande case et une petite case en coordonnées x, y.

        Paramètres:
            grande_case (int): L'indice de la grande case.
            petite_case (int): L'indice de la petite case.

        Retourne:
            tuple: (x, y) - Coordonnées correspondant au clic.
        """
        taille_grande_case = dimMorpion / 3
        taille_petite_case = taille_grande_case / 3

        colonne_grande = (grande_case - 1) % 3
        ligne_grande = (grande_case - 1) // 3
        colonne_petite = (petite_case - 1) % 3
        ligne_petite = (petite_case - 1) // 3

        x = colonne_grande * taille_grande_case + colonne_petite * taille_petite_case + taille_petite_case / 2
        y = ligne_grande * taille_grande_case + ligne_petite * taille_petite_case + taille_petite_case / 2
        print(self.determinerCase( x, y))
        return x, y

    def Minimax(self, grande_case, depth, is_maximizing, alpha, beta, joueur):
        """
        Algorithme Minimax pour calculer le meilleur coup en tenant compte des cases déjà occupées et des cases bannies.

        Paramètres:
            grande_case (int): L'indice de la grande case en cours.
            depth (int): Profondeur actuelle de l'algorithme.
            is_maximizing (bool): Si le joueur maximise ou minimise le score.
            alpha (float): Valeur alpha pour l'élagage alpha-bêta.
            beta (float): Valeur bêta pour l'élagage alpha-bêta.
            joueur (int): Joueur actuel (1 ou 2).

        Retourne:
            tuple: (score, grande_case, petite_case) - Le score et les coordonnées du meilleur coup.
        """


        # Vérifier si la profondeur est atteinte ou si l'état est terminal
        if depth == 0 or grande_case in self.win or all(cell != 0 for cell in self.lists[grande_case]):
            return (
                self.EvaluerGrille(grande_case, joueur) + self.EvaluerMegaGrille(joueur),
                grande_case,
                None
            )


        # Initialiser les variables de score et de meilleur coup
        meilleur_coup = (None, None)
        coups_possibles = []

        # Trouver les coups valides dans la grande case
        for petite_case in range(1, 10):
            # Vérifiez que la petite case est vide et pas bannie
            if (self.lists[grande_case][petite_case - 1] == 0) or\
                    ((self.lists[grande_case][petite_case - 1] == 0) and
                     (grande_case not in self.ban or petite_case not in self.ban[grande_case])):
                coups_possibles.append(petite_case)
        print(coups_possibles)


        # Si aucune petite case valide n'est trouvée, retourner un score de 0 et None
        if not coups_possibles:
            return 0, grande_case, None

        if is_maximizing:
            max_eval = float('-inf')
            for petite_case in coups_possibles:
                # Simuler le coup
                self.lists[grande_case][petite_case - 1] = joueur
                eval_score, _, _ = self.Minimax(grande_case, depth - 1, False, alpha, beta, 3 - joueur)
                self.lists[grande_case][petite_case - 1] = 0  # Annuler le coup

                if eval_score > max_eval:
                    max_eval = eval_score
                    meilleur_coup = (grande_case, petite_case)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            print(meilleur_coup)
            return max_eval, meilleur_coup[0], meilleur_coup[1]

        else:
            min_eval = float('inf')
            for petite_case in coups_possibles:
                # Simuler le coup
                self.lists[grande_case][petite_case - 1] = joueur
                eval_score, _, _ = self.Minimax(grande_case, depth - 1, True, alpha, beta, 3 - joueur)
                self.lists[grande_case][petite_case - 1] = 0  # Annuler le coup

                if eval_score < min_eval:
                    min_eval = eval_score
                    meilleur_coup = (grande_case, petite_case)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            print(meilleur_coup)
            return min_eval, meilleur_coup[0], meilleur_coup[1]

    def CalculerMeilleurCoup(self, grande_case, depth, joueur):
        """
        Calcule le meilleur coup pour un joueur donné à l'aide de l'algorithme Minimax.

        Paramètres:
            grande_case (int): La grande case où jouer.
            depth (int): Profondeur de recherche pour l'algorithme Minimax.
            joueur (int): Joueur actuel (1 ou 2).

        Retourne:
            tuple: (grande_case, petite_case) - Le coup optimal.
        """
        _, grande_case, petite_case = self.Minimax(grande_case, depth, True, float('-inf'), float('inf'), joueur)
        return grande_case, petite_case

    def EvaluerGrille(self, grande_case, joueur):
        """
        Évalue une grande case pour déterminer un avantage stratégique.

        Paramètres:
            grande_case (int): L'indice de la grande case.
            joueur (int): Le joueur pour lequel évaluer la grille (1 ou 2).

        Retourne:
            int: Score de la grande case.
        """
        liste = self.lists[grande_case]
        adversaire = 3 - joueur

        # Scores de base
        score = 0
        lignes = [
            (liste[0], liste[1], liste[2]),
            (liste[3], liste[4], liste[5]),
            (liste[6], liste[7], liste[8]),
            (liste[0], liste[3], liste[6]),
            (liste[1], liste[4], liste[7]),
            (liste[2], liste[5], liste[8]),
            (liste[0], liste[4], liste[8]),
            (liste[2], liste[4], liste[6])
        ]

        for ligne in lignes:
            if ligne.count(joueur) == 3:
                score += 1000  # Alignement gagnant
            elif ligne.count(joueur) == 2 and ligne.count(0) == 1:
                score += 50  # Menace de victoire
            elif ligne.count(joueur) == 1 and ligne.count(0) == 2:
                score += 10  # Opportunité stratégique

            if ligne.count(adversaire) == 3:
                score -= 1000  # Alignement perdant
            elif ligne.count(adversaire) == 2 and ligne.count(0) == 1:
                score -= 50  # Menace défensive
            elif ligne.count(adversaire) == 1 and ligne.count(0) == 2:
                score -= 10  # Défense stratégique

        # Bonus pour le contrôle central
        if grande_case == 5:
            score += 20 if joueur == joueur else -20

        return score

    def EvaluerMegaGrille(self, joueur):
        """
        Évalue la méta-grille pour déterminer un avantage stratégique global.

        Paramètres:
            joueur (int): Joueur pour lequel évaluer la méta-grille.

        Retourne:
            int: Score de la méta-grille.
        """
        adversaire = 3 - joueur
        score = 0
        lignes = [
            (self.MegaGrille[0], self.MegaGrille[1], self.MegaGrille[2]),
            (self.MegaGrille[3], self.MegaGrille[4], self.MegaGrille[5]),
            (self.MegaGrille[6], self.MegaGrille[7], self.MegaGrille[8]),
            (self.MegaGrille[0], self.MegaGrille[3], self.MegaGrille[6]),
            (self.MegaGrille[1], self.MegaGrille[4], self.MegaGrille[7]),
            (self.MegaGrille[2], self.MegaGrille[5], self.MegaGrille[8]),
            (self.MegaGrille[0], self.MegaGrille[4], self.MegaGrille[8]),
            (self.MegaGrille[2], self.MegaGrille[4], self.MegaGrille[6]),
        ]

        for ligne in lignes:
            if ligne.count(joueur) == 3:
                score += 5000
            elif ligne.count(joueur) == 2 and ligne.count(0) == 1:
                score += 100
            elif ligne.count(joueur) == 1 and ligne.count(0) == 2:
                score += 20

            if ligne.count(adversaire) == 3:
                score -= 5000
            elif ligne.count(adversaire) == 2 and ligne.count(0) == 1:
                score -= 100
            elif ligne.count(adversaire) == 1 and ligne.count(0) == 2:
                score -= 20

        return score







Morpion()