# Projet 1 - Préparez vos placements financiers

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimache 3 octobre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200928T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif
Concevoir et implémenter un programme permettant de calculer le rendement de différents investissements selon différentes situations. Les fichiers `interet_simple.py`, `interet_compose.py`,  et `heritage.py` seront à compléter.

## Partie 1 : Interet simple
À faire : compléter le fichier `interet_simple.py`

on place un capital de 5 000 $ pendant 89 jours au taux annuel de 8.5%. Calculer l’intérêt et la valeur acquise à l’issue du placement. On utilise la formule uivante:
<img src="https://render.githubusercontent.com/render/math?math=I=Ctn">

- ***I*** : intérêt
- ***C*** : capital placé
- ***t*** : taux journalier (**taux annuel / 365**)
- ***n*** : nombre de jours

Enfin:  **Valeur acquise = Capital + Intérêts**


Exemple d'affichage : 
![Formules de section](data/formules_sections.png)

## Partie 2 :  Comparer deux placements à intérêts simples
À faire : compléter le fichier `interet_compose.py`

On possède un capital de 2600$. Votre banquier vous propose deux types de placement :
<img src="https://render.githubusercontent.com/render/math?math=I=Ctn">

- Pas de frais avec un taux annuel à 4,5 %
- 60$ de frais fixe qui sont prélevés du capital mais avec un taux annuel de 10%
1) Calculez le montant de votre capital avec le premier placement au 100ème jour de l'année
2) Calculez le montant de votre capital avec le deuxième placement au 300ème jour de l'année 
3) Au bout de combien de jours le deuxième placement vous rapportera plus que le premier ?

Remarque : La formule pour calculer la valeur de votre capital est :
<img src="https://render.githubusercontent.com/render/math?math= C = capital_initial + capital_initial*(taux/365)*nb_jours">

Exemple d'affichage : 
![Formules de section](data/formules_sections.png)

La déformation maximale de la poutre est 42.24 mm
```

## Partie 2 : Optimisation de contraintes
À faire : compléter le fichier `poutre_section.py`

Concevoir un programme qui permet, considérant les données d'entrée fournies dans le fichier, d'afficher le type de section minimisant la déformation maximale de la poutre.

Votre programme doit afficher la réponse suivant une nomenclature précise :
```
Le type de section minimisant la déformation maximale est <section>, avec une déformation de <delta_max> mm
```
où :
- <section> est le type de section, pouvant prendre les valeurs : `rectangulaire`, `carrée`, `ronde`et `creuse`.
- <delta_max> est la déformation maximale correspondant à ce type de section, arrondi avec deux décimales.

Exemple d'affichage :

```
Le type de section minimisant la déformation maximale est ronde, avec une déformation de 20.07 mm
```

Pour résoudre cet exercice, vous devez utiliser des structures de contrôles.

## Ressources
### Calcul de la déformation maximale
Afin de résoudre ce problème, nous pouvons utiliser des formules connues en résistance des matériaux permettant de calculer la flèche maximale, ainsi que la déformée de la poutre.

La formule de la déformation maximale pour une poutre encastrée est:

![Equation](data/equation.png)

où:

- F est la force appliquée 
- E est le module de Young
- I est le moment quadratique de la section (appelé *inertie* dans les sources)
- L est la longueur de la poutre

### Calcul du moment quadratique de la section

Le tableau suivant présente les formules permettant de calculer le moment quadratique de la poutre en fonction de son type de section (rectangulaire, carré, rond, creux) et de ses paramètres.

![Formules de section](data/formules_sections.png)
