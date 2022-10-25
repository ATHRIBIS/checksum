def check(C):
    L, s = [], 0 # L acceuil le code, s la somme de contrôle

    while C != 0: # convertisseur int en list
        C, r = divmod(C, 10) # renvoi un tuple, C le quotient, r le reste
        L.insert(0, r) # ajoute en début de liste le digit découpé
    l = len(L) # récupere la longueur du code

    rang = [i for i in range(l, 0, -1)]

    # création du rang en fonction du poids du premier et du dernier digit
    # ordre croissant du rang pour un premier digit supérieur au dernier
    # ordre décroissant du rang pour un dernier digit supérieur au premier

    for i in range(l): # traitement du code contenu dans la liste L
        j = rang[i] # permet d'appeler la valeur du rang plus facilement
        if (j % 2) == 0: # si le rang est paire, on multiplie la valeur au rang par deux
            L[i] += L[i] # poids bruts
            if L[i] > 9: L[i] -= 9 # poids corrigés
        s += L[i] # calcul de la somme de contrôle

    b = True if (s % 10) == 0 else False # validation du code
    return (b, s)

def calcul_cle(N):
    b, s = check(N)
    cle = 10 - (s % 10)
    return cle


C = 2008
print(check(C))
print(calcul_cle(C))
