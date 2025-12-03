import sys

print('====================================')
print('START PROGRAM')
print('====================================')

# per vedere l'indirizzo di un oggetto usiamo il metodo id()
# può essere usato per identificare l'indirizzo referenziato da una variabile (tag) - id(a)
# può essere usato per identificare l'indirizzo dell'oggetto stesso - id(20)

# per vedere il reference count usiamo sys.getrefcount()
# il reference count indica quante variabili puntano allo stesso oggetto
# nota: getrefcount() restituisce sempre +1 perché crea un riferimento temporaneo

# tre variabili vengono create con valori interi
a: int = 320
print(f"id(a) = {id(a)}")  # stampa l'indirizzo di memoria dell'oggetto 20
print(f"refcount(a) = {sys.getrefcount(a)}")  # il reference count sarà alto perché 20 è usato internamente da Python

b: int = a
print(f"id(b) = {id(b)}")  # b punta allo stesso oggetto di a, quindi stesso id
print(f"refcount(b) = {sys.getrefcount(b)}")  # il reference count aumenta perché ora b punta allo stesso oggetto

c: int = 320
print(f"id(c) = {id(c)}")  # anche c punta allo stesso oggetto 20, grazie all'integer interning di Python
print(f"refcount(c) = {sys.getrefcount(c)}")  # il reference count aumenta ancora

print('------------------------------------')

# riassegniamo a ad un nuovo valore
a = 2
print(f"id(a) = {id(a)}")  # ora a punta ad un oggetto diverso (2), quindi id diverso
print(f"refcount(a) = {sys.getrefcount(a)}")  # reference count dell'oggetto 2

# riassegniamo b al nuovo valore di a
b = a
print(f"id(b) = {id(b)}")  # b ora punta allo stesso oggetto di a (2)
print(f"refcount(b) = {sys.getrefcount(b)}")  # il reference count di 2 aumenta

print(f"id(c) = {id(c)}")  # c non è cambiato, punta ancora all'oggetto 20
print(f"refcount(c) = {sys.getrefcount(c)}")  # il reference count di 20 è diminuito perché a e b non lo puntano più
