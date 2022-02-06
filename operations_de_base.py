def variables_entiers():
    """
    Créer une variable nommée 'addition' qui contiendra le résultat de l'addition de 'a' et 'b'
    Créer une variable nommée 'soustration' qui contiendra le résultat de la soustraction de 'a' par 'b'
    Créer une variable nommée 'multiplication' qui contiendra le résultat de le multiplication de 'a' par 'b'
    Créer une variable nommée 'division' qui contiendra le résultat de la division de 'a' par 'b'
    Créer une variable nommée 'reste' qui contiendra le modulo de 'a' par 'b'
    Créer une variable nommée 'carre' qui contiendra la valeur de 'a' au carré
    """
    a = 15
    b = 34

    # Ecrire votre code ici

    assert(addition == a + b)
    assert(soustraction == a - b)
    assert(multiplication == a * b)
    assert(division == a / b)
    assert(modulo == a % b)
    assert(carre == a ** 2)
    print("Exercice 1 Validé ! ✔")

def variables_boolean():
    """
    Compléter les variables ci-dessous avec les tests ssuivants :
     - condition1: x est égal à 5
     - condition2: x est égal à y
     - condition3: x est différent de y
     - condition4: x est inférieur à y
     - condition5: x est supérieur à y
     - condition6: y est supérieur ou égal à 10

    Evaluer les conditions 7 à 9 et compléter les assertions avec la bonne valeur
    """
    x = 5
    y = 10

    # Compléter les condition ci-dessous en fonction de l'énnoncé
    condition1 = __
    condition2 = __
    condition3 = __
    condition4 = __
    condition5 = __
    condition6 = __

    assert(condition1 is True)
    assert(condition2 is False)
    assert(condition3 is True)
    assert(condition4 is True)
    assert(condition5 is False)
    assert(condition6 is True)

    # Compléter les assertions ci-dessous en effectuant les évaluations
    condition7 = (x == 5) or (y == 5)
    condition8 = (x == 5) and (y == 5)
    condition9 = condition1 or condition2

    assert(condition7 is __)
    assert(condition8 is __)
    assert(condition9 is __)
    print("Exercice 2 Validé ! ✔")


def comparaisons_egal_vs_is():
    """
    Evaluer les conditions suivantes et compléter leurs valeurs dans les assertions.
    Est-ce qu'une des valeurs vous semble étrange ?
    """
    a = {5}
    b = {5}

    c = 1
    d = 1

    assert((a == b) is __)
    assert((a is b) is __)
    assert((c == d) is __)
    assert((c is d) is __)
    print("Exercice 3 Validé ! ✔")

def listes():
    """
    - Commpléter l'assertion concernant les deux listes vides. Malgré les deux manières de déclarer, sont-elle égales ?
    - Compléter la variable 'ma_liste' afin qu'elle contienne une liste avec les éléments suivants : 1, 2, 3
    - Compléter la variable 'premier_element' afin qu'elle récupère la valeur du premier élément de la variable 'ma_liste'
    - Compléter la variable 'dernier_element' afin qu'elle récupère la valeur du dernier élément de la variable 'ma_liste'
    - Compléter la variable 'slice_deux_derniers_elements' afin qu'elle récupère une sous-liste de la variable 'ma_liste'
        contenant les deux derniers éléments. slice_deux_derniers_elements sera donc une liste contenant les valeurs 2, 3
    - Compléter la variable 'liste_concat' pour qu'elle contienne la valeur de 'ma_liste' + [4, 5]. Que se passe-t-il lorsqu'on
        additionne deux listes ?
    - Compléter la variable 'in_liste' pour qu'elle contienne 'True' si l'élément 3 est dans la liste, ou 'False' sinon
    """
    liste_vide = list()
    liste_vide_2 = []

    ma_liste = __

    premier_element = __
    dernier_element = __
    
    slice_deux_derniers_elements = __
    
    liste_concat = __

    in_list = __

    assert((liste_vide == liste_vide_2) is __)
    assert(ma_liste == [1, 2, 3])
    assert(premier_element == 1)
    assert(dernier_element == 3)
    assert(slice_deux_derniers_elements == [2, 3])
    assert(liste_concat == [1, 2, 3, 4, 5])
    assert(in_list is True)
    print("Exercice 4 validé ! ✔")

def chaines_de_caracteres():
    """
    - Compléter la variable chaine1 pour qu'elle contienne la chaîne de caractères "Louise la mouche"
    - Compléter la variable chaine_avec_guillemet pour qu'elle contienne la chaîne de caractères 'Louise la "mouche"'
        Les guillemets font partie de la chaîne.
    - Compléter la variable caractere_4 pour qu'elle contienne le 4ème caractère de la variable 'chaine1'
    - Compléter la variable 'chaine2' pour qu'elle contienne 'chaine1' suivi de " mange un barbecue"
    - Compléter la variable 'sous_chaine' pour qu'elle contienne les caractères 7 et 8 de la variable 'chaine1'
    """
    chaine1 = __
    chaine_avec_guillemet = __
    caractere_4 = __
    chaine2 = __
    sous_chaine = __


    assert(chaine1 == "Louise la mouche")
    assert(chaine_avec_guillemet == "Louise la \"mouche\"")
    assert(caractere_4 == "i")
    assert(chaine2 == "Louise la mouche mange un barbecue")
    assert(sous_chaine == "la")
    print("Exercice 5 validé ! ✔")


if __name__ == "__main__":
    variables_entiers()
    variables_boolean()
    comparaisons_egal_vs_is()
    listes()
    chaines_de_caracteres()


__ = "A COMPLETER"
