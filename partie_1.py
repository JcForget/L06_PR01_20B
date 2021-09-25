# Initialisation des variables 

capital = 8000 # en dollars
nb_jours = 72 # en jours
taux_annuel = 0.065# pourcentage / 100
jour_annee = 365# jour par année


# Calcul du taux périodique 
taux_periodique = taux_annuel/365

# Calcul des intérêts 
interet = capital * nb_jours * taux_periodique

# Calcul de la valeur acquise
valeur_acquise = capital + interet

# Affichage des interets et de la valeur acquise 
print(f"\n Les intérêts gagnés après 72 jours sont : {interet:.2f} \n La valeur acquise après 72 jours est : {valeur_acquise:.2f} \n")
