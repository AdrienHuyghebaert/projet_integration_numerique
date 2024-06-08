# ================================================================================================
# Auteur: Groupe
# Date: 5 juin 2024
# Intégrale numérique
# ================================================================================================

# Importation des modules

import numpy as np
import matplotlib.pyplot as plt
import methode_rectangles


# ================================================================================================
# Fonction qui demande les informations pour réaliser le calcul (coefficients, bornes d'intégration, nombre de segments)
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

            # Permet que 'a' soit la borne inférieure et 'b' la borne supérieure si l'utilisateur a inversé.
            elif len(liste_intervalle) == 2 and b < a:
                c = b
                b = a
                a = c
                break
        except ValueError:
            print("Le format n'est pas bon. Veuillez réessayer.")

    while True:
        try:
            nb_segments = int(input("Veuillez rentrer le nombre de segments que vous voulez utiliser:\n"))
            if nb_segments > 0 and isinstance(nb_segments, int):
                break
        except ValueError:
            print("Le format n'est pas bon. "
                  "Veuillez entrer un nombre entier et supérieur à 0.")

    return p1, p2, p3, p4, a, b, nb_segments


# ================================================================================================
# Fonction pour réaliser le calcul analytique
def calculer_solution_analytique(a, b, p1, p2, p3, p4):
    x = np.linspace(a, b, 10)
    y = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)
    aire_totale = ((p1 * b + (p2 / 2) * b ** 2 + (p3 / 3) * b ** 3 + (p4 / 4) * b ** 4)
                   - (p1 * a + (p2 / 2) * a ** 2 + (p3 / 3) * a ** 3 + (p4 / 4) * a ** 4))

    return x, y, aire_totale


# ================================================================================================
# Fonction pour afficher les courbes
def afficher_courbes(pas, x_py_rect, y_py_rect, x_np_rect, y_np_rect, x_ana, y_ana):
    plt.bar(x_py_rect, y_py_rect, width=pas, align='edge', alpha=0.3, edgecolor='b')
    plt.bar(x_np_rect, y_np_rect, width=pas, align='edge', alpha=0.3, edgecolor='r')
    plt.plot(x_ana, y_ana, color='black', linestyle='-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title("Méthode des rectangles 'Python' et 'NumPy' et solution analytique")
    plt.show()


# ================================================================================================
# Fonction principale

# Récupération des informations pour réaliser les calculs
p_1, p_2, p_3, p_4, borne_a, borne_b, nombre_segments = entrees_utilisateurs()
pas = (borne_b - borne_a) / nombre_segments  # Création de la variable pas

# Méthodes des rectangles avec Python
x_py_rectangle, y_py_rectangle, aire_totale_py_rectangle = \
    methode_rectangles.methode_des_rectangles_py(borne_a, pas, p_1, p_2, p_3, p_4, nombre_segments)


# Méthode des rectangles avec NumPy
x_np_rectangle, y_np_rectangle, aire_totale_np_rectangle = \
    methode_rectangles.methode_des_rectangles_numpy(borne_a, borne_b, pas, p_1, p_2, p_3, p_4, nombre_segments)

# Résolution analytique
x_analytique, y_analytique, aire_totale_analytique = calculer_solution_analytique(borne_a, borne_b, p_1, p_2, p_3, p_4)

# Affichage des courbes
afficher_courbes(pas, x_py_rectangle, y_py_rectangle, x_np_rectangle, y_np_rectangle, x_analytique, y_analytique)
