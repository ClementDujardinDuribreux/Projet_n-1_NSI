def generer_plateau(horizontal:int, vertical:int):
    """
    Cette fonction génère le plateau de jeu
    """
    dico = {}
    for i in range(vertical):
        dico[i] = []
        for y in range(horizontal):
            dico[i].append("?")
    for valeur in dico.values():
        print(valeur)
    return dico

generer_plateau(8,8)