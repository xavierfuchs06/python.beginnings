import random                                                           #Importiert den Benötigten Zufallsgenerator
t = 0                                                                   #Anzahl der Versuche, beim Start natürlich 0

c = int(random.uniform(0, 100))                                         #Speichere die Generierte Zahl, als integer in Variable c
print('Errate die Zahl die Zwischen 1 und 100')                         #Aufgabe
u = int(input())                                                        #Nehme die Antwort des Spielers und speicher sie in Variable u


while u != c:                                                           #Solange Antwort des Spielers nicht die Generierte Zahl ist
    u = int(input())                                                    #Frage nach Antwort des Spielers
    if u-1 != int():                                                    #Ist die Eingabe des Spielers Invalid z.B. -1 oder 101
        t=t+1                                                           #Addiere 1 zu Aktuellen Versuchen
        print('Invalide Eingabe, Zahl zwischen 1 und 100')              #Anmerkung zur invaliden Eingabe
    
    if u > c:                                                           #Ist die Antwort des Spielers kleiner als die Generierte Zahl
        t = t+1                                                         #Addiere 1 zu Aktuellen Versuchen
        print('Die zu erratene Zahl ist kleiner als die angegebene')    #Anmerkung zur Flascheingabe und Tipp
       

    if u < c:                                                           #Ist die Antwort des Spielers größer als die Generierte Zahl
        t = t+1                                                         #Addiere 1 zu Aktuellen Versuchen
        print('Die zu erratene Zahl ist größer als die angegebene')     #Anmerkung zur Flascheingabe und Tipp
        

if u == c:                                                              #Ist die Antwort des Spielers identisch zur Generierten Zahl
    t = t+1                                                             #Addiere 1 zu Aktuellen Versuchen
    print('Richtig, du hast die Zahl in',t,'Versuchen erraten')         #Gratuliere und nenne die Versuche t
    
    
