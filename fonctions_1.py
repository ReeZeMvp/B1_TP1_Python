# Ecrire une fonction nommée 'carre' qui prend en paramètre un entier 'x' et qui retourne son carré.
def carre(x):
    x = x ** 2
    return x
# Ecrire une fonction nommée 'check' qui prend en paramètre un entier 'x' et qui retourne True si jamais 'x' est inférieur à 10, False sinon
def check(x):
    if (x < 10):
        return True
    else:
        return False

if __name__ == "__main__":
    assert(carre(5) == 25)
    assert(carre(2) == 4)
    assert(carre(0) == 0)
    assert(carre(-10) == 100)
    print("Fonction carre validée ! ✔")

    assert(check(9) is True)
    assert(check(10) is False)
    assert(check(19) is False)
    assert(check(0) is True)
    assert(check(-67) is True)
    print("Fonction check validée ! ✔")
    print("Exercice validé ! 🎉")