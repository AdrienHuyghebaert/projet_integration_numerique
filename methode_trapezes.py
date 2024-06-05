# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Intégrale numérique: Méthode des trapezes
# ================================================================================================

import numpy as np

# Méthode des trapezes en python
def methodes_trapezes_python(a, b, n, p1, p2, p3, p4):
    pas = (b-a)/n # calcul du pas du découpage
    aire_totale = 0 # initialisation de l'aire totale sous la courbe
    a_i = a
    b_i = a + pas
    for i in range(n):
        f_a = p1 + p2 * a_i + p3 * (a_i ^ 2) + p4 * (a_i ^ 3)
        f_b = p1 + p2 * b_i + p3 * (b_i ^ 2) + p4 * (b_i ^ 3)
        aire_trapeze = (b - a) + (f_a + f_b) / 2
        aire_totale += aire_trapeze
        a_i += pas
        b_i += pas
    return aire_totale

# Méthode des trapèzes avec numpy

def methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4):
    pas = (b-a)/n
    liste_a = np.array([a + pas*i for i in range(n)])
    liste_b = np.array([2*a + pas*i for i in range(n-1)])
    print(liste_a)
    print(liste_b)
    f_a = np.zeros((n))
    f_b = np.zeros((n))
    aire_trapeze = np.zeros((n))
    for i in range(n):
        f_a[i] = p1 + p2 * liste_a[i] + p3 * (liste_a[i] ^ 2) + p4 * (liste_a[i] ^ 3)
        f_b[i] = p1 + p2 * liste_b[i] + p3 * (liste_b[i] ^ 2) + p4 * (liste_b[i] ^ 3)
        aire_trapeze[i] = (b - a) + (f_a[i] + f_b[i]) / 2
    return (np.sum(aire_trapeze))







