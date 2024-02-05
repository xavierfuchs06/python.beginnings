import string

print("Encrypt or Decrypt?")
choice = input('E or D: ').lower()

if choice == 'e':
        plain_text = input("What is your plain text? ").upper()
        shift = int(input("What is your shift?"))
        shift %= 26     # Loop shift back to beginning if user enters value beyond 26

        alphabet = string.ascii_uppercase       # Define used alphabet as full uppercase ASCII A-Z
        shifted = alphabet[shift:] + alphabet[:shift]   # Start the alphabet by the shifted amount (ex. Ceaser3: ABCD = CDEF), and add the rest of it at the end
        table = str.maketrans(alphabet, shifted)        # Creating a table with the standard and shifted alphabets below eachother, like the ceaser cypher

        encrypted = plain_text.translate(table)         # Puts each character through the cypher table made above, essencially using the encryption

        print("Your encrypted text is: " + encrypted)

if choice == 'd':
        encrypted_text = input("What is your encrypted text? ").upper()
        shift = 26 - int(input("What is the shift used for encryption?"))          # If you shift the encrypted text by the diffenrec betwwen the maximum of 26 and the known cypher, then it will loop it back to being decrypted.
        shift %= 26

        alphabet = string.ascii_uppercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted)

        decrypted = encrypted_text.translate(table)

        print("Your decrypted text is: " + decrypted)


        # Habe den Code  durch YouTube tutorials zusammengeschustert, da ich mich weder mit Python noch mit
        # der Ceaser verschlüsselung gut genug auskenne um dies komplett selbst schreiben zu können.

