### BUT:
Ce programme permet de comparer 3 méthode d'intégration apr calcul de l'aire sous la courbe:
- méthode des rectangles
- méthode des trapèzes
- méthode de Simpson

### Structure du code:

Pour chaque méthode, on compare un code en python classique et un avec la librairie numpy. Pour les deux dernières méthodes, on les compare également avec les fonctions déjà implémentées de scipy qui permettent le calcul d'intégrales. 
Chaque méthode est implémentée dans un fichier python séparé portant le même nom.
Le fichier .main contient le programme principal qui appelle les autres fichiers.

### Utilisation du code:


**Méthode de Simpson**

On utilise la formule de Simpson pour calculer l'aire sous la courbe sur le segment [a, b]: 
![image](https://github.com/AdrienHuyghebaert/projet_integration_numerique/assets/169941933/09cd9718-b0d8-421d-a769-b6a9c3b6d471)

Pour cela on utilise 3 fonctions : 

**formule_simpson()**

Cette fonction prend en entrée les points du segment de la subdivision [a, b] et calcul l'aire sous la courbe selon la formule de Simpson. 

**La fonction fait appel à la fonction de la formule à intégrer pour calculer les valeurs de l'évalutation de la fonction en a, b et (a+b)/2**

- *Entrées :p1, p2, p3, p4, a, b*
- *Sorties : valeur de l'aire sous la courbe pour l'interval*

**calcul_integrale_simpson()**
Discrétise le segment donné par l'utilisateur selon le nombre de points fournis et renvoie la valeur de l'aire sous la courbe, ainsi que les points x, y associés à la courbe.

**La fonction fait appel à la fonction de la formule_simpson()**

- *Entrées :p1, p2, p3, p4, a, b, n*
- *Sorties : valeur de l'aire sous la courbe, points x/y*

**fctio()**

Cette fonction évalue la fonction avec les paramètres définis pas l'utilisateur au point x donné. 

- *Entrées :p1, p2, p3, p4, x*
- *Sorties : point y*

**tracer_courbes()**

Trace les courbes de la méthode Simpson pour la version simple et la version vectorisée. 

*Une fonction permet également d'obtenir la valeur calculée selon un module Scipy : **calcul_integrale_simpson_scipy()***


**Méthode des trapèzes**

Le fichier contient les fonctions suivantes:

- fonction_polynomiale(p1, p2, p3, p4, x):
- integrale_exacte(p1, p2, p3, p4, a, b):
- methodes_trapezes_python(a, b, n, p1, p2, p3, p4):
- methodes_trapezes_numpy(a, b, n, p1, p2, p3, p4):
- aire_trapeze_scipy(a, b, n, p1, p2, p3, p4):
- calcul_convergence_temps_scipy(a, b, p1, p2, p3, p4, n):
- tracer_convergence_temps_scipy(a, b, p1, p2, p3, p4, n):
- tracer_graphique_trapeze(a, b, n, p1, p2, p3, p4):
- calculer_temps_convergence(p1, p2, p3, p4, a, b, n):
- tracer_convergence_temps_python_numpy(p1, p2, p3, p4, a, b, n):
