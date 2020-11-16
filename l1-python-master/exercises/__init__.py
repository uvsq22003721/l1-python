def motsCommuns(mot1, mot2) :
    """ Fonction qui prend en entrée deux chaînes de caractères et renvoie une liste contenant
        les mots communs de ces deux chaînes."""
    
    # La méthode .split() convertit une chaîne en une liste de mots.
    liste1 = mot1.split()
    liste2 = mot2.split()
    
    listeCommune = []
    for x in liste1: 
        if x in liste2:
            listeCommune.append(x)
    return listeCommune
    
listeMotsCommuns = motsCommuns("Python est un langage de programmation sympa", "Programmer en Python est facile")
print("Les mots communs sont :", listeMotsCommuns)