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
import methode_simpson

# ================================================================================================
# Entrées utilisateur
borne_a = -1
borne_b = 1
nombre_segments = 2000
p_1 = 24
p_2 = -30
p_3 = -50
p_4 = 3


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
# Fonction qui compare le temps de calcul des différentes méthodes
def comparer_temps_calcul(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)

    # Récupération des temps de calcul de la méthode des trapèzes
    temps_calcul_traps_numpy = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[5]
    temps_calcul_traps_python = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[4]

    # Récupération des temps de calcul de la méthode des rectangles
    temps_calcul_rect_python = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[4]
    temps_calcul_rect_numpy = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[5]

    # Récupération des temps de calcul de la méthode de Simpson
    temps_calcul_simp_python = methode_simpson.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[6]
    temps_calcul_simp_numpy = methode_simpson.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[7]

    # Affichage des courbes
    plt.rcParams['font.size'] = 12
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    # Avec Python
    plt.plot(liste_n, temps_calcul_rect_python, color='blue', label='méthode des rectangles (Python)')
    plt.plot(liste_n, temps_calcul_traps_python, color='red', label='méthode des trapèzes (Python)')
    plt.plot(liste_n, temps_calcul_simp_python, color='green', label='méthode de Simpson (Python)')

    # Avec Numpy
    plt.plot(liste_n, temps_calcul_rect_numpy, color='blue', linestyle='--', label='méthode des rectangles (Numpy)')
    plt.plot(liste_n, temps_calcul_traps_numpy, color='red', linestyle='--', label='méthode des trapèzes (Numpy)')
    plt.plot(liste_n, temps_calcul_simp_numpy, color='green', linestyle='--', label='méthode de Simpson (Numpy)')

    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')
    plt.title('Evolution du temps de calcul en fonction du nombre de segments et de la méthode')
    plt.legend()

    plt.show()


# ================================================================================================
# Fonction qui compare la convergence des différentes méthodes
def comparer_convergence(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)

    # Récupération des convergences de la méthode des rectangles
    convergence_rect_python = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[2]
    convergence_rect_numpy = methode_rectangles.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[3]

    # Récupération des convergences de la méthode des trapèzes
    convergence_traps_python = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[3]
    convergence_traps_numpy = methode_trapezes.calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[1]

    # Récupération des convergences de la méthode de Simpson
    convergence_simp_python = methode_simpson.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[3]
    convergence_simp_numpy = methode_simpson.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[4]

    # Affichage des courbes
    plt.rcParams['font.size'] = 12
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125
    plt.yscale('log')

    # Avec Python
    plt.plot(liste_n, convergence_rect_python, color='blue',  label='méthode des rectangles (Python)')
    plt.plot(liste_n, convergence_traps_python, color='red', label='méthode des trapèzes (Python)')
    plt.plot(liste_n, convergence_simp_python, color='green', label='méthode de Simpson (Python)')

    # Avec Numpy
    plt.plot(liste_n, convergence_rect_numpy, color='blue', linestyle='--', label='méthode des rectangles (Numpy)')
    plt.plot(liste_n, convergence_traps_numpy, color='red', linestyle='--', label='méthode des trapèzes (Numpy)')
    plt.plot(liste_n, convergence_simp_numpy, color='green', linestyle='--', label='méthode de Simpson (Python)')

    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur')
    plt.title('Evolution de la convergence en fonction du nombre de segments et de la méthode')
    plt.legend()

    plt.show()


# ================================================================================================
# Fonction qui compare la convergence et le temps de calcul des méthodes pré-programmées
# dans le package Scipy (Trapèzes et Simpson)
def comparer_scipy(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)

    # Récupération du temps de calcul et de la convergence de la méthode des trapèzes de Scipy
    temps_calcul_trap = methode_trapezes.calcul_convergence_temps_scipy(a, b, p1, p2, p3, p4, n)[2]
    convergence_trap = methode_trapezes.calcul_convergence_temps_scipy(a, b, p1, p2, p3, p4, n)[1]

    # Récupération du temps de calcul et de la convergence de la méthode de Simpson de Scipy
    temps_calcul_simp = methode_simpson.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[8]
    convergence_simp = methode_simpson.etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[5]

    # Affichage des courbes
    plt.rcParams['font.size'] = 5.5
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    # Temps de calcul
    plt.subplot(1, 2, 1)
    plt.plot(liste_n, temps_calcul_trap, color='red', label='méthode des trapèzes (Scipy)')
    plt.plot(liste_n, temps_calcul_simp, color='green', label='méthode de Simpson (Scipy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')
    plt.title('Evolution du temps de calcul en fonction du nombre de segments et de la méthode intégrée dans Scipy')
    plt.legend()

    # Convergence
    plt.subplot(1, 2, 2)
    plt.yscale('log')
    plt.plot(liste_n, convergence_trap, color='red', label='méthode des trapèzes (Scipy)')
    plt.plot(liste_n, convergence_simp, color='green', label='méthode des Simpson (Scipy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur')
    plt.title('Evolution de la convergence en fonction du nombre de segments et de la méthode intégrée dans Scipy')
    plt.legend()

    plt.show()


# ================================================================================================
# Appel des fonctions

comparer_temps_calcul(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
comparer_convergence(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
comparer_scipy(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
