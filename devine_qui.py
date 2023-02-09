from random import shuffle
from personnages import CARACTERISTIQUES
import math


# Fonction N°1

def types_caracteristiques_ordre_aleatoire():
    """
    Donne les types de caractéristiques dans un ordre aléatoire.

    Indices:
    - Vous pouvez obtenir le dictionnaire de caractéristiques en important CARACTERISTIQUES
        du module personnages.
    - Vous pouvez obtenir la liste des clés d'un dictionnaire avec list(dictionnaire.keys())
    - Utilisez la fonction shuffle importée pour mélanger l'ordre de la liste (Attention:
        shuffle ne retourne rien, mais modifie directement la liste en argument)

    Returns:
        list: La liste des types de caractéristiques
    """

    # VOTRE CODE ICI

    # création de la variable types_de_caracterstiques dans laquelle nous allons stocker la liste des caracteristiques

    types_de_carateristiques = list(CARACTERISTIQUES.keys())
    shuffle(types_de_carateristiques)

    return types_de_carateristiques


# Fonction N°2

def valeurs_ordre_aleatoire(type_caracteristique):
    """
    Donne les valeurs de caractéristiques dans un ordre aléatoire,
    pour un type de caractéristique donné.

    Attention!! Si vous utilisez shuffle directement sur la liste de valeurs,
    celles-ci sera modifiée pour la suite du programme (il ne faut pas).
    Faites-en d'abord une copie avec liste.copy()

    Args:
        type_caracteristique (string): Le type de caractéristique

    Returns:
        list: La liste des valeurs possibles pour ce type de caractéristique
    """
    # VOTRE CODE ICI

    # création de la variable valeurs_de_caractersiqtues qui vindra stcoker les valeurs de chaque type de carateristique

    valeurs_de_caracteristiques = CARACTERISTIQUES[type_caracteristique].copy()
    shuffle(valeurs_de_caracteristiques)

    return valeurs_de_caracteristiques


# Fonction N°3

def possede(donnees_personnage, type_caracteristique, valeur_caracteristique):
    """
    Indique si la valeur de caractéristique fait partie des données du personnage.

    Attention! Si le type de caractéristique est accessoires ou pilosite, il faut vérifier
    que la valeur cherchée EST DANS les données du personnage pour ce type, tandis que
    si le type est autre chose, il faut vérifier que la valeur cherchée EST la donnée du personnage
    pour ce type.

    Args:
        donnees_personnage (dict): Les données (sous forme type:valeur) pour un personnage
        type_caracteristique: Le type de caractéristique analysé
        valeur_caracteristique: La valeur de la caractéristique recherchée

    Returns:
        bool: True si le personnage possède la caractéristique, False sinon.
    """
    # VOTRE CODE ICI

    # Il s'agit ici de verifier si un personnage posséde la carateristique ou pas en tenant compte d'un cas spécial

    if type_caracteristique in ("accessoires", "pilosite"):
        return valeur_caracteristique in donnees_personnage[type_caracteristique]

    else:
        return donnees_personnage[type_caracteristique] == valeur_caracteristique


# Fonction N°4

def score_dichotomie(personnages_restants, type_caracteristique, valeur_caracteristique):
    """
    Retourne un score en fonction du nombre de personnages restants ayant ou n'ayant pas la
    caractéristique en paramètres.
    Ce score est élevé pour les caractéristiques divisant les personnages
    en deux parties le plus égales possibles, et est faible pour les caractéristiques divisant les
    personnages en parties inégales.

    Le score est calculé selon la formule suivante:
    nombre de personnages total - maximum(nombre de personnages ayant la caractéristique,
                                          nombre de personnages n'ayant pas la caractéristique)

    Exemple:
    En début de partie, il y 5 femmes sur 24 personnages. Le score de la caractéristique ayant le type genre
    et la valeur femme est donc 24 - maximum(5, 19), c'est-à-dire 5.
    En revanche, ce score peut changer en cours de partie. Par exemple supposons qu'il ne reste que
    les personnages ayant des chapeaux. Il y a alors 2 femmes sur 5 personnages. Le score
    de la caractéristique femme est donc 5 - maximum(2, 3), donc 2. Le score de la caractéristique
    lunettes serait quant à lui 5 - maximum(1, 4), c'est-à-dire 1. Cela indique que, parmi les personnages
    ayant des chapeaux, la caractéristique femme divise mieux l'ensemble que la caractéristique lunettes.

    Note: cette fonction devrait appeler la fonction possede.

    Args:
        personnages_restants (dict): L'ensemble des personnages n'ayant pas été éliminés encore.
        type_caracteristique (string): Le type de la caractéristique dont on veut connaître le score
        valeur_caracteristique (string): La valeur de la caractéristique dont on veut connaître le score

    Returns:
        int: Le score
    """
    # VOTRE CODE ICI

    # création de la variable personnages_total (type : entier) qui va stocker la longeur de personnages_restants.
    # création de la variable personnage_avec (type : entier) qui viendra compter le nombre de personnages qui possede
    # le type de caracteristique recherché et valeur associée.
    # création de la variable personnages_sans (type : entier) qui viendra compter le nombre de personnages qui ne
    # possedent pas le type de caracteristique recherché et valeur associée.

    personnages_total = len(personnages_restants)
    personnages_avec = 0
    personnages_sans = 0

    for nom in personnages_restants.values():
        if possede(nom, type_caracteristique, valeur_caracteristique):
            personnages_avec += 1
        else:
            personnages_sans += 1

    return personnages_total - max(personnages_avec, personnages_sans)


# Fonction N°5

def selectionner_caracteristique(personnages_restants):
    """
    Parmi tous les couples type/valeur de caractéristiques, retourne
    celui qui présente le meilleur score de dichotomie. Les types et valeurs doivent être
    itérées en ordre aléatoire (utilisez les fonctions à cet effet déclarées précédemment)

    Note: cette fonction devrait appeler les fonctions
        types_caracteristiques_ordre_aleatoire, valeurs_ordre_aleatoire et score_dichotomie.

    Args:
        personnages_restants (dict): Les personnages à considérer pour les scores.

    Returns:
        (string, string): Le type et la valeur ayant le meilleur score dichotomique
    """
    # VOTRE CODE ICI

    # création de la variable max_score qui viendra stocker le score le plus élevé
    # création des variables type_max et valeur_max qui viendront stocker le type et valeur maximum

    max_score = 0
    type_max, valeur_max = None, None
    for types in types_caracteristiques_ordre_aleatoire():
        for valeurs in valeurs_ordre_aleatoire(types):
            score = score_dichotomie(personnages_restants, types, valeurs)
            if score > max_score:
                max_score = score
                type_max, valeur_max = types, valeurs

    return type_max, valeur_max


# Fonction N°6

def mettre_a_jour_hypotheses(personnages_restants, type_caracteristique, valeur_caracteristique, reponse):
    """
    Retourne un dictionnaire basé sur le dictionnaire de personnages restants en paramètre, dans
    lequel on enlève les personnages qui possèdent ou ne possèdent pas la caractéristique en paramètres.

    Args:
        personnages_restants (dict): Les personnages préalablement restants
        type_caracteristique (string): Le type de la caractéristique dont on
                                       veut conserver/enlever ceux qui l'ont
        valeur_caracteristique (string): La valeur de la caractéristique dont
                                   on veut conserver/enlever ceux qui l'ont
        reponse (bool): True si on doit conserver les personnages qui possèdent la caractéristique,
                        False si on doit conserver ceux qui ne la possèdent pas.

    Note: cette fonction devrait appeler la fonction possede.

    Returns:
        dict: Le dictionnaire de personnages restants mis à jour.
    """
    # VOTRE CODE ICI

    dictionnaire = {}  # le dictionnaire que nous allons retourner

    for nom, donnee in personnages_restants.items():
        est_ce_possede = possede(donnee, type_caracteristique, valeur_caracteristique)
        veut_concerver = reponse
        if est_ce_possede and veut_concerver == True:
            dictionnaire[nom] = donnee
        elif not est_ce_possede and veut_concerver == False:
            dictionnaire[nom] = donnee
        else:
            dictionnaire = dictionnaire

    return dictionnaire


if __name__ == '__main__':
    print("Tests unitaires...")

    # Test de la fonction types_caracteristiques_ordre_aleatoire
    assert len(types_caracteristiques_ordre_aleatoire()) == len(CARACTERISTIQUES)

    # Test de la fonction valeurs_ordre_aleatoire
    assert len(valeurs_ordre_aleatoire("cheveux")) == len(CARACTERISTIQUES["cheveux"])

    # Tests de la fonction possede
    donnees = {"cheveux": "bruns", "accessoires": ["chapeau"]}
    assert possede(donnees, "cheveux", "bruns")
    assert not possede(donnees, "accessoires", "bijoux")

    # Tests de la fonction score_dichotomie
    personnages = {'Bernard': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Claire': {'genre': 'femme', 'accessoires': ['chapeau']},
                   'Eric': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'George': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Maria': {'genre': 'femme', 'accessoires': ['chapeau']}}
    assert score_dichotomie(personnages, 'genre', 'homme') == 2  # = 5 - max(3, 2)
    assert score_dichotomie(personnages, 'accessoires', 'chapeau') == 0  # = 5 - max(5, 0)

    # Aucun test n'est fourni pour selectionner_caracteristiques

    # Tests de la fonction mettre_a_jour_hypotheses

    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', True)) == 3
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', False)) == 2

    print("Tests réussis!")