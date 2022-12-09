from fonc_pions import*

##  ------------------------------------------------------------  ##

def case_autour(pos:tuple) -> list:
    a = 0
    b = 0
    c = 0
    d = 0
    if pos[0] == 0:
        a = 1
    if pos[0] == 8:
        b = 1
    if pos[1] == 0:
        c = 1
    if pos[1] == 8:
        d = 1
    liste_case_autour = []
    for lignes in range(pos[0] - 1 + a, pos[0] + 2 - b):
        for index in range(pos[1] - 1 + c, pos[1] + 2 - d):
            liste_case_autour.append((lignes,index))

    liste_case_autour.remove(pos)

    return liste_case_autour

##  ------------------------------------------------------------  ##

def liste_case_entre():
    pass

##  ------------------------------------------------------------  ##

def verifier_case():
    pass

##  ------------------------------------------------------------  ##

def contrainte_pions():
    pass

##  ------------------------------------------------------------  ##

def contrainte_fou():
    pass

##  ------------------------------------------------------------  ##

def contrainte_tour():
    pass

##  ------------------------------------------------------------  ##

def contrainte_cavalier():
    pass

##  ------------------------------------------------------------  ##

def contrainte_roi():
    pass

##  ------------------------------------------------------------  ##

def contraite_dame():
    pass
