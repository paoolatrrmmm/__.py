# Control flow'n'Return

# Funzione per controllare se un numero è pari
def restituisce_numero_pari(numero):
    # Se il resto della divisione per 2 è 0 → numero pari
    if numero % 2 == 0:
        return True
    else:
        return False


# Funzione per applicare uno sconto in base all'età
def calcola_sconto(prezzo, età):
    if età < 18:
        return prezzo * 0.8  # sconto 20%
    elif età >= 65:
        return prezzo * 0.7  # sconto 30%
    else:
        return prezzo  # nessuno sconto


# Funzione per valutare la temperatura
def valuta_temperatura(gradi):
    if gradi < 15:
        return "Freddo"
    elif gradi <= 25:
        return "Mite"
    else:
        return "Caldo"


# --------------- Programma Interattivo ---------------

# INPUT con gestione degli errori tramite "ciclo while"
while True:
# Numero pari + controllo errore / tramite "try 'n' except"
    try:
        numero = int(input("Inserisci un numero intero: "))
        break
    except ValueError:
        print("Errore! Devi inserire un numero intero. Riprova.")

print("Pari?", restituisce_numero_pari(numero))


# Input per prezzo con controllo errori
while True:
    try:
        prezzo = float(input("Inserisci il prezzo: "))
        break
    except ValueError:
        print("Errore! Devi inserire un numero. Esempio: 99.50")


# Input per età con controllo errore
while True:
    try:
        età = int(input("Inserisci l'età: "))
        break
    except ValueError:
        print("Errore! Devi inserire un numero intero.")


# Mostra prezzo finale
print("Prezzo scontato:", calcola_sconto(prezzo, età))


# Input per temperatura con controllo errori
while True:
    try:
        temperatura = float(input("Inserisci la temperatura: "))
        break
    except ValueError:
        print("Errore! Inserisci un numero valido.")


# Mostra risultato finale
print("Valutazione temperatura:", valuta_temperatura(temperatura))

# -----------------------------------------------------
print("\nGrazie per aver utilizzato il programma!")
