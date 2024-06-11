# ================================================================================================
# Auteur: Rouanet Baptiste
# Date: 10 juin 2024
# Intégrale numérique: Méthode de Simpson
# ================================================================================================

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci
from scipy.interpolate import CubicSpline
from time import perf_counter


# Section calcul python simple

# Fonction de calcul de l'aire sous la courbe entre les points a et b à l'aide de la fonction de Simspon
def formule_simpson_simple(p1, p2, p3, p4, a, b):
    int_intervalle = ((b - a) / 6) * (fction_simple(p1, p2, p3, p4, a) + 4 * fction_simple(p1, p2, p3, p4, (a + b) / 2)
                                      + fction_simple(p1, p2, p3, p4, b))
    return int_intervalle


# Calcul des points de la courbe et la valeur de l'intégrale selon la méthode de Simpson
def calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, n):
    # Creation de l'interval de calcul
    interval = abs(b - a) / n
    pts_courbe = [fction_simple(p1, p2, p3, p4, a)]
    somme = 0
    x = a
    i = n
    pts_calcul = [a]

    # calcul des points de la fonction associé aux valeurs de l'interval et de la somme des aires sous la courbe associé
    while i > 0:
        somme += formule_simpson_simple(p1, p2, p3, p4, x, x + interval)
        x += interval
        pts_courbe.append(fction_simple(p1, p2, p3, p4, x))
        pts_calcul.append(x)
        i -= 1
    return somme, pts_calcul, pts_courbe


# Calcul de la fonction à intégrer
def fction_simple(p1, p2, p3, p4, x):
    fct_eval = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)
    return fct_eval


# Section calcul python vectorisé

# Fonction de calcul de l'aire sous la courbe entre les points a et b à l'aide de la fonction de Simspon avec le module Numpy
def formule_simpson_vect(p1, p2, p3, p4, a, b):
    int_intervalle = ((b - a) / 6) * (fction_vect(p1, p2, p3, p4, a) + (4 * fction_vect(p1, p2, p3, p4, (a + b) / 2)) + fction_vect(p1, p2, p3, p4, b))
    return int_intervalle


def calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, n):
    # définition de l'interval de calcul
    pts_calcul = np.linspace(a, b, n+1)

    # calcul des points de la fonction associé aux valeurs de l'interval
    pts_courbe = fction_vect(p1, p2, p3, p4, pts_calcul)

    # et de la somme des aires sous la courbe associé
    somme = np.sum(formule_simpson_vect(p1, p2, p3, p4, pts_calcul[0:n], pts_calcul[1:n+1]))

    return somme, pts_calcul, pts_courbe


# Calcul de la fonction à intégrer à l'aide de Numpy
def fction_vect(p1, p2, p3, p4, x):
    fct_eval = p1 + p2 * x + p3 * np.power(x, 2) + p4 * np.power(x, 3)
    return fct_eval


# Section methode importée

def calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, n):
    # définition de l'interval de calcul
    pts_calcul = np.linspace(a, b, n+1)

    # calcul des points de la fonction associé aux valeurs de l'interval
    pts_courbe = p1 + p2 * pts_calcul + p3 * np.power(pts_calcul, 2) + p4 * np.power(pts_calcul, 3)

    # et de la somme des aires sous la courbe associé
    # lien de la doc : https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html
    somme = sci.simpson(pts_courbe, x=pts_calcul)  # Mettre les valeurs de y de la courbe en premier argument et le x associé en deuxième argument lien de la doc : https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html

    return somme


# ======================================= Graphiques aire méthode Simpson =======================================
def tracer_courbes(p1, p2, p3, p4, a, b, n):
    # On importe les résutlats des fonctions :
    somme_simple, pts_calcul_simple, pts_courbe_simple = calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, n)
    somme_vect, pts_calcul_vect, pts_courbe_vect = calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, n)

    # somme_scipy = calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, n)

    # Données de la courbe basique :
    pts_calcul = np.linspace(a, b, 300)
    pts_courbe = p1 + p2 * pts_calcul + p3 * np.power(pts_calcul, 2) + p4 * np.power(pts_calcul, 3)

    # J'utilise la fonction interpolate pour le calcul des points situés entre chaque ordonnées f(a) et f(b) afin
    # d'avoir autant de point que la fonction polynomiale pour le tracé des courbes
    y_interp_simple = CubicSpline(pts_calcul_simple, pts_courbe_simple)
    y_interp_vect = CubicSpline(pts_calcul_vect, pts_courbe_vect)

    # On trace les graphiques associés
    plt.figure(10)
    plt.suptitle("Comparaison des résultats des méthodes Simpson")

    # On trace le graph de la méthode simple
    plt.subplot(121).set_title("Méthode simple")
    plt.plot(pts_calcul, y_interp_simple(pts_calcul), label="methode python", color='#27F94E')
    plt.plot(pts_calcul, pts_courbe, label="fonction analytique", color='#F53315')
    plt.fill_between(pts_calcul, y_interp_simple(pts_calcul), color='#27F94E', alpha=0.3)
    plt.legend()
    plt.grid()

    # On trace le graph de la méthode vectorisée
    plt.subplot(122).set_title("Méthode vectorisée")
    plt.plot(pts_calcul, y_interp_vect(pts_calcul), label="methode numpy", color='#27C6F9')
    plt.plot(pts_calcul, pts_courbe, label="fonction analytique", color='#F53315')
    plt.fill_between(pts_calcul, y_interp_vect(pts_calcul), color='#27C6F9', alpha=0.3)
    plt.legend()
    plt.grid()

    plt.show()


def calculer_integrale_exacte(a, b, p1, p2, p3, p4):
    integrale_exacte = p1 * (b - a) + p2 * ((b ** 2) - (a ** 2)) / 2 + p3 * ((b ** 3) - (a ** 3)) / 3 + p4 * (
            (b ** 4) - (a ** 4)) / 4
    return integrale_exacte


# ================================================================================================
# Temps d'exécution des deux méthodes
def temps_execution(a, b, n, p1, p2, p3, p4):
    # Temps d'exécution de la méthode de Simpson en python
    tic = perf_counter()
    calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, n)
    toc = perf_counter()
    tic_toc_py = toc - tic

    # Temps d'exécution de la méthode de Simpson en numpy
    tic_2 = perf_counter()
    calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, n)
    toc_2 = perf_counter()
    tic_toc_np = toc_2 - tic_2

    # Temps d'exécution de la méthode de Simpson importée
    tic_3 = perf_counter()
    calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, n)
    toc_3 = perf_counter()
    tic_toc_scipy = toc_3 - tic_3
    return tic_toc_py, tic_toc_np, tic_toc_scipy


# ================================================================================================
# Fonction qui étudie la convergence et le temps de calcul des 2 méthodes en fonction de la solution exacte
def etudier_convergence_temps_calcul(a, b, n, p1, p2, p3, p4):
    liste_n = np.arange(1, n + 1, 1)
    erreurs_python = np.zeros(len(liste_n))
    erreurs_numpy = np.zeros(len(liste_n))
    erreurs_scipy = np.zeros(len(liste_n))
    temps_calcul_python = np.zeros((len(liste_n)))
    temps_calcul_numpy = np.zeros((len(liste_n)))
    temps_calcul_scipy = np.zeros((len(liste_n)))
    integrale_exacte = np.array(calculer_integrale_exacte(a, b, p1, p2, p3, p4))
    cpt = 0

    for i in liste_n:
        temps_exec = temps_execution(a, b, i, p1, p2, p3, p4)
        # Temps de calcul de la méthode de Simpson python
        temps_calcul_python[cpt] = temps_exec[0]

        # Temps de calcul de la méthode de Sympson avec numpy
        temps_calcul_numpy[cpt] = temps_exec[1]

        # Temps de calcul de la méthode de Sympson avec la fonction importrée
        temps_calcul_scipy[cpt] = temps_exec[2]

        # Convergence de la méthode avec python
        int_simple_simspon = calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, i)[0]
        erreurs_python[cpt] = integrale_exacte - int_simple_simspon

        # Convergence méthode avec numpy
        int_vect_simpson = calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, i)[0]
        erreurs_numpy[cpt] = integrale_exacte - int_vect_simpson

        # Convergence méthode importée avec scipy
        int_scipy_simpson = calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, i)
        erreurs_scipy[cpt] = integrale_exacte - int_scipy_simpson

        cpt += 1

    return temps_calcul_python, temps_calcul_numpy, temps_calcul_scipy, erreurs_python, erreurs_numpy, erreurs_scipy


# ================================================================================================
# Fonction qui gère l'affichage des graphes
def afficher_courbes(n, temps_calc_python, temps_calc_numpy, temps_calc_scipy, erreurs_pyt, erreurs_num, erreurs_sci):
    liste_n = np.arange(1, n + 1, 1)

    # Affichage des 4 courbes
    plt.rcParams['font.size'] = 4
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 125

    plt.subplot(2, 2, 1)
    plt.plot(liste_n, erreurs_pyt, color='green')
    plt.title('Evolution de la convergence de la méthode de Simpson en fonction du nombre de segments (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 2)
    plt.plot(liste_n, erreurs_num, color='magenta')
    plt.title('Evolution de la convergence de la méthode de Simpson en fonction du nombre de segments (numpy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.subplot(2, 2, 3)
    plt.plot(liste_n, temps_calc_python, color='green')
    plt.plot(liste_n, temps_calc_numpy, color='magenta')
    plt.plot(liste_n, temps_calc_scipy, color='yellow')
    plt.title('Evolution du temps de calcul de la méthode de Simspon en fonction du nombre de segments (python)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (s)')

    plt.subplot(2, 2, 4)
    plt.yscale('log')
    plt.plot(liste_n, erreurs_sci, color='yellow')
    plt.title('Evolution de la convergence de la méthode de Simpson importée en fonction du nombre de segments (scipy)')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur maximale')

    plt.show()


# Paramètres de test :

p_1 = 24
p_2 = -30
p_3 = -50
p_4 = 3
borne_a = -1
borne_b = 1
nombre_segments = 500

# ================================================================================================
# Zone d'appel des fonctions :

# tracer_courbes(p_1, p_2, p_3, p_4, borne_a, borne_b, nombre_segments)
temps_calcul_python, temps_calcul_numpy, temps_calcul_scipy, erreurs_python, erreurs_numpy, erreurs_scipy = etudier_convergence_temps_calcul(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
# tracer_graphique(borne_a, borne_b, nombre_segments, p_1, p_2, p_3, p_4)
afficher_courbes(nombre_segments, temps_calcul_python, temps_calcul_numpy, temps_calcul_scipy, erreurs_python, erreurs_numpy, erreurs_scipy)
