# ================================================================================================
# Auteur: Groupe
# Date: 10 juin 2024
# Intégrale numérique: Méthode des trapezes
# ================================================================================================

# Importation des packages

import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

# p1 = 24
# p2 = -30
# p3 = -50
# p4 = 3
# a = -1
# b = 1
# n = 100

# ======================================= Fonction polynomiale ====================================================

# Fonction 1: Calcul de la courbe polynomiale exacte et de son intégrale


def fonction_polynomiale(p1, p2, p3, p4, x):
    polynome = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)
    return polynome

# Calcul aire exacte de l'intégrale


def integrale_exacte(p1, p2, p3, p4, a, b):
    integrale_exacte = (p1 * (b - a) + p2 * ((b ** 2) - (a ** 2))/2
                        + p3 * ((b ** 3) - (a ** 3))/3 + p4 * ((b ** 4) - (a ** 4))/4)
    return integrale_exacte

# ========================================== Méthode python ===============================================


# Fonction 2: Méthode des trapezes en python

def methodes_trapezes_python(a, b, n, p1, p2, p3, p4):
    pas = (b-a)/n  # calcul du pas du découpage
    liste_pas = [a + i*pas for i in range(n+1)]  # liste des valeurs de x
    liste_ordonnees_python = [fonction_polynomiale(p1, p2, p3, p4, x) for x in liste_pas]  # calcul des ordonnées y

    aire_totale = 0  # initialisation de la somme des aires de chaque trapèze
    for j in range(n):
        aire_trapeze = (liste_pas[j+1] - liste_pas[j]) * ((liste_ordonnees_python[j] + liste_ordonnees_python[j+1]) / 2)
        aire_totale += aire_trapeze

    return aire_totale, liste_ordonnees_python

# ======================================== Méthode calcul aire numpy ==========================================


# Fonction 3: Méthode des trapèzes avec numpy


def methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4):
    pas = (b-a)/n
    liste_pas = np.linspace(a, b, n + 1)
    liste_ordonnees = np.array([fonction_polynomiale(p1, p2, p3, p4, x) for x in liste_pas])
    aire_trapeze = pas * (liste_ordonnees[:-1] + liste_ordonnees[1:]) / 2
    return np.sum(aire_trapeze), liste_ordonnees

# ========================================== Méthode calcul aire scipy ========================================


# Fonction 4: Méthode des trapèzes avec scipy: calcul aire


def aire_trapeze_scipy(a, b, n, p1, p2, p3, p4):
    x = np.linspace(a, b, n + 1)
    y = fonction_polynomiale(p1, p2, p3, p4, x)
    return trapezoid(y, x)  # retourne l'aire sous la courbe


# Fonction 5: Convergence et temps de calcul de la méthode scipy

def calcul_convergence_temps_scipy(a, b, p1, p2, p3, p4, n):
    liste_n = np.arange(1, n+1, 1)
    diff = np.zeros((len(liste_n)))
    count = 0
    temps_calcul_scipy = np.zeros((len(liste_n)))
    aire_exacte = integrale_exacte(p1, p2, p3, p4, a, b)

    # Calcul erreur avec scipy
    for valeur in liste_n:
        diff[count] = abs(aire_trapeze_scipy(a, b, valeur, p1, p2, p3, p4) - aire_exacte)

    # Temps de calcul méthode des trapèzes avec scipy
        tic = perf_counter()
        aire_trapeze_scipy(a, b, valeur, p1, p2, p3, p4)
        toc = perf_counter()
        temps_calcul_scipy[count] = toc - tic

        count += 1
    return temps_calcul_scipy, diff


def tracer_convergence_temps_scipy(a, b, p1, p2, p3, p4, n):

    liste_n = np.arange(1, n + 1, 1)

    plt.subplot(1, 2, 1)
    plt.plot(liste_n, calcul_convergence_temps_scipy(a, b, p1, p2, p3, p4, n)[1])
    plt.title('Convergence fonction scipy')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur aire')

    plt.subplot(1, 2, 2)
    plt.bar(liste_n, calcul_convergence_temps_scipy(a, b, p1, p2, p3, p4, n)[0], color='cyan')
    plt.title('Temps de calcul méthode des trapèzes (scipy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')
    plt.show()

# ======================================= Graphiques aire méthode trapèzes =======================================

# Fonction 5: Tracé des graphiques pour un nombre de segments n donné


def tracer_graphique_trapeze(a, b, n, p1, p2, p3, p4):

    plt.rcParams['font.size'] = 8
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 200

    # Fonction analytique

    x = np.linspace(a, b, 200)
    y = [fonction_polynomiale(p1, p2, p3, p4, i) for i in x]

    # Méthode des trapèzes avec numpy

    # J'utilise la fonction interpolate pour le calcul des points situés entre chaque ordonnées f(a) et f(b) afin
    # d'avoir autant de point que la fonction polynomiale pour le tracé des courbes

    f_a = methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4)[1]
    x_numpy = np.linspace(a, b, n+1)
    y_interp = np.interp(x, x_numpy, f_a)

    plt.subplot(1, 2, 1)
    plt.plot(x, y_interp, color='magenta', label='méthode numpy', linestyle='-')
    plt.plot(x, y, color='blue', label='fonction analytique', linestyle='-', linewidth=0.8)
    plt.fill_between(x, y_interp, color='yellow', alpha=0.3)
    plt.title('Méthode des trapèzes avec numpy')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

    # Méthode des trapèzes avec python

    liste_ordonnees = methodes_trapezes_python(a, b, n, p1, p2, p3, p4)[1]
    y_interp_python = np.interp(x, x_numpy, liste_ordonnees)

    plt.subplot(1, 2, 2)
    plt.plot(x, y_interp_python, color='cyan', label='méthode python', linestyle='-')
    plt.plot(x, y, color='blue', label='fonction analytique', linestyle='-', linewidth=0.8)
    plt.fill_between(x, y_interp_python, color='yellow', alpha=0.3)
    plt.title('Méthode des trapèzes avec python')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()

    plt.show()

    # Affichage des tableaux

    print("Tableau des ordonnées de la fonction polynomiale:\n", y, '\n')
    print('-'*50 + 'Données aires' + '-'*50)
    print('Aire totale exacte:', integrale_exacte(p1, p2, p3, p4, a, b), '\n')
    print("Aire totale sous la courbe méthode des trapèzes:",
          methodes_trapezes_python(a, b, n, p1, p2, p3, p4)[0], '\n')
    print("Aire totale sous la courbe avec scipy:", aire_trapeze_scipy(a, b, n, p1, p2, p3, p4), '\n')
    print('-' * 115)

    # Temps d'exécution de la méthode des trapèzes en python

    tic1 = perf_counter()
    methodes_trapezes_python(a, b, n, p1, p2, p3, p4)
    toc1 = perf_counter()
    print(f"Temps d'execution avec méthode trapèzes (python): {toc1-tic1} [s]", '\n')

    # Temps d'exécution de la méthode des trapèzes en numpy
    tic2 = perf_counter()
    methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4)
    toc2 = perf_counter()
    print(f"Temps d'execution avec méthode trapèzes (numpy): {toc2-tic2} [s]")

    # Comparaison du temps d'exécution
    if toc1-tic1 > toc2-tic2:
        print('Méthode numpy plus rapide que méthode python')
    else:
        print('false')


# ======================================== Convergence et temps de calcul trapèzes =============================


# Fonction 6: Étude et affichage de la convergence et du temps de calcul
def calculer_temps_convergence(p1, p2, p3, p4, a, b, n):

    liste_n = np.arange(1, n+1, 1)
    diff_python = np.zeros((1000, len(liste_n)))
    diff_numpy = np.zeros((1000, len(liste_n)))
    maximums_python = np.zeros((len(liste_n)))
    maximums_numpy = np.zeros((len(liste_n)))
    temps_calcul_python = np.zeros((len(liste_n)))
    temps_calcul_numpy = np.zeros((len(liste_n)))
    x = np.linspace(a, b, 1000)
    y = [fonction_polynomiale(p1, p2, p3, p4, i) for i in x]
    cpt = 0
    for i in liste_n:
        x_numpy = np.linspace(a, b, i+1)

        # Temps de calcul méthode des trapèzes avec python
        tic = perf_counter()
        liste_ordonnees = methodes_trapezes_python(a, b, i, p1, p2, p3, p4)[1]
        toc = perf_counter()
        temps_calcul_python[cpt] = toc-tic

        # Temps de calcul méthode des trapèzes avec numpy
        tic_2 = perf_counter()
        liste_ordonnees_numpy = methodes_trapezes_numpy(a, b, i, p1, p2, p3, p4)[1]
        toc_2 = perf_counter()
        temps_calcul_numpy[cpt] = toc_2-tic_2

        # Convergence méthode des trapèzes avec python
        y_interp_python = np.interp(x, x_numpy, liste_ordonnees)
        diff_python[:, cpt] = abs(y - y_interp_python)
        maximums_python[cpt] = max(diff_python[:, cpt])

        # Convergence méthode des trapèzes avec numpy
        y_interp_numpy = np.interp(x, x_numpy, liste_ordonnees_numpy)
        diff_numpy[:, cpt] = abs(y - y_interp_numpy)
        maximums_numpy[cpt] = max(diff_numpy[:, cpt])

        cpt += 1

        return temps_calcul_numpy, maximums_numpy, temps_calcul_python, maximums_python


def tracer_convergence_temps_python_numpy(p1, p2, p3, p4, a, b, n):

    # Affichage des 4 courbes (convergence + temps de calcul)
    liste_n = np.arange(1, n + 1, 1)

    plt.rcParams['font.size'] = 8
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    plt.subplot(2, 2, 1)
    plt.plot(liste_n, calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[3], color='green')
    plt.title('Convergence de la méthode des trapèzes (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 2)
    plt.plot(liste_n, calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[1], color='magenta')
    plt.title('Convergence de la méthode des trapèzes (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 3)
    plt.bar(liste_n, calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[2], color='green')
    plt.title('Temps de calcul méthode des trapèzes (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.subplot(2, 2, 4)
    plt.bar(liste_n, calculer_temps_convergence(p1, p2, p3, p4, a, b, n)[0], color='magenta')
    plt.title('Temps de calcul méthode des trapèzes (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.show()