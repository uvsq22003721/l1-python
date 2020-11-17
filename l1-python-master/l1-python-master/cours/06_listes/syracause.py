def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    res = []
    while True:
        res.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return res
print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max + 1):
        syracuse(1)
    return True

print(testeConjecture(10000))

def tempsVol(n):
    """ Retourne le temps de vol de n """
    

print("Le temps de vol de", 3, "est", tempsVol(3))