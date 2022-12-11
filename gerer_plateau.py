def generer_plateau(horizontal:int, vertical:int) -> dict:
    """
    Cette fonction génère le plateau de jeu
    """

    dico = {}
    for i in range(1,vertical + 1):
        dico[i] = []
        for y in range(horizontal):
            dico[i].append("")
    return dico

##  ------------------------------------------------------------  ##

def afficher_plateau(dico:dict) -> None:
    """
    Cette fonction permet d'afficher le plateau de jeu (avec le nom des lignes et des colonnes)
    """

    print('     1    2   3   4   5   6   7   8')
    print('')
    x = 0
    lettres = 'ABCDEFGH'
    for valeurs in dico.values():
        print(lettres[x], ' ', valeurs)
        x += 1
    return None

##  ------------------------------------------------------------  ##

from fonc_pions import*

def placement_pion_depart(dico:dict) -> dict:
    """
    Cette fonction permet de placer les pions avec le placement de base au echecs
    """
    
    dico_placement_depart_J1 = {"tour1" : 'H1', "cavalier1" : 'H2', "fou1" : 'H3', "roi" : 'H4', "dame" : 'H5', "tour2": 'H8', "cavalier2": 'H7', "fou2": 'H6', "pion1": 'G1', "pion2": 'G2', "pion3": 'G3', "pion4": 'G4', "pion5": 'G5', "pion6": 'G6', "pion7": 'G7', "pion8": 'G8'}
    dico_placement_depart_J2 = {"tour1" : 'A1', "cavalier1" : 'A2', "fou1" : 'A3', "roi" : 'A4', "dame" : 'A5', "tour2": 'A8', "cavalier2": 'A7', "fou2": 'A6', "pion1": 'B1', "pion2": 'B2', "pion3": 'B3', "pion4": 'B4', "pion5": 'B5', "pion6": 'B6', "pion7": 'B7', "pion8": 'B8'}

    for pion in dico_placement_depart_J1.keys():
        placement_pion(dico, pion_en_nombre(pion, 1), pos(dico_placement_depart_J1[pion]))
    for pion in dico_placement_depart_J2.keys():
        placement_pion(dico, pion_en_nombre(pion, 2), pos(dico_placement_depart_J2[pion]))
    return dico

##  ------------------------------------------------------------  ##

