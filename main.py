# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Intégrale numérique
# ================================================================================================

# Importation des modules

import numpy as np
import matplotlib.pyplot as plt
import methode_rectangles
import methode_trapezes

# ================================================================================================
# Entrées utilisateur
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

    # Récupération des temps de calcul de la méthode des trapèzes
    temps_calcul_traps_numpy = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[0]
    temps_calcul_traps_python = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[2]

    # Récupération des temps de calcul de la méthode des rectangles
    temps_calcul_rect_python = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[0]
    temps_calcul_rect_numpy = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[1]

    # Affichage des courbes
    plt.rcParams['font.size'] = 4
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    # Avec Python
    plt.subplot(1, 2, 1)
    plt.plot(liste_n, temps_calcul_rect_python, color='blue', label='méthode des rectangles (Python)')
    plt.plot(liste_n, temps_calcul_traps_python, color='red', label='méthode des trapèzes (Python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')
    plt.title('Evolution du temps de calcul en fonction du nombre de segments avec Python')
    plt.legend()

    # Avec Numpy
    plt.subplot(1, 2, 2)
    plt.plot(liste_n, temps_calcul_rect_numpy, color='blue', label='méthode des rectangles (Numpy)')
    plt.plot(liste_n, temps_calcul_traps_numpy, color='red', label='méthode des trapèzes (Numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')
    plt.title('Evolution du temps de calcul en fonction du nombre de segments avec Numpy')
    plt.legend()

    plt.show()


# ================================================================================================
# Fonction qui compare la convergence
def comparer_convergence(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)

    # Récupération des convergences de la méthode des rectangles
    convergence_rect_python = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[2]
    convergence_rect_numpy = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[3]

    # Récupération des convergences de la méthode des trapèzes
    convergence_traps_python = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[3]
    convergence_traps_numpy = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[1]

    # Affichage des courbes
    plt.rcParams['font.size'] = 4
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    # Avec Python
    plt.subplot(1, 2, 1)
    plt.plot(liste_n, convergence_rect_python, color='blue', label='méthode des rectangles (Python)')
    plt.plot(liste_n, convergence_traps_python, color='red', label='méthode des trapèzes (Python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur')
    plt.title('Evolution de la convergence en fonction du nombre de segments avec Python')
    plt.legend()

    # Avec Python
    plt.subplot(1, 2, 2)
    plt.plot(liste_n, convergence_rect_numpy, color='blue', label='méthode des rectangles (Numpy)')
    plt.plot(liste_n, convergence_traps_numpy, color='red', label='méthode des trapèzes (Numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur')
    plt.title('Evolution de la convergence en fonction du nombre de segments avec Numpy')
    plt.legend()

    plt.show()


# ================================================================================================
# Appel des fonctions

comparer_temps_calcul(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
comparer_convergence(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
