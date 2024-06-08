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


# ================================================================================================
# Affichage des courbes
def afficher_courbes(liste_x_py, liste_y_py, x_np, y_np,  pas):
    plt.bar(liste_x_py, liste_y_py, width=pas, align='edge', alpha=0.8, edgecolor='b')
    plt.bar(liste_x_py, liste_y_py, width=pas, align='edge', alpha=0.3, edgecolor='g')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("Méthode des rectangles et solution analytique 'Python' et 'NumPy'")
    plt.show()


# ================================================================================================
# Fonction principale

borne_a = 20
borne_b = 40
n = 10
p1 = 10
p2 = 4
p3 = 1
p4 = 50

# Création du pas
pas_resolution = (borne_b - borne_a) / n

liste_x_python, liste_y_python, aire_totale_python =\
    methode_des_rectangles_py(borne_a, pas_resolution, p1, p2, p3, p4, n)

x_numpy, y_numpy, aire_totale_numpy = (
    methode_des_rectangles_numpy(borne_a, borne_b, pas_resolution, p1, p2, p3, p4, n))

afficher_courbes(liste_x_python, liste_y_python, x_numpy, y_numpy, pas_resolution)
