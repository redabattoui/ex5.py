ex5.py
def trouver_maximum(liste):
    if not liste:
        return "La liste est vide"

    maximum = liste[0]
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    return maximum