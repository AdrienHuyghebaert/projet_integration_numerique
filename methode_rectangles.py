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
# Affichage des deux méthodes en fonction de la fonction et du nombre de segments
def tracer_graphiques(a, b, n, p1, p2, p3, p4):
    plt.rcParams['font.size'] = 8
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100

    # Fonction analytique

    x_ana = np.linspace(a, b, n)
    y_ana = [calculer_fonction_polynomiale(i, p1, p2, p3, p4) for i in x_ana]

    n = 10  # Affichage pour 10 segments
    pas = (b - a) / n  # Création du pas

    # Méthode des rectangles avec python
    x_rect_py = methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[0]
    y_rect_py = methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[1]
    plt.subplot(2, 2, 1)
    plt.bar(x_rect_py, y_rect_py, width=pas, align='edge', alpha=0.3, edgecolor='r', label='méthode Python')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2, label='fonction')
    plt.title(f'Méthode des rectangles avec python ({n} segments)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()

    # Méthode des rectangles avec numpy
    x_rect_np = methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[0]
    y_rect_np = methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[1]
    plt.subplot(2, 2, 2)
    plt.bar(x_rect_np, y_rect_np, width=pas, align='edge', alpha=0.3, edgecolor='r', label='méthode Numpy')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2, label='fonction')
    plt.title(f'Méthode des rectangles avec numpy({n} segments)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

    n = 1000  # Affichage pour 1000 segments
    pas = (b - a) / n  # Changement du pas

    # Méthode des rectangles avec python
    x_rect_py = methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[0]
    y_rect_py = methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[1]
    plt.subplot(2, 2, 3)
    plt.bar(x_rect_py, y_rect_py, width=pas, align='edge', alpha=0.3, edgecolor='r', label='méthode Python')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2, label='fonction')
    plt.title(f'Méthode des rectangles avec python ({n} segments)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()

    # Méthode des rectangles avec numpy
    x_rect_np = methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[0]
    y_rect_np = methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[1]
    plt.subplot(2, 2, 4)
    plt.bar(x_rect_np, y_rect_np, width=pas, align='edge', alpha=0.3, edgecolor='r', label='méthode Numpy')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2, label='fonction')
    plt.title(f'Méthode des rectangles avec numpy ({n} segments)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

    # Comparatif des valeurs des intégrales

    nombre_segments = [10, 1000, 5000, 10000]
    integrales_py = [methode_des_rectangles_py(a, b, n, p1, p2, p3, p4)[2] for n in nombre_segments]
    integrales_np = [methode_des_rectangles_numpy(a, b, n, p1, p2, p3, p4)[2] for n in nombre_segments]
    integrale_exacte = calculer_integrale_exacte(a, b, p1, p2, p3, p4)
    bar_width = 0.35
    index = np.arange(len(nombre_segments))

    fig, ax = plt.subplots()

    ax.bar(index - bar_width / 2, integrales_py, bar_width, label='Méthode Python', color='blue')
    ax.bar(index + bar_width / 2, integrales_np, bar_width, label='Méthode Numpy', color='red')

    ax.axhline(y=integrale_exacte, color='green', label='Intégrale exacte (analytique)')

    ax.set_xlabel('Nombre de segments')
    ax.set_ylabel('Valeur de l\'intégrale')
    ax.set_title('Comparaison des méthodes d\'intégration')
    ax.set_xticks(index)
    ax.set_xticklabels(nombre_segments)
    ax.legend()
    plt.tight_layout()
    plt.show()


# ================================================================================================
# Temps d'exécution des deux méthodes
def temps_execution(a, b, n, p1, p2, p3, p4):
    # Temps d'exécution de la méthode des rectangles en python
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

        # Convergence de la méthode des rectangles avec numpy
        erreurs_numpy[cpt] = abs(integrale_exacte - methode_des_rectangles_numpy(a, b, i, p1, p2, p3, p4)[2])

        cpt += 1

    # Régression linéaire pour l'affichage du temps de calcul python

    coefficients_python = np.polyfit(liste_n, temps_calcul_python, 1)  # 1 pour une régression linéaire
    slope, intercept = coefficients_python
    y_lineaire_python = slope * liste_n + intercept

    # Régression linéaire pour l'affichage du temps de calcul numpy

    coefficients_numpy = np.polyfit(liste_n, temps_calcul_numpy, 1)  # 1 pour une régression linéaire
    slope, intercept = coefficients_numpy
    y_lineaire_numpy = slope * liste_n + intercept

    return temps_calcul_python, temps_calcul_numpy, erreurs_python, erreurs_numpy, y_lineaire_python, y_lineaire_numpy


# ================================================================================================
# Fonction qui gère l'affichage des graphes des temps de calcul et des convergences
def afficher_courbes(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)

    plt.rcParams['font.size'] = 5
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    plt.subplot(2, 2, 1)
    plt.yscale('log')
    plt.plot(liste_n, etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[2], color='green')
    plt.title('Evolution de la convergence de la méthode des rectangles en fonction du nombre de segments (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur (échelle log)')

    plt.subplot(2, 2, 2)
    plt.yscale('log')
    plt.plot(liste_n, etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[3], color='magenta')
    plt.title('Evolution de la convergence de la méthode des rectangles en fonction du nombre de segments (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale (échelle log)')

    plt.subplot(2, 2, 3)
    plt.plot(liste_n, etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[4],
             color='green', label='méthode des rectangles (Python)')
    plt.plot(liste_n, etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4)[5],
             color='magenta', label='méthode des rectangles (Numpy)')
    plt.title('Evolution du temps de calcul de la méthode des rectangles en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.legend()
    plt.show()


# ================================================================================================
# Appel des fonctions

borne_a = -1
borne_b = 1
nombre_segments = 1000
p_1 = 24
p_2 = -30
p_3 = -50
p_4 = 3

# methode_des_rectangles_py(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
# calculer_integrale_exacte(borne_a, borne_b, p_1, p_2, p_3, p_4)
# temps_execution(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
# etudier_convergence_temps_calcul(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4))
tracer_graphiques(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
# afficher_courbes(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
