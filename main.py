# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Intégrale numérique
# ================================================================================================

# Importation des modules

import numpy as np
import matplotlib.pyplot as plt
from math import *
import timeit
import time


# ================================================================================================
# FONCTION QUI DEMANDE LES COEFFICIENTS DU POLYNOME
def entrees_utilisateurs():
    print("Le polynôme est de la forme p1 + p2 * x + p3 * x^2 + p4 * x^3.")
    while True:
        try:
            constantes = input("Veuillez rentrer les constantes de votre polynôme p1, p2, p3, p4 séparées par des "
                               "virgules et sans espaces:\n")
            liste_constantes = constantes.split(',')

            if len(liste_constantes) == 4:
                p1 = float(liste_constantes[0])
                p2 = float(liste_constantes[1])
                p3 = float(liste_constantes[2])
                p4 = float(liste_constantes[3])
                break
        except ValueError:
            print("Le format n'est pas bon, rentrez vos constantes en chiffre.")

    while True:
        try:
            intervalle = input(
                "Veuillez donner les bornes d'intégration a et b séparées par une virgule et sans espaces:\n")
            liste_intervalle = intervalle.split(',')
            a = float(liste_intervalle[0])
            b = float(liste_intervalle[1])

            if len(liste_intervalle) == 2 and b > a:
                break

            # Permet que 'a' soit la borne inférieure et 'b' la borne supérieure si l'utilisateur a inversée.
            elif len(liste_intervalle) == 2 and b < a:
                c = b
                b = a
                a = c
                break
        except ValueError:
            print("Le format n'est pas bon. Veuillez réessayer.")

    while True:
        print(
            "Il existe 3 méthodes pour calculer votre intrégrale : la méthode des rectangles, la méthode des trapèzes "
            "et la méthodes de Simpson.")
        methode = input("Veuillez rentrer le nom de la méthode (trapezes, simpson ou rectangles):\n")

        if methode in ['trapezes', 'rectangles', 'simpson']:
            break
        else:
            print("Rentrée invalide. Veuillez réessayer.")

    while True:
        try:
            nombre_segments = int(input("Veuillez rentrer le nombre de segments que vous voulez utiliser:\n"))
            if nombre_segments > 0 and isinstance(nombre_segments, int):
                break
        except ValueError:
            print("Le format n'est pas bon. "
                  "Veuillez entrer un nombre entier et supérieur à 0.")

    return p1, p2, p3, p4, a, b, methode, nombre_segments


# ================================================================================================
# FONCTION PRINCIPALE
def integration_numerique():
    print("****************************************************************************** "
          "\nTu t'apprêtes à utiliser un code pour réaliser une intégrale numérique d'un polynôme de degré 3"
          "\n******************************************************************************")
    print("\n")


p1, p2, p3, p4, a, b, methode, nombre_segments = entrees_utilisateurs()
print(p1, p2, p3, p4, a, b, methode, nombre_segments)

# if methode == 'simpson':
# methode simpson
# elif methode == 'trapeze':
# methode trapeze
# elif methode == 'rectangle':
