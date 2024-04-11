# 1. Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1/x: x∈[1,10]}
# B = {1, 2, 4, 8,…, }
# C = {x: x∈ B i x jest liczbą podzielną przez 4}

A = [1/x for x in range(1, 11)]
B = [2**i for i in range(4)]
C = [i for i in B if i%4==0]

# 2. Wygeneruj macierz (lista dwupoziomowa) losowych wartości (sprawdź pakiet random) 4x4 i wykorzystując Python comprehension zdefiniuj listę, która będzie zawierała tylko elementy znajdujące się na głównej przekątnej.

import random
import numpy as np

D = [random.randint(1, 100) for i in range(16)]
D = np.reshape(D, (4, 4))
E = [D[i][j] for i in range(4) for j in range(4) if i == j]

# 3. Napisz wyrażenie generujące, które będzie zwracało krotkę dwuwartościową postaci: ('Ala', [65, 108, 97]), ('ma', [109, 97]), ('kota.', [107, 111, 116, 97, 46]) dla przykładowego zdania Ala ma kota. 
# Dla każdego wyrazu z tekstu przekazanego jako argument wejściowy tego wyrażenia zwraca ten wyraz oraz listę wartości int odpowiadającą kodowi tego znaku z tablicy znaków (zobacz wbudowane ord(), chr()).

sentence = 'Ala ma kota'
F = ((word, [ord(char) for char in word]) for word in sentence.split())
for item in F:
    print(item)

# 4. Dodaj do funkcji z listingu 8 type hinting.
import math
from typing import Union, Tuple

def row_kwadratowe(a: float, b: float, c: float) -> Union[float, Tuple[float, float], int]:
    delta = b**2 - 4 * a * c
    if delta < 0:
        # brak pierwiastków
        return -1
    elif delta == 0:
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

# 5. Napisz funkcję, która:
# przyjmuje z klawiatury n, będące liczbą całkowitą
# wykonuje n rzutów kostką k6 i zwraca listę krotek wartości postaci ('oczka: 6', 'rzutów: i') itd., gdzie zmienna i jest ilością rzutów dla tej liczby oczek. Dodaj odpowiedni type hinting.

import random
def toss(n: int):
    sum = 0
    for i in range(n):
        sum += random.randint(1, 7)
    x = 'oczka: ' + str(sum)
    y = 'rzutów: ' + str(n)
    return (x, y)

result = toss(5)
print(result)

# 6. Wykorzystując poprzedni przykład z listingu 11 zdefiniuj funkcję, która będzie przyjmowała obiekty typu str jako wejście (dowolną liczbę), a będzie zwracała listę tych łańcuchów posortowaną alfabetycznie.

def sort_words(*words: str) -> list:
    return sorted(words)

print(sort_words('lama', 'bal', 'arka', 'papaj'))

# 7. Napisz funkcję, która przyjmuje nieokreśloną liczbę wartości z kluczem. Funkcja przyjmuje argumenty w postaci: klucz to nazwa drużyny a wartość to ilość punktów, które drużyna zdobyła. Funkcja zlicza, ile jest wszystkich punktów razem i zwraca tę wartość.

def sum_of_points(**teams_points) -> int:
    total_points = sum(teams_points.values())
    return total_points

points = sum_of_points(Liverpool=85, Manchester_City=83, Chelsea=77, Manchester_United=74)
print("Total points:", points)
