def juft_sonlar(*args):
    juftlar = []
    for son in args:
        if son % 2 == 0:
            juftlar.append(son)
    return juftlar


print(juft_sonlar(1, 2, 3, 4, 5, 6))
