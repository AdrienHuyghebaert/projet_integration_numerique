# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Méthodes des rectangles
# ================================================================================================

import numpy as np


# ================================================================================================
# Méthodes des rectangles

def methode_des_rectangles(a, b, n, p1, p2, p3, p4):
    pas = (b - a) / n
    aire_totale = 0  # Initialisation de l'aire totale sous la courbe
    x_i = a  # Initialisation de la borne inférieure
    liste_x = []  # Initialisation de la liste des x
    liste_y = []  # Initialisation de la liste des y
    for i in range(n):
        y_i = p1 + p2 * x_i + p3 * (x_i ** 2) + p4 * (x_i ** 3)
        aire_rectangle = pas * y_i
        aire_totale += aire_rectangle
        liste_x[i] = x_i
        liste_y[i] = y_i
        x_i += pas

    return aire_totale


#def methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4):
#    pas = np.linspace(a, b, n)
#    tableau_valeurs_numpy = np.array()


# ================================================================================================

a = 20
b = 40
n = 10
p1 = 10
p2 = 4
p3 = 1
p4 = 50

methode_des_rectangles(a, b, n, p1, p2, p3, p4)
