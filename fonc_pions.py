
def pions_en_nombre(pion: str, joueur : int) -> int:
    """
    Cette fonction permet de return le nombre associé au piont
    """

    j1 = {"tour1" : 1, "cavalier1" : 2, "fou1" : 3, "roi" : 4, "dame" : 5, "tour2": 6, "cavalier2": 7, "fou2":8, "pion1": 9, "pion2": 10, "pion3": 11, "pion4": 12, "pion5": 13, "pion6": 14, "pion7": 15, "pion8": 16, }
    j2 = {"tour1" : 100, "cavalier1" : 110, "fou1": 120, "roi" : 130, "dame" : 140, "tour2": 150, "cavalier2": 160, "fou2": 170, "pion1": 180, "pion2": 190, "pion3": 200, "pion4": 210, "pion5": 220, "pion6": 230, "pion7": 240, "pion8": 250, }

    if joueur == 1:
        return j1[pion.lower()]
    else:
        return j2[pion.lower()]

##  ------------------------------------------------------------  ##

def pos(x_y:str) -> tuple:
    """
    Cette fonction permet de return la position en python (par rapport aux listes) en donnant la position sur le plateau de jeu (ex : 'A1')
    """

    lettres = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H': 8}
    return (lettres[x_y[0].upper()],int(x_y[1]))

##  ------------------------------------------------------------  ##

def placement_pion(dico_plateau:dict, pion:int, pos:tuple) -> dict:
    """
    Cette fonction permet de placer un pion sur le plateau
    """
    
    del dico_plateau[pos[0]][pos[1] - 1]
    dico_plateau[pos[0]].insert(pos[1] - 1,pion)
    return dico_plateau

##  ------------------------------------------------------------  ##

def roi_en_vie_J1():
    pass

##  ------------------------------------------------------------  ##

def roi_en_vie_J2():
    pass

##  ------------------------------------------------------------  ##

