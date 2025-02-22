def lire_graphe_triangulaire(fichier):
    """
    Lit un fichier DIMACS et convertit le graphe en une matrice triangulaire inférieure.

    :param fichier: Chemin du fichier .col
    :return: Matrice triangulaire inférieure sous forme de liste de listes
    """
    with open(fichier, 'r') as f:
        # Lit toutes les lignes et les stocke dans une liste lignes.
        lignes = f.readlines()

    nb_sommets = 0
    # Une liste de tuples où chaque tuple (sommet1, sommet2) représente une arête du graphe.
    aretes = []
    
    for ligne in lignes:  # Parcourt toutes les lignes du fichier une par une.
        ligne = ligne.strip() # Supprime les espaces inutiles au début et à la fin de la ligne.
        if ligne.startswith('p'): # Vérifie si la ligne commence par 'p', ce qui signifie qu'elle donne des informations sur le graphe.
            _, _, nb_sommets, _ = ligne.split() # divise la ligne en mots et extrait nb_sommets qui est converti en entier (int()).
            nb_sommets = int(nb_sommets)
        elif ligne.startswith('e'):
            _, sommet1, sommet2 = ligne.split() # Vérifie si la ligne commence par 'e', ce qui signifie qu'elle décrit une arête entre deux sommets.
            sommet1, sommet2 = int(sommet1), int(sommet2)
            aretes.append((sommet1, sommet2))

    # Création d'une matrice triangulaire inférieure
    matrice_triangulaire = [[0] * (i + 1) for i in range(nb_sommets)]

    # Remplir la matrice triangulaire inférieure
    for sommet1, sommet2 in aretes:
        sommet1 -= 1  # Ajustement des indices (DIMACS commence à 1, Python à 0)
        sommet2 -= 1

        if sommet1 > sommet2:
            matrice_triangulaire[sommet1][sommet2] = 1
        else:
            matrice_triangulaire[sommet2][sommet1] = 1

    return matrice_triangulaire

def afficher_matrice_triangulaire(matrice):
    """
    Affiche la matrice d'adjacence.
    Parcourt chaque ligne de la matrice.
    Convertit chaque élément de la ligne en chaîne de caractères (map(str, ligne)).
    Utilise " ".join(...) pour afficher la ligne avec des espaces entre les éléments
    """
    for ligne in matrice:
        print(" ".join(map(str, ligne)))

fichier = "H:/2CS/Modules/OPTIM/TP/dsjc1000.1.col.txt"  
matrice_triangulaire = lire_graphe_triangulaire(fichier)

print("Matrice triangulaire inférieure :")
afficher_matrice_triangulaire(matrice_triangulaire)
