def somme_entiers(n):
    """
    Ecrire la fonction somme_entiers, qui prend un entier 'n' en paramètre d'entrée, et qui va calculer la somme de tous les entiers naturels jusqu'à n.
    Exemple: pour n = 10, la fonction doit retourner 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    """
    # Ecrire votre code ici
    pass

def minimum_dans_liste(elements):
    """
    Ecrire la fonction minimum_dans_liste, qui prend en entrée une liste d'entiers 'elements', et qui va renvoyer l'entier le plus petit présent dans la liste.
    Exemple: Pour elements = [1, 5, -5, 10], la fonction doit retourner -5
    """
    # Ecrire votre code ici
    pass

def inverser_liste(liste):
    """
    Ecrire la fonction inverser_liste qui va renverser tous les éléments dans la liste passée en paramètre.
    Exemple: Pour liste = [1, 2, 3, 4, 5, 6], la fonction doit retourner [6, 5, 4, 3, 2, 1]
    """
    # Ecrire votre code ici
    pass

def compter_nombre_digits(n):
    """
    Ecrire la fonction compter_nombre_digits, qui prend en entrée un entier n, et qui renverra le nombre de chiffres qui compose cet entier.
    Exemple: Pour n = 54378, la fonction doit retourner 5
    """
    # Ecrire votre code ici
    pass

def decaler_zeros(liste):
    """
    Ecrire la fonction decaler_zeros, qui prend en entrée une liste d'entiers n, et qui déplacera tout les 0 à la fin de la liste avant de la renvoyer.
    Exemple: Pour liste = [45, 0, 7, 12, 98, 0, 0, 1, 54], la fonction doit renvoyer [45, 7, 12, 98, 1, 54, 0, 0, 0]
    """
    # Ecrire votre code ici
    pass


if __name__ == "__main__":
    assert(somme_entiers(10) == 55)
    assert(somme_entiers(15) == 120)
    assert(somme_entiers(0) == 0)
    assert(somme_entiers(200) == 20100)
    assert(somme_entiers(1560) == 1217580)
    print("Fonction somme_entiers validée ! ✔")

    assert(minimum_dans_liste([1, 5, -5, 10]) == -5)
    assert(minimum_dans_liste([0, 0, 0, 0]) == 0)
    assert(minimum_dans_liste([1, 2, 67, 43, 23, 8675, 45325346, 24565, 12354, -56, -567654, 10, -5666666778]) == -5666666778)
    print("Fonction minimum_dans_liste validée ! ✔")

    assert(inverser_liste([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1])
    assert(inverser_liste([564, 43, 78, -1, 98, 3421]) == [3421, 98, -1, 78, 43, 564])
    assert(inverser_liste([]) == [])
    assert(inverser_liste([1]) == [1])
    print("Fonction inverser_liste validée ! ✔")

    assert(compter_nombre_digits(54378) == 5)
    assert(compter_nombre_digits(1) == 1)
    assert(compter_nombre_digits(657434567898765) == 15)
    assert(compter_nombre_digits(0) == 1)
    print("Fonction compter_nombre_digits validée ! ✔")

    assert(decaler_zeros([45, 0, 7, 12, 98, 0, 0, 1, 54]) == [45, 7, 12, 98, 1, 54, 0, 0, 0])
    assert(decaler_zeros([0, 0, 0]) == [0, 0, 0])
    assert(decaler_zeros([1, 45, 67, 89]) == [1, 45, 67, 89])
    assert(decaler_zeros([]) == [])
    assert(decaler_zeros([0, 0, 0, 7]) == [7, 0, 0, 0])
    print("Fonction decaler_zeros validée ! ✔")

    print("Exercice validé ! 🎉")
