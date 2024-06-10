# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Méthodes des rectangles
# ================================================================================================
# Importation des packages

import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter


# ================================================================================================
# Méthode des rectangles "Python"

def methode_des_rectangles_py(a, b, n, p1, p2, p3, p4):
    pas = (b - a) / n  # calcul du pas
    aire_totale = 0  # Initialisation de l'aire totale sous la courbe
    x_i = a  # Initialisation de la borne inférieure
    liste_x = []  # Initialisation de la liste des x
    liste_y = []  # Initialisation de la liste des y
    for i in range(n):
        y_i = p1 + p2 * x_i + p3 * (x_i ** 2) + p4 * (x_i ** 3)
        aire_rectangle = pas * y_i
        aire_totale += aire_rectangle
        liste_x.append(x_i)
        liste_y.append(y_i)
        x_i += pas
    return liste_x, liste_y, aire_totale


# ================================================================================================
# Méthode des rectangles "Numpy"

def methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4):
    pas = (b - a) / n  # calcul du pas
    x = np.linspace(a, b - pas, n)  # Génération des valeurs de x
    y = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)  # Calcul des valeurs de y
    aire_totale = np.sum(pas * y)  # Calcul de l'aire totale
    return x, y, aire_totale


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
# Affichage des deux méthodes en fonction de la fonction
def tracer_graphique(a, b, n, p1, p2, p3, p4):
    plt.rcParams['font.size'] = 4
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100

    # Fonction analytique

    x_ana = np.linspace(a, b, n)
    y_ana = [calculer_fonction_polynomiale(i, p1, p2, p3, p4) for i in x_ana]

    # Création du pas
    pas = (b - a) / n

    # Méthode des rectangles avec python

    x_rect_py = methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[0]
    y_rect_py = methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[1]
    plt.subplot(1, 2, 1)
    plt.bar(x_rect_py, y_rect_py, width=pas, align='edge', alpha=0.3, edgecolor='r')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2)
    plt.title('Méthode des rectangles avec python')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()

    # Méthode des rectangles avec numpy

    x_rect_np = methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[0]
    y_rect_np = methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[1]

    plt.subplot(1, 2, 2)
    plt.bar(x_rect_np, y_rect_np, width=pas, align='edge', alpha=0.3, edgecolor='r')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2)
    plt.title('Méthode des rectangles avec numpy')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

    plt.show()

    # Affichage des tableaux

    print("Tableau des ordonnées de la fonction polynomiale:\n", y_ana, '\n')
    print("Aire totale sous la courbe avec la méthode des rectangles (python):",
          methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[2], '\n')
    print("Aire totale sous la courbe avec la méthode des rectangles (numpy):",
          methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[2], '\n')


# ================================================================================================
# Temps d'exécution des deux méthodes
def temps_execution(a, b, n, p1, p2, p3, p4):
    # Temps d'exécution de la méthode des trapèzes en python
    tic = perf_counter()
    methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)
    toc = perf_counter()
    tic_toc_py = toc - tic

    # Temps d'exécution de la méthode des rectangles en numpy
    tic_2 = perf_counter()
    methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)
    toc_2 = perf_counter()
    tic_toc_np = toc_2 - tic_2

    return tic_toc_py, tic_toc_np


# ================================================================================================
# Fonction qui étudie la convergence et le temps de calcul des 2 méthodes en fonction de la solution exacte
def etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)
    erreurs_python = np.zeros(len(liste_n))
    erreurs_numpy = np.zeros(len(liste_n))
    temps_calcul_python = np.zeros((len(liste_n)))
    temps_calcul_numpy = np.zeros((len(liste_n)))
    integrale_exacte = np.array(calculer_integrale_exacte(a, b, p1, p2, p3, p4))
    cpt = 0

    for i in liste_n:
        # Temps de calcul de la méthode des rectangles avec python
        temps_calcul_python[cpt] = temps_execution(a, b, i, p1, p2, p3, p4)[0]

        # Temps de calcul de la méthode des rectangles avec numpy
        temps_calcul_numpy[cpt] = temps_execution(a, b, i, p1, p2, p3, p4)[1]

        # Convergence de la méthode des rectangles avec python
        erreurs_python[cpt] = abs(integrale_exacte - methode_des_rectangles_py(a, b, i, p1, p2, p3, p4)[2])

        # Convergence méthode des rectangles avec numpy
        erreurs_numpy[cpt] = abs(integrale_exacte - methode_des_rectangles_numpy(a, b, i, p1, p2, p3, p4)[2])

        cpt += 1

    return temps_calcul_python, temps_calcul_numpy, erreurs_python, erreurs_numpy


# ================================================================================================
# Fonction qui gère l'affichage des graphes
def afficher_courbes(n, temps_calcul_python, temps_calcul_numpy, erreurs_python, erreurs_numpy):
    liste_n = np.arange(1, n + 1, 1)

    plt.rcParams['font.size'] = 4
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    plt.subplot(2, 2, 1)
    plt.plot(liste_n, erreurs_python, color='green')
    plt.title('Evolution de la convergence de la méthode des rectangles en fonction du nombre de segments (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 2)
    plt.plot(liste_n, erreurs_numpy, color='magenta')
    plt.title('Evolution de la convergence de la méthode des rectangles en fonction du nombre de segments (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 3)
    plt.bar(liste_n, temps_calcul_python, color='green')
    plt.title('Evolution du temps de calcul de la méthode des rectangles en fonction du nombre de segments (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.subplot(2, 2, 4)
    plt.bar(liste_n, temps_calcul_numpy, color='magenta')
    plt.title('Evolution du temps de calcul de la méthode des rectangles en fonction du nombre de segments (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.show()


# ================================================================================================
# Fonction principale
# Cette fonction permet d'estimer la convergence et le temps d'exécution lorsqu'on augmente le nombre de segments

borne_a = 20
borne_b = 40
nombre_segments = 100
p_1 = 10
p_2 = 4
p_3 = 1
p_4 = 50

# methode_des_rectangles_py(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
# calculer_integrale_exacte(borne_a, borne_b, p_1, p_2, p_3, p_4)
# temps_execution(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
temps_calcul_python, temps_calcul_numpy, erreurs_python, erreurs_numpy = (
    etudier_convergence_temps_calcul(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4))
# tracer_graphique(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
afficher_courbes(nombre_segments, temps_calcul_python, temps_calcul_numpy, erreurs_python, erreurs_numpy)
