# Tipi
num: int = 2

num_f: float = 2.8

num_str: str = "2.8"

booleano: bool = False

# Stampo Int
print(type(num))

# Stampo float
print(type(num_f))

# Stampo Stringa
print(type(num_str))

# Stampo booleano
print(type(booleano))

# come viene compilato un programma python
# 1. file.py → compilatore
# 2. bytecode → pvm

# come viene compilato un programma python
# 1. file.py → compilatore
# 2. bytecode → pvm

# come funziona la memoria
# 1. due spazi di memoria principali
#    1.1 stack
#    1.2 heap

import sys

a: int = 500
b: int = a
print(sys.getrefcount(500))

# todo :
## indagare sul perchè riporta cinque
### getrefcount() non mostra soltanto le nostre variabili, ma anche i riferimenti temporanei creati

print(sys.version)
# print(sys.platform)

# print(dir(sys))
# print(help(sys))

from psutil import cpu_stats

# print(dir(psutil))

print(cpu_stats())

## funzioni buil in
none: str = "Pippo"

print(len(none))

int_val: int = 3

print(type(int_val))

print(type(float(int_val)))

float_val: float = float(int_val)

print(type(float_val))

str_val: str = "30"
print(type(int(str_val)))

# help(input)

codice: str = input("Inserire codice di tre cifre dietro la carta:")
print(type(codice))
