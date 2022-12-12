def pion_en_nombre(pion: str, joueur : int) -> int:
    """
    Cette fonction permet de return le nombre associé au piont
    """

    j1 = {"tour1" : 1, "cavalier1" : 2, "fou1" : 3, "roi" : 4, "dame" : 5, "tour2": 6, "cavalier2": 7, "fou2":8, "pion1": 9, "pion2": 10, "pion3": 11, "pion4": 12, "pion5": 13, "pion6": 14, "pion7": 15, "pion8": 16}
    j2 = {"tour1" : 100, "cavalier1" : 110, "fou1": 120, "dame" : 130, "roi" : 140, "tour2": 150, "cavalier2": 160, "fou2": 170, "pion1": 180, "pion2": 190, "pion3": 200, "pion4": 210, "pion5": 220, "pion6": 230, "pion7": 240, "pion8": 250}
    
    if joueur == 1:
        if pion.lower() not in j1.keys():
            return pion_en_nombre(input('Quel piont veux tu bouger ? : '), 1)
        return j1[pion.lower()]
    elif joueur == 2:
        if pion.lower() not in j2.keys():
            return pion_en_nombre(input('Quel piont veux tu bouger ? : '), 2)
        return j2[pion.lower()]

    
def nombre_en_pion(nombre:int) -> tuple:
    j1 = {1 : "tour1", 2 : "cavalier1", 3 : "fou1", 4 : "roi", 5 : "dame", 6 : "tour2", 7 : "cavalier2", 8 : "fou2", 9 : "pion1", 10 : "pion2", 11 : "pion3", 12 : "pion4", 13 : "pion5", 14 : "pion6", 15 : "pion7", 16 : "pion8"}
    j2 = {100 : "tour1", 110 : "cavalier1", 120 : "fou1", 130 : "dame", 140 : "roi", 150 : "tour2", 160 : "cavalier2", 170 : "fou2", 180 : "pion1", 190 : "pion2", 200 : "pion3", 210 : "pion4", 220 : "pion5", 230 : "pion6", 240 : "pion7", 250 : "pion8"}

    if nombre in j1.keys():
        return (j1[nombre], 1)
    elif nombre in j2.keys():
        return (j2[nombre], 2)

##  ------------------------------------------------------------  ##

def pos(x_y:str) -> tuple:
    """
    Cette fonction permet de return la position en python (par rapport aux listes) en donnant la position sur le plateau de jeu (ex : 'A1')
    """

    lettres = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H': 8}

    if x_y[0].upper() not in lettres.keys() or int(x_y[1]) not in range(1,9):
        return pos(input('Où ? : '))

    return (lettres[x_y[0].upper()],int(x_y[1]))

##  ------------------------------------------------------------  ##

def placement_pion(dico_plateau:dict, pion:int, pos:tuple) -> dict:
    """
    Cette fonction permet de placer un pion sur le plateau
    """
    
    del dico_plateau[pos[0]][pos[1] - 1]
    dico_plateau[pos[0]].insert(pos[1] - 1,pion)
    return dico_plateau


def deplacer_pion(dico_plateau:dict, pion:int, pos_de_deplacement:tuple) -> dict:
    """
    Cette fonction permet de deplacer un pion d'un case a une autre
    """
    
    placement_pion(dico_plateau, '', pos_pion(dico_plateau,pion))
    placement_pion(dico_plateau, pion, pos_de_deplacement)
    return dico_plateau

##  ------------------------------------------------------------  ##

def roi_en_vie_J1(dico_plateau:dict) -> bool:
    """
    Cette fonction permet de return si le roi du joueur 1 est pris ou non
    """

    for listes in dico_plateau.values():
        if 4 in listes:
            return True
    return False

##  ------------------------------------------------------------  ##

def roi_en_vie_J2(dico_plateau:dict) -> bool:
    """
    Cette fonction permet de return si le roi du joueur 2 est pris ou non
    """

    for listes in dico_plateau.values():
        if 130 in listes:
            return True
    return False

##  ------------------------------------------------------------  ##

def pos_pion(dico_plateau:dict, pion:int) -> tuple:
    for cle in dico_plateau.keys():
        if pion in dico_plateau[cle]:
            pos_ini = (cle,dico_plateau[cle].index(pion) + 1)
    return pos_ini