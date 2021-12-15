import time
import os
import random

def hatvanyozas(alap: int, kitevo: int) -> int:
    eredmeny = 1
    for x in range(kitevo):
        eredmeny *= alap
    return eredmeny

def kilepes():
    for x in range(3):
        print(f'{x + 1}')
        time.sleep(1)
    print('viszont látásra!')
    time.sleep(2)
    os.system('cls')

def osszeadas(a, b):
    return a + b

# paraméterként megkapja:
# mekkora legyen a lista hossza
# mettől meddig töltse fel véletlen számokkal
# visszatér a véletlen számokkal feltöltött listával

def randomlista(hossz: int, tol: int, ig: int) -> list:
    lista = []
    for x in range(hossz):
        lista.append(random.randint(tol, ig))
    return lista