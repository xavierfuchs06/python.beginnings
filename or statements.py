setpw=1

print("Wie heißt du?")
name=input()
print('Guten Tag, '+ name)

print("Passwort?")
userpw=input()
if setpw==userpw:
    print('Wilkommen')
if setpw!=userpw:
    print('Passwort falsch')


