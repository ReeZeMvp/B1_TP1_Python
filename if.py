def est_pair(x: int):
    """
    Compléter la fonction suivante pour qu'elle retourne 'True' si l'entier 'x' est pair, 'False' sinon
    """
    # Ecrire votre code ici
    if (x % 2 == 0): 
        return True
    else:
        return False

def calcul_taxes(revenus):
    """
    Compléter la fonction pour qu'elle renvoi les taxes à payer en fonction des différents seuils.
    Le calcul n'est pas progressif. Le taux séléctionné est appliqué à l'entiereté des revenus :
     - Si les revenus sont compris entre 0 et 10000 exclus, pas de taxes
     - Si les revenus sont compris entre 10000 inclus et 25000 exclus, 11% des revenus
     - Si les revenus sont compris entre 25000 inclus et 73000 exclus, 30% des revenus
     - Si les revenus sont compris entre 73000 inclus et 150000 exclus, 41% des revenus
     - Si les revenus sont supérieurs à 150000, 45% des revenus
    """
    # Ecrire votre code ici
    if (revenus < 10000):
        return 0
    elif (revenus >= 10000 and revenus < 25000):
        taxe = 11 * revenus / 100
        return taxe
    elif (revenus >= 25000 and revenus < 73000):
        taxe = 30 * revenus / 100
        return taxe
    elif (revenus >= 73000 and revenus < 150000):
        taxe = 41 * revenus / 100
        return taxe
    elif (revenus >= 150000):
        taxe = 45 * revenus / 100
        return taxe
    


if __name__ == "__main__":
    assert(est_pair(2) is True)
    assert(est_pair(0) is True)
    assert(est_pair(11) is False)
    assert(est_pair(15) is False)
    print("Fonction est_pair validée ! ✔")

    assert(calcul_taxes(5000) == 0)
    assert(calcul_taxes(10000) == 1100)
    assert(calcul_taxes(15000) == 1650)
    assert(calcul_taxes(24999) == 2749.89)
    assert(calcul_taxes(56000) == 16800)
    assert(calcul_taxes(73000) == 29930)
    assert(calcul_taxes(140000) == 57400)
    assert(calcul_taxes(189000) == 85050)
    print("Fonction calcul_taxes validée ! ✔")

    print("Exercice validé ! 🎉")
