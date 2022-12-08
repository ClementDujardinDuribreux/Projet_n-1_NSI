from fonc_roi_en_vie import roi_en_vie_J1, roi_en_vie_J2
from fonc_pion_en_nombre import pions_en_nombre


def lancer(J1: str, J2: str) -> None:
    while roi_en_vie_J1() == True and roi_en_vie_J2() == True:
        pass
    

    if roi_en_vie_J1() == False:
        gagnant = J2
    else:
        gagnant = J1