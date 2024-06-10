# ================================================================================================
# Auteur: Rouanet Baptiste
# Date: 5 juin 2024
# Methode simpson
# ================================================================================================

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci


# Section calcul python simple

# Fonction de calcul de l'aire sous la courbe entre les points a et b à l'aide de la fonction de Simspon
def formule_simpson_simple(p1, p2, p3, p4, a, b):
    int_intervalle = ((b-a)/6) * (fction_simple(p1, p2, p3, p4, a) + 4*fction_simple(p1, p2, p3, p4, (a+b)/2) + fction_simple(p1, p2, p3, p4, b))
    return int_intervalle


# Calcul des points de la courbe et la valeur de l'intégrale selon la méthode de Simpson
def calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, n):
    # Creation de l'interval de calcul
    interval = (b - a)/n
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
    fct_eval = p1 + p2*x + p3*(x**2) + p4*(x**3)
    return fct_eval


# Section calcul python vectorisé

# Fonction de calcul de l'aire sous la courbe entre les points a et b à l'aide de la fonction de Simspon avec le module Numpy
def formule_simpson_vect(p1, p2, p3, p4, a, b):
    int_intervalle = ((b-a)/6) * (fction_vect(p1, p2, p3, p4, a) + 4*fction_vect(p1, p2, p3, p4, (a+b)/2) + fction_vect(p1, p2, p3, p4, b))
    return int_intervalle


def calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, n):
    # définition de l'interval de calcul
    pts_calcul = np.linspace(a, b, n)

    # calcul des points de la fonction associé aux valeurs de l'interval
    pts_courbe = fction_vect(p1, p2, p3, p4, pts_calcul)

    # et de la somme des aires sous la courbe associé
    somme = np.sum(formule_simpson_vect(p1, p2, p3, p4, pts_calcul[0:n-1], pts_calcul[1:n]))

    return somme, pts_calcul, pts_courbe


# Calcul de la fonction à intégrer à l'aide de Numpy
def fction_vect(p1, p2, p3, p4, x):
    fct_eval = p1 + p2*x + p3*np.power(x,2) + p4*np.power(x, 3)
    return fct_eval


# Section methode importée

def calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, n):
    # définition de l'interval de calcul
    pts_calcul = np.linspace(a, b, n)

    # calcul des points de la fonction associé aux valeurs de l'interval
    pts_courbe = p1 + p2*pts_calcul + p3*np.power(pts_calcul, 2) + p4*np.power(pts_calcul, 3)

    # et de la somme des aires sous la courbe associé
    # lien de la doc : https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html
    somme = sci.simpson(pts_courbe, x=pts_calcul)  # Mettre les valeurs de y de la courbe en premier argument et le x associé en deuxième argument lien de la doc : https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html

    return somme


# Tracé des courbes

def tracer_courbes(p1, p2, p3, p4, a, b, n):
    # On importe les résutlats des fonctions :
    somme_simple, pts_calcul_simple, pts_courbe_simple = calcul_integrale_simpson_simple(p1, p2, p3, p4, a, b, n)
    somme_vect, pts_calcul_vect, pts_courbe_vect = calcul_integrale_simpson_vect(p1, p2, p3, p4, a, b, n)
    somme_scipy = calcul_integrale_simpson_scipy(p1, p2, p3, p4, a, b, n)

    # Données de la courbe basique :
    pts_calcul = np.linspace(a, b, n)
    pts_courbe = p1 + p2 * pts_calcul + p3 * np.power(pts_calcul, 2) + p4 * np.power(pts_calcul, 3)
    # On trace les graphiques associés
    plt.figure(10)
    # fig, axs = plt.subplots(1, 3)
    plt.suptitle("Comparaison des résultats des méthodes Simpson")

    # On trace le graph de la méthode simple
    plt.subplot(121).set_title("Méthode simple")
    plt.plot(pts_calcul_simple, pts_courbe_simple, label="Méthode simple", color='#27F94E')
    plt.plot(pts_calcul, pts_courbe, label="Courbe primitive", color='#F53315')
    plt.fill_between(pts_calcul_simple, pts_courbe_simple, color='#539ecd')
    plt.legend()
    plt.grid()

    # On trace le graph de la méthode vectorisée
    plt.subplot(122).set_title("Méthode vectorisée")
    plt.plot(pts_calcul_vect, pts_courbe_vect, label="Méthode vectorisée", color='#27C6F9')
    plt.plot(pts_calcul, pts_courbe, label="Courbe primitive", color='#F53315')
    plt.fill_between(pts_calcul_vect, pts_courbe_vect, color='#539ecd')
    plt.legend()
    plt.grid()

    plt.show()

------------------------------------------------------------------------------------------------------------------------
### Paramètres de test :

# p1 = 24
# p2 = -30
# p3 = -50
# p4 = 3
# a = -1
# b = 1
# n = 10
#
# tracer_courbes(p1, p2, p3, p4, a, b, n)
