# ================================================================================================
# Auteur: Rouanet Baptiste
# Date: 5 juin 2024
# Methode simpson
# ================================================================================================

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci


# Section calcul python simple
def formule_simpson_simple(p1, p2, p3, p4, a, b):
    int_intervalle = ((b-a)/6) * (fction_simple(p1, p2, p3, p4, a) + 4*fction_simple(p1, p2, p3, p4, (a+b)/2) + fction_simple(p1, p2, p3, p4, b))
    return int_intervalle


def calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, n):
    interval = (b - a)/n
    pts_courbe = [fction_simple(p1, p2, p3, p4, a)]
    somme = 0
    x = a
    i = n
    pts_calcul = [a]
    while i > 0:
        somme += formule_simpson_simple(p1, p2, p3, p4, x, x + interval)
        x += interval
        pts_courbe.append(fction_simple(p1, p2, p3, p4, x))
        pts_calcul.append(x)
        i -= 1
    return somme, pts_calcul, pts_courbe


def fction_simple(p1, p2, p3, p4, x):
    fct_eval = p1 + p2*x + p3*(x**2) + p4*(x**3)
    return fct_eval


# Section calcul python vectorisé

def formule_simpson_vect(p1, p2, p3, p4, a, b):
    int_intervalle = ((b-a)/6) * (fction_vect(p1, p2, p3, p4, a) + 4*fction_vect(p1, p2, p3, p4, (a+b)/2) + fction_vect(p1, p2, p3, p4, b))
    return int_intervalle


def calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, n):
    pts_calcul = np.linspace(a, b, n)
    pts_courbe = fction_vect(p1, p2, p3, p4, pts_calcul)
    somme = np.sum(formule_simpson_vect(p1, p2, p3, p4, pts_calcul[0:n-1], pts_calcul[1:n]))
    return somme, pts_calcul, pts_courbe


def fction_vect(p1, p2, p3, p4, x):
    fct_eval = p1 + p2*x + p3*np.power(x,2) + p4*np.power(x, 3)
    return fct_eval


# Section methode importée

def calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, n):
    pts_calcul = np.linspace(a, b, n)
    pts_courbe = p1 + p2*pts_calcul + p3*np.power(pts_calcul,2) + p4*np.power(pts_calcul, 3)
    somme = sci.simpson(pts_courbe, pts_calcul)
    return somme


# Tracé des courbes

def tracer_courbes(p1, p2, p3, p4, a, b, n):
    # On importe les résutlats des fonctions :

    fig, axs = plt.subplots(1, 3)
    fig.suptitle("Comparaison des résultats des méthodes Simpson")
    axs[0, 0].plt.plot()