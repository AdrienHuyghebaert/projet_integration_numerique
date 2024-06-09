# ================================================================================================
# Auteur: Groupe
# Date: 9 juin 2024
# Intégrale numérique: Méthode des trapezes
# ================================================================================================

# Importation des packages

import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

a = 0
b = 100
n = 50
p1 = 1
p2 = 8
p3 = 5
p4 = 9

# Fonction 1: Calcul de la courbe polynomiale exacte et de son intégrale


def fonction_polynomiale(p1, p2, p3, p4, x):
    polynome = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)
    return polynome

def integrale_exacte(p1, p2, p3, p4, a, b):
    integrale_exacte = p1 * (b - a) + p2 * ((b ** 2) - (a ** 2))/2 + p3 * ((b ** 3) - (a ** 3))/3 + p4 * ((b ** 4) - (a ** 4))/4
    return integrale_exacte

print(integrale_exacte(p1, p2, p3, p4, a, b))

# Fonction 2: Méthode des trapezes en python
def methodes_trapezes_python(a, b, n, p1, p2, p3, p4):
    pas = (b-a)/n  # calcul du pas du découpage
    liste_pas = [a + i*pas for i in range(n+1)]
    liste_ordonnees_python = [fonction_polynomiale(p1, p2, p3, p4, x) for x in liste_pas]

    aire_totale = 0
    for j in range(n):
        aire_trapeze = (liste_pas[j+1] - liste_pas[j]) * ((liste_ordonnees_python[j] + liste_ordonnees_python[j+1]) / 2)
        aire_totale += aire_trapeze

    return aire_totale, liste_ordonnees_python

# Fonction 3: Méthode des trapèzes avec numpy


def methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4):
    pas = (b-a)/n
    liste_pas = np.array([a + pas * i for i in range(n+1)])
    aire_trapeze = np.zeros((n+1))
    liste_ordonnees = [fonction_polynomiale(p1, p2, p3, p4, x) for x in liste_pas]
    for i in range(n):
        aire_trapeze[i] = (liste_pas[i+1] - liste_pas[i]) * ((liste_ordonnees[i] + liste_ordonnees[i+1]) / 2)
    return np.sum(aire_trapeze), liste_ordonnees

# Fonction 4: Méthode des trapèzes avec scipy


def aire_trapeze_scipy(a, b, n, p1, p2, p3, p4):
    x = np.linspace(a, b, n + 1)
    y = fonction_polynomiale(p1, p2, p3, p4, x)
    return trapezoid(y, x)  # retourne l'aire sous la courbe


def convergence_scipy(a, b, p1, p2, p3, p4):
    liste_n = np.arange(1, 20, 1)
    diff = np.zeros((len(liste_n)))
    count = 0
    aire_exacte = integrale_exacte(p1, p2, p3, p4, a, b)
    for valeur in liste_n:
        diff[count] = abs(aire_trapeze_scipy(a, b, valeur, p1, p2, p3, p4) - aire_exacte)
        count += 1
    plt.plot(liste_n, diff)
    plt.title('Convergence fonction scipy')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur aire')
    plt.show()
    return

convergence_scipy(a, b, p1, p2, p3, p4)

# Fonction 5: Tracé des graphiques pour un nombre de segments n donné

def tracer_graphique(a, b, n, p1, p2, p3, p4):

    plt.rcParams['font.size'] = 8
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 200

    # Fonction analytique

    x = np.linspace(a, b, 200)
    y = [fonction_polynomiale(p1, p2, p3, p4, i) for i in x]

    # Méthode des trapèzes avec numpy

    f_a = methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4)[1]
    x_numpy = np.linspace(a, b, n+1)
    y_interp = np.interp(x, x_numpy, f_a)

    plt.subplot(1, 2, 1)
    plt.plot(x, y_interp, color='magenta', label='méthode numpy', linestyle='-')
    plt.plot(x, y, color='blue', label='fonction analytique', linestyle='-')
    plt.fill_between(x, y_interp, color='red', alpha=0.3)
    plt.title('Méthode des trapèzes avec numpy')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

    # Méthode des trapèzes avec python

    liste_ordonnees = methodes_trapezes_python(a, b, n, p1, p2, p3, p4)[1]
    y_interp_python = np.interp(x, x_numpy, liste_ordonnees)

    plt.subplot(1, 2, 2)
    plt.plot(x, y_interp_python, color='green', label='méthode python', linestyle='-')
    plt.plot(x, y, color='blue', label='fonction analytique', linestyle='-')
    plt.fill_between(x, y_interp_python, color='red', alpha=0.3)
    plt.title('Méthode des trapèzes avec python')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()

    plt.show()

    # Affichage des tableaux

    print("Tableau des ordonnées de la fonction polynomiale:\n", y, '\n')
    print("Aire totale sous la courbe méthode des trapèzes:",
          methodes_trapezes_python(a, b, n, p1, p2, p3, p4)[0], '\n')
    print("Aire totale sous la courbe avec scipy:", aire_trapeze_scipy(a, b, n, p1, p2, p3, p4), '\n')

    # Temps d'exécution de la méthode des trapèzes en python

    tic = perf_counter()
    methodes_trapezes_python(a, b, n, p1, p2, p3, p4)
    toc = perf_counter()
    print(f"Temps d'execution avec méthode trapèzes (python): {toc-tic} [s]", '\n')

    # Temps d'exécution de la méthode des trapèzes en numpy
    tic = perf_counter()
    methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4)
    toc = perf_counter()
    print(f"Temps d'execution avec méthode trapèzes (numpy): {toc-tic} [s]")

# Appel de la fonction

tracer_graphique(a, b, n, p1, p2, p3, p4)


# Fonction 6: Étude et affichage de la convergence et du temps de calcul
def convergence(p1, p2, p3, p4, a, b):
    liste_n = np.arange(1, 20, 1)
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

    # Affichage des 4 courbes

    plt.rcParams['font.size'] = 8
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    plt.subplot(2, 2, 1)
    plt.plot(liste_n, maximums_python, color='green')
    plt.title('Convergence de la méthode des trapèzes (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 2)
    plt.plot(liste_n, maximums_numpy, color='magenta')
    plt.title('Convergence de la méthode des trapèzes (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 3)
    plt.bar(liste_n, temps_calcul_python, color='green')
    plt.title('Temps de calcul méthode des trapèzes (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.subplot(2, 2, 4)
    plt.bar(liste_n, temps_calcul_numpy, color='magenta')
    plt.title('Temps de calcul méthode des trapèzes (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.show()


# Appel de la fonction

convergence(p1, p2, p3, p4, a, b)