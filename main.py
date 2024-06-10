# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Intégrale numérique
# ================================================================================================

# Importation des modules

import numpy as np
import matplotlib.pyplot as plt
import methode_rectangles

# ================================================================================================
# Entrées utiliateur
borne_a = 20
borne_b = 40
nombre_segments = 1000
p_1 = 10
p_2 = 4
p_3 = 1
p_4 = 50


# ================================================================================================
# Calcul de la courbe polynomiale et de son intégrale

def calculer_fonction_polynomiale(x, p1, p2, p3, p4):
    polynome = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)
    return polynome


def calculer_integrale_exacte(a, b, p1, p2, p3, p4):
    integrale_exacte = p1 * (b - a) + p2 * ((b ** 2) - (a ** 2)) / 2 + p3 * ((b ** 3) - (a ** 3)) / 3 + p4 * (
            (b ** 4) - (a ** 4)) / 4
    return integrale_exacte


# ================================================================================================
# Fonction qui compare le temps de calcul
def comparer_temps_calcul(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)
    temps_calcul_rect_python = np.zeros((len(liste_n)))
    temps_calcul_rect_numpy = np.zeros((len(liste_n)))

    cpt = 0
    for i in liste_n:
        # Temps de calcul de la méthode des rectangles avec python
        temps_calcul_rect_python[cpt] = methode_rectangles.temps_execution(a, b, i, p1, p2, p3, p4)[0]

        # Temps de calcul de la méthode des rectangles avec numpy
        temps_calcul_rect_numpy[cpt] = methode_rectangles.temps_execution(a, b, i, p1, p2, p3, p4)[1]

        cpt += 1

    # Affichage des courbes
    plt.rcParams['font.size'] = 4
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    plt.plot(liste_n, temps_calcul_rect_python, color='green', label='méthode des rectangles (Python)')
    plt.plot(liste_n, temps_calcul_rect_numpy, color='magenta', label='méthode des rectangles (Numpy)')
    plt.title('Evolution du temps de calcul en fonction du nombre de segments et de la méthode choisie')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')
    plt.legend()
    plt.show()


# ================================================================================================
# Appel des fonctions

comparer_temps_calcul(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
