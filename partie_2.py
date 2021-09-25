# Initialisation des variables 
capital = 2600 # en dollars
pas_de_frais = 0.045# intérêts /100
frais_fixe = [60,0.10]# [frais initials,intérêts /100]
jours_par_an = 365# en jours
# Calcul du montant du capital avec le premier placement au 100ème jour de l'année 
Capital_1_100_jours = capital + capital*(pas_de_frais/jours_par_an)*100
# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année 
Capital_2_300_jours = capital + frais_fixe[0] + capital*(frais_fixe[1]/jours_par_an)*300
# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier
interets1 = 0
interets2 = -frais_fixe[0]
jours = 1
while interets1 >= interets2:

    interets1 += capital * pas_de_frais / jours_par_an
    interets2 += capital * frais_fixe[1] / jours_par_an
    jours+=1


# Affichage des valeurs calculées
phrase1 = f" Le montant du capital avec le premier placement après 100 jours: {Capital_1_100_jours:.2f}"
phrase2 = f" Le montant du capital avec le deuxième placement après 300 jours: {Capital_2_300_jours:.2f}"
phrase3 = f" Le placement à frais fixe devient l'option la plus profitable après {jours:} jours"
print(phrase1,phrase2,phrase3,sep='\n')