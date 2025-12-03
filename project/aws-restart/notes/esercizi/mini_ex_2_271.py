# Mini_ex_2_271

def richiedi_intero(messaggio):
    """Richiede un numero intero, ripetendo finché l'input non è valido"""
    while True:
        valore = input(messaggio)
        if valore.lstrip("-").isdigit():
            return int(valore)
        print("Errore: inserisci un numero intero valido!")


def richiedi_intero_positivo(messaggio):
    """Richiede un numero intero positivo, ripetendo finché l'input non è valido"""
    while True:
        valore = input(messaggio)
        if valore.isdigit() and int(valore) > 0:
            return int(valore)
        print("Errore: inserisci un numero intero positivo!")


def stampa_tabellina(numero):
    """Stampa la tabellina del numero passato come parametro"""
    print(f"\nTabellina del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def disegna_rettangolo_intero(larghezza, altezza):
    """Disegna un rettangolo pieno di asterischi *"""
    print(f"\nRettangolo intero {larghezza} x {altezza}:")
    for _ in range(altezza):
        print("*" * larghezza)


def disegna_rettangolo_perimetro(larghezza, altezza):
    """Disegna solo il perimetro del rettangolo con asterischi *"""
    print(f"\n Perimetro rettangolo {larghezza} x {altezza}:")
    for r in range(altezza):
        for c in range(larghezza):
            if r == 0 or r == altezza - 1 or c == 0 or c == larghezza - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# ==============================
# (MENU)
# ==============================

while True:
    print("\nBenvenuto! Cosa vuoi fare?")
    print("1. Stampa Tabellina")
    print("2. Disegna un rettangolo intero")
    print("3. Disegna il perimetro di un rettangolo")
    print("4. Esci")

    scelta = richiedi_intero("Scegli un'opzione (1-4): ")

    if scelta == 1:
        numero = richiedi_intero("Inserisci un numero: ")
        stampa_tabellina(numero)

    elif scelta == 2:
        w = richiedi_intero_positivo("Larghezza: ")
        h = richiedi_intero_positivo("Altezza: ")
        disegna_rettangolo_intero(w, h)

    elif scelta == 3:
        w = richiedi_intero_positivo("Larghezza: ")
        h = richiedi_intero_positivo("Altezza: ")
        disegna_rettangolo_perimetro(w, h)

    elif scelta == 4:
        print("Au Revoir!")
        break

    else:
        print("Ritenta.")
