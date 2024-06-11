## Projet B: analyse numérique

### BUT:
Ce programme permet de comparer 3 méthodes d'intégration par calcul de l'aire sous la courbe:
- méthode des rectangles
- méthode des trapèzes
- méthode de Simpson

L'objectif est de les comparer en affichant des graphiques de convergence (erreur) et de temps de calcul de chaque méthode.

Pour notre étude, nous prenons une **fonction polynomiale** de la forme:

  ![image](https://github.com/AdrienHuyghebaert/projet_integration_numerique/assets/169942081/654b8fee-6655-4ea6-982c-0fd8e81a14a9)


### Structure du code:

Pour chaque méthode, on compare un code en **python classique** et un avec la **librairie numpy**. Pour les deux dernières méthodes, on les compare également avec les fonctions déjà implémentées de **scipy** qui permettent le calcul d'intégrales. 
Chaque méthode est implémentée dans un fichier python séparé portant le même nom.
Le fichier .main contient le programme principal qui appelle les autres fichiers et trace les courbes de comparaison des 3 méthodes. 
Le temps de calcul est donné par la fonction ***perf counter*** du package time. Nous utilisons une régression linéaire pour afficher le temps de calcul dans un souci de clarté des graphiques.

### Méthode des rectangles










### Méthode des trapèzes

Le fichier contient les fonctions suivantes:

- fonction_polynomiale(): calcule f(x) selon les coefficients donnés
- integrale_exacte(): calcule l'aire exacte par intégration de la fonction entre a et b
- methodes_trapezes_python(): calcule l'aire avec la méthode des trapèzes en pyhton simple, la formule mathématique est la suivante:
  
  ![image](https://github.com/AdrienHuyghebaert/projet_integration_numerique/assets/169942081/9cd38ec2-e26c-47b5-85b7-38b39f7c7732)

- methodes_trapezes_numpy(): calcule l'aire avec la méthode des trapèzes avec vectorisation du code 
- aire_trapeze_scipy(): calculer l'aire sous la courbe à partir de la fonction ***trapezoid*** du package integrate de **scipy**
- calcul_convergence_temps_scipy(): renvoie le tableau des temps de calcul de scipy et le tableau des différences avec l'aire exacte (erreurs) pour n variant de 1 à 1000
- tracer_convergence_temps_scipy(): trace les courbes avec les données de la fonction ci-dessus
- tracer_graphique_trapeze(): trace les courbes de la méthode des trapèzes pour pyhton et numpy (n fixé) et renvoie la valeur de l'aire sous la courbe 
- calculer_temps_convergence(): renvoie un tableau des différences maximales des ordonnées pour chaque valeur de segment n et un tableau des temps calculés
- tracer_convergence_temps_python_numpy(): trace les courbes de la fonction précédente

  

### Méthode de Simpson

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

### Le fichier .main

Il contient les fonctions suivantes:

- comparer_temps_calcul(): affiche le graphique des tracés linéaires des temps de calcul pour les 3 méthodes
- comparer_convergence(): affiche le graphique des tracés de la convergence pour les 3 méthodes
- comparer_scipy(): affiche les graphiques des tracés de la convergence et du temps de calcul avec scipy pour les méthodes des trapèzes et de simpson




