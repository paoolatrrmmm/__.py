#  Quiz_boycottimenti

# Funzione quiz
def esegui_quiz():
    print("\n--- QUIZ: Linguaggio Preferito ---")
    print("Qual è il tuo linguaggio di programmazione preferito?")
    print("1. Python")
    print("2. JavaScript")
    print("3. Java")
    print("4. C++")

    try:
        risposta = int(input("Inserisci un numero da 1 a 4: "))
    except ValueError:
        print("Errore: devi inserire un numero!")
        return  # Torna al menù

    if risposta == 1:
        print("Spumeggiante!")
    elif risposta == 2:
        print("Interessante..")
    elif risposta == 3:
        print("Quindi.. non Python?")
    elif risposta == 4:
        print("I nerd apprezzano!")
    else:
        print("Ritenta: avevamo detto che dovevi scegliere un'opzione tra 1 e 4!")


# 0) Menù
def mostra_menu():
    print("\n====== MENU ======")
    print("1. Avvia il Quiz")
    print("2. Esci")
    print("=================")


# 1) Control Flow
while True:
    mostra_menu()

    try:
        scelta = int(input("Aspetto tue: "))
    except ValueError:
        print("Ritenta: avevamo detto che dovevi scegliere un'opzione tra 1 e 4!")
        continue

    if scelta == 1:
        esegui_quiz()
    elif scelta == 2:
        print("Au revoir!")
        break
    else:
        print("Ritenta: avevamo detto che dovevi scegliere un'opzione tra 1 e 4!")

