from fonc_pions import*
from gerer_plateau import*

##  ----------------------- Zone TEST --------------------------  ##

def test():
    print("")
    print("")
    dico_plateau = generer_plateau(8,8)
    afficher_plateau(dico_plateau)
    print("")
    print("")
    print("")
    dico_plateau = placement_pion(dico_plateau, pions_en_nombre('Fou2',1), pos('E3'))
    afficher_plateau(dico_plateau)
    print("")
    print("")

test()

##  ------------------------------------------------------------  ##


def lancer(J1: str, J2: str) -> None:
    while roi_en_vie_J1() == True and roi_en_vie_J2() == True:
        pass
    

    if roi_en_vie_J1() == False:
        gagnant = J2
    else:
        gagnant = J1