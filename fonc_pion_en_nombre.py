def pions_en_nombre(pion: str, joueur : int) -> None:
    j1={"tour1" : 1, "cavalier1" : 2, "fou1" : 3, "roi" : 4, "dame" : 5, "tour2": 6, "cavalier2": 7, "fou2":8}
    j2={"tour1" : 10, "cavalier1" : 20, "fou1": 30, "roi" : 40, "dame" : 50, "tour2": 60, "cavalier2": 70, "fou2": 80}

    if joueur == 1:
        return j1[pion.lower()]
    else:
        return j2[pion.lower()]
print(pions_en_nombre("RoI", 1))