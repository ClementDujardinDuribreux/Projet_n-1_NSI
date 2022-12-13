from fonc_pions import*
from gerer_plateau import*
from fonc_contraintes import*


##  ----------------------- Zone TEST --------------------------  ##

def test():
    pass

##  ------------------------------------------------------------  ##


def lancer(J1: str, J2: str) -> None:
    """
    Cette fonction permet de lancer le jeu d'échec
    """

    ficher = open('historique_parties.txt', 'a')
    tour = 1
    dico_plateau = placement_pion_depart(generer_plateau(8,8))

    print("")
    print("")
    afficher_plateau(dico_plateau)

    while roi_en_vie_J1(dico_plateau) == True and roi_en_vie_J2(dico_plateau) == True:
        if tour % 2 != 0:
            joueur = 1
            player_name = J1
        else:
            joueur = 2
            player_name = J2
        
        print("")
        print("")
        print("C'est au tour du Joueur", joueur, ':', player_name)

        pion_a_bouger = pion_en_nombre(input("Quel piont veux tu bouger ? : "), joueur)
        pos_final = pos(input('Où ? : '))

        while contraintes_global(dico_plateau, pion_a_bouger, pos_pion(dico_plateau,pion_a_bouger), pos_final, joueur, tour)[0] != True:
            raison = contraintes_global(dico_plateau, pion_a_bouger, pos_pion(dico_plateau,pion_a_bouger), pos_final, joueur, tour)[1]
            print(raison)
            pos_final = pos(input('Où ? : '))

        dico_plateau = deplacer_pion(dico_plateau, pion_a_bouger, pos_final)
        afficher_plateau(dico_plateau)

        tour += 1
    
    tour -= 1
    if roi_en_vie_J1(dico_plateau) == False:
        gagnant = J2
    else:
        gagnant = J1

    print("")
    print("ECHEC ET MAT !")
    print("")
    print('Bravo le/la gagnant(e) est :', gagnant)
    print("")
    print("")

    ficher.write(' - ' + J1 + '\n' + ' - ' + J2 + '\n' + 'Le gagnant de cette partie est : ' + gagnant + '\n' + '\n')
    ficher.close()

    return None

##lancer('Florent', 'Clement')