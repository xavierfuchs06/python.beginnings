### --------------- Berechnung des Gesamtbremsweges -------------- #####


v = int(input('Gib die Geschwindigkeit in km/h an.' ))              # Abfrage der Geschwindigkeit 
reaktionsweg = (v/10)*3                                 # Berechnung des Reaktionsweg
bremsweg = (v/10)*(v/10)                                # Berechnung des Bremsweg
gesamtweg = reaktionsweg + bremsweg
notbremsung = reaktionsweg + bremsweg/2
print(' Der Reaktionsweg sind: ',reaktionsweg ,'m. Der Bremsweg : ', bremsweg ,'m. Der Gesamtbremsweg: ', bremsweg+reaktionsweg,'m.')
print(' Bei einer Notbremsung beträgt der Bremsweg: ', reaktionsweg+bremsweg/2,'m.')
