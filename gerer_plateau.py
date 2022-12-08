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

    print('#    1    2   3   4   5   6   7   8   #')
    print('')
    x = 0
    lettres = 'ABCDEFGH'
    for valeurs in dico.values():
        print(lettres[x], ' ', valeurs)
        x += 1
    return None
