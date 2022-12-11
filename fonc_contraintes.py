from fonc_pions import*

joueur_1 = {"tour1" : 1, "cavalier1" : 2, "fou1" : 3, "roi" : 4, "dame" : 5, "tour2": 6, "cavalier2": 7, "fou2":8, "pion1": 9, "pion2": 10, "pion3": 11, "pion4": 12, "pion5": 13, "pion6": 14, "pion7": 15, "pion8": 16, }
joueur_2 = {"tour1" : 100, "cavalier1" : 110, "fou1": 120, "roi" : 130, "dame" : 140, "tour2": 150, "cavalier2": 160, "fou2": 170, "pion1": 180, "pion2": 190, "pion3": 200, "pion4": 210, "pion5": 220, "pion6": 230, "pion7": 240, "pion8": 250, }

##  ------------------------------------------------------------  ##

def case_autour(pos:tuple) -> list:

    liste_case_autour = []
    liste_case_remove = []
    for lignes in range(pos[0] - 1, pos[0] + 2):
        for index in range(pos[1] - 1, pos[1] + 2):
            liste_case_autour.append((lignes,index))
    liste_case_autour.remove(pos)

    for tuples in liste_case_autour:
        if 0 in tuples or 9 in tuples:
            liste_case_remove.append(tuples)

    for tuples_remove in liste_case_remove:
        liste_case_autour.remove(tuples_remove)

    return liste_case_autour

##  ------------------------------------------------------------  ##

def liste_cases_entre():
    pass

##  ------------------------------------------------------------  ##

def verifier_case(dico_plateau:dict ,pos:tuple) -> int:
    return  dico_plateau[pos[0]][pos[1] - 1]
    
##  ------------------------------------------------------------  ##

def contraintes_pions():
    pass

##  ------------------------------------------------------------  ##

def contraintes_fou():
    pass

##  ------------------------------------------------------------  ##

def contraintes_tour():
    pass

##  ------------------------------------------------------------  ##

def contraintes_cavalier():
    pass

##  ------------------------------------------------------------  ##

def contraintes_roi(pos_ini:tuple, pos_final:tuple, joueur:int) -> tuple:
    if pos_final not in case_autour(pos_ini):
        raison = 'Tu ne peux pas bouger ton roi ici !'
        return (False, raison)

    if joueur == 1:
        if verifier_case(pos_final) in joueur_1.values():
            raison = 'Cette case est deja prise pas un de tes pions !'
            return (False, raison)
    elif joueur == 2:
        if verifier_case(pos_final) in joueur_2.values():
            raison = 'Cette case est deja prise pas un de tes pions !'
            return (False, raison)
    
    return (True, '')

##  ------------------------------------------------------------  ##

def contraintes_dame():
    pass

##  ------------------------------------------------------------  ##

def contraintes_global(pion:int, pos_ini:tuple, pos_final:tuple, joueur:int) -> bool:
    if nombre_en_pion(pion)[0] == 'roi':
        if contraintes_roi(pos_ini, pos_final, joueur)[0] == True:
            return True
        else:
            return False
    return (True, '')