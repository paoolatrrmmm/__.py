# laundry_check
# una domanda / quattro risposte multiple visibili

# Yuri  si è riscoperto ambientalista e vuole mettere su un eco-bucato
# question_1 : str = "Quali sono le misure migliori da adottare per un bucato sostenibile?"
# answer_1 : str = "A. Mezzo carico is the way, lavare spesso e poco"
# answer_2 : str = "B. Non aspettare di separere i capi:mixare è bello"
# answer_3 : str = "C. Aspettare di avere un carico completo"
# answer_4 : str = "D. Lavaggi > 30°"

# print(f"""
# {question_1}
#       A. {answer_1}
#       B. {answer_2}
#       C. {answer_3}
#      D. {answer_4}
# """)

# answer: str = input("Inserisci la tua risposta preferita:")

# answer.tmp = answer.upper()

# match answer_tmp:
#       case "A":
#        result = f la risposta è : {"Ottima scelta, suppungo sia dettata da uno stile di vita frenetico. Però ritenta!"}

# match answer_tmp:
#       case "B":
#        result = f ("Si sta pensando di mettere su il bucato o il frullato? \n Ritenta!")

# match answer_tmp:
#       case "C":
#        result  = f ("E - S - A - T - T - O! Obvs, separando tessuti&colori! Ma lo sai già, no?")

# match answer_tmp:
#       case "C":
#        result  = f ("Se si tratta di lenzuola, asciugamani, intimo non delicato, capi molto sporchi - già sottoposti ad un lavaggio a mano di pre-trattamento finito male - Sì! Per tutti gli altri casì: Non lo so Rick, questa cosa non mi convince! \n Ritenta")

# while False:
#    print("Non mi sembrava una domanda a risposta aperta, però potrei essermi tranquillamente sbagliata io. Seleziona 1 delle quattro risposte proposte!")
#    scelta = input ("Inserisci la tua scelta (1-4):")
question_1 = "Quali sono le misure migliori da adottare per un bucato sostenibile?"

answer_1 == "A. Mezzo carico is the way, lavare spesso e poco"
answer_2 == "B. Non aspettare di separare i capi: mixare è bello"
answer_3 == "C. Aspettare di avere un carico completo"
answer_4 == "D. Lavaggi > 30°"

print(f"""
{question_1}
A. {answer_1}
B. {answer_2}
C. {answer_3}
D. {answer_4}
""")

answer = input("Inserisci la tua risposta preferita (A-D): ").upper()
while answer not in ("A", "B", "C", "D"):
    print(
        "Non mi sembrava una domanda a risposta aperta. Seleziona una delle quattro risposte proposte"
    )
    break

if answer is ("A"):
    print(
        "Ottima scelta, suppongo sia dettata da uno stile di vita frenetico. Però ritenta!"
    )
    break

elif answer is ("B"):
    print("Stai pensando di mettere su il bucato o il frullato? Ritenta!")
    break

elif answer is ("C"):
    print("ESATTO! Ovviamente separando tessuti & colori!")
    break

elif answer is ("D"):
    print("Solo per alcuni capi molto sporchi o resistenti. Ritenta!")
    break
