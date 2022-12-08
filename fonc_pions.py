def pions_en_nombre(pion: str, joueur : int) -> None:
    j1 = {"tour1" : 1, "cavalier1" : 2, "fou1" : 3, "roi" : 4, "dame" : 5, "tour2": 6, "cavalier2": 7, "fou2":8, "pion1": 9, "pion2": 10, "pion3": 11, "pion4": 12, "pion5": 13, "pion6": 14, "pion7": 15, "pion8": 16, }
    j2 = {"tour1" : 100, "cavalier1" : 110, "fou1": 120, "roi" : 130, "dame" : 140, "tour2": 150, "cavalier2": 160, "fou2": 170, "pion1": 180, "pion2": 190, "pion3": 200, "pion4": 210, "pion5": 220, "pion6": 230, "pion7": 240, "pion8": 250, }

    if joueur == 1:
        return j1[pion.lower()]
    else:
        return j2[pion.lower()]

def roi_en_vie_J1():
    pass


def roi_en_vie_J2():
    pass