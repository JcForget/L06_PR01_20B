# Initilisation des variables 
capital = 300000
taux_interet = 0.08
jours_par_annee = 365
nombre_annee = 20
annee = 1

# Calcul du capital au bout de 20 années 
while annee < nombre_annee:
    capital += capital * taux_interet
    annee += 1


# Affichage du capital au bout de 20 années
print(f"\n Après 20 ans, le capital sera de {capital:.2f} dollars")