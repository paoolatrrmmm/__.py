def blocco_1(nome: str) -> None:
    print("=" * 40)
    print(f"BENVENUTO {nome} NEL SISTEMA")
    print("=" * 40)


def stampa_divisore(simbolo: str, coefficiente: int) -> str:
    return f"{simbolo}" * coefficiente


def stampa_frase_con_divisore(frase: str) -> str:
    divisore: str = stampa_divisore("*", 100)
    return f"{divisore}\n{frase}\n{divisore}"


def restituisce_frase_con_nome(nome: str) -> str:
    return f"BENVENUTO {nome} NEL SISTEMA"


risultato = stampa_frase_con_divisore("BENVENUTO {nome} NEL SISTEMA")
print(risultato)



