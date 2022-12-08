from fonc_pions import*


def lancer(J1: str, J2: str) -> None:
    while roi_en_vie_J1() == True and roi_en_vie_J2() == True:
        pass
    

    if roi_en_vie_J1() == False:
        gagnant = J2
    else:
        gagnant = J1