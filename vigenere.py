"""Test pour coder selon la méthode Vigenere
Fichier : vigenere.py
URL : https://www.apprendre-en-ligne.net/crypto/python/vigenere/index.html
Dans PyCharm CTRL-MAJ-F10 ou clic droit sur l'onglet pour un run de ce fichier vigenere.py
"""


# crypte un texte avec le chiffre de Vigenere


def lettre(c):
    # retourne vrai si c est une lettre non accentuee
    car = ord(c.upper())
    return 64 < car < 91


def decalage(c, k):
    # decale une lettre majuscule. Les autres caracteres ne sont pas modifies
    car = ord(c.upper())
    if lettre(c):
        car += k
        while car > 90:
            car -= 26
        while car < 65:
            car += 26
        return chr(car)
    else:
        return ""


def vigenere(message, cle, crypte):
    # effectue le decalage en fonction de la cle sur les caracteres de message
    n = 0
    chiffre = ''
    for c in message:
        if lettre(c):
            k = ord(cle[n % len(cle)]) - 65
            if crypte:
                chiffre += decalage(c, k)
            else:
                chiffre += decalage(c, -k)
            n += 1
        else:
            chiffre += c
    return chiffre


# tests
cle = "JULIUS"
texte = "Ave Caesar morituri te salutant"
texte_code = vigenere(texte, cle, True)
print(texte_code)
texte_decode = vigenere(texte_code, cle, False)
print(texte_decode)
