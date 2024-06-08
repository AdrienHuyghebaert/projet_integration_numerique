# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Méthodes des rectangles
# ================================================================================================

import numpy as np
import matplotlib.pyplot as plt


# ================================================================================================
# Méthodes des rectangles "Python"

def methode_des_rectangles_py(a, pas, p_1, p_2, p_3, p_4, n):
    aire_totale = 0  # Initialisation de l'aire totale sous la courbe
    x_i = a  # Initialisation de la borne inférieure
    liste_x = []  # Initialisation de la liste des x
    liste_y = []  # Initialisation de la liste des y
    for i in range(n):
        y_i = p_1 + p_2 * x_i + p_3 * (x_i ** 2) + p_4 * (x_i ** 3)
        aire_rectangle = pas * y_i
        aire_totale += aire_rectangle
        liste_x.append(x_i)
        liste_y.append(y_i)
        x_i += pas
    return liste_x, liste_y, aire_totale


# ================================================================================================
# Méthodes des rectangles "Numpy"

def methode_des_rectangles_numpy(a, b, pas, p_1, p_2, p_3, p_4, n):
    x = np.linspace(a, b - pas, n)  # Génération des valeurs de x
    y = p_1 + p_2 * x + p_3 * (x ** 2) + p_4 * (x ** 3)  # Calcul des valeurs de y
    aire_totale = np.sum(pas * y)  # Calcul de l'aire totale
    return x, y, aire_totale

