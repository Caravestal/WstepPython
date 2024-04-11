# 1. Napisz pętlę, która wyświetla liczby podzielne przez 5 z zakresu [0,50].

for i in range(51):
    if i%5 == 0:
        print(i)

# 2. Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9, ale tylko nieparzysta wysokość.

def draw_diamond(height):
    
    for i in range(1, height + 1, 2):
        print(" " * ((height - i) // 2) + "o" * i)
    
    for i in range(height - 2, 0, -2):
        print(" " * ((height - i) // 2) + "o" * i)

height = int(input("Give odd height of the diamond (3 to 9): "))
draw_diamond(height)

# 3. Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100 w formie tabeli, z wyrównaniem liczb do strony prawej, nagłówkiem kolumn i wierszy.

import pandas as pd
first_number = []
second_number = []
result = []

for i in range(1, 11):
    for j in range(1, 11):
        first_number.append(i)
        second_number.append(j)
        result.append(i*j)
        
df = pd.DataFrame({'First number': first_number, 'Second number': second_number, 'Result': result})
print(df)

# 4. Pobieraj z klawiatury wartość w postaci liczby całkowitej, a następnie wyświetl ją w postaci liczby binarnej, ósemkowej i szesnastkowej.

number = input("Print an integer: ")

try:
    number = int(number)
except:
    print('Input is not an integer')
    
print('1: ', bin(number), ' 8: ', oct(number), ' 16: ', hex(number))

# 6. Napisz skrypt, który pobiera od użytkownika wartość liczbową, a następnie wyświetla na konsoli zdanie w postaci: "Podaną liczbę można zapisać jako: ...", 
# gdzie zapis będzie w postaci sumy iloczynów liczb dla każdego rzędu. Np. liczba 123: "Podaną liczbę można zapisać jako: 100 * 1 + 10 * 2 + 1 * 3". 
# Do pobrania i wypisania wartości użyj odpowiednio instrukcji readline() i write() z modułu sys).

import sys

def decompose_number(number):
    number_as_string = str(number)
    decompositions = []

    for i, digit in enumerate(number_as_string):
        place_value = 10 ** (len(number_as_string) - i - 1)
        decomposition = f"{place_value} * {digit}"
        decompositions.append(decomposition)

    return decompositions

try:
    user_input = input("Proszę podać liczbę całkowitą: ")
    number = int(user_input)
except ValueError:
    sys.stderr.write("Błąd: Podana wartość nie jest liczbą całkowitą.\n")
    sys.exit(1)

decompositions = decompose_number(number)

sys.stdout.write("Podaną liczbę można zapisać jako: ")
sys.stdout.write(" + ".join(decompositions))
sys.stdout.write("\n")

# 7. Wykorzystaj moduł this (sprawdź jego kod źródłowy) i korzystając z umieszczonego tam słownika kodującego (sprawdź dostępne zmienne modułu this) napisz skrypt, 
# który będzie kodował tym słownikiem wpisywane zdanie (przechwytuj z klawiatury). Wypisuj na konsoli zakodowane zdanie.

import this

encoding_dict = this.d

def encode_sentence(sentence):
    encoded_sentence = ""
    for char in sentence:
        if char in encoding_dict:
            encoded_char = encoding_dict[char]
            encoded_sentence += encoded_char
        else:
            encoded_sentence += char
    return encoded_sentence

try:
    sentence = input("Enter the sentence to encode: ")
except KeyboardInterrupt:
    print("\nInterrupted by the user.")
    exit()

encoded_sentence = encode_sentence(sentence)

print("Encoded sentence:", encoded_sentence)

# 8. Napisz skrypt, który pobiera z klawiatury zdanie, a na konsoli wyświetla wyrazy z tego zdania posortowane według ich długości rosnąco.

writing = input('Type your sentence: ')

tokens = writing.split(' ')
sorted = sorted(tokens, key=len)

print(sorted)

# 9. Napisz skrypt, który z tabeli dostępnej pod adresem http://prawolaffera.pl/uniwersalny-kod-przemowien/ (dane należy zaszyć w skrypcie na stałe) będzie generował n zdań na konsolę. Ilość zdań podawana jest przez użytkownika z klawiatury.

import random
import sys

array = [['Koleżanki i koledzy',
'realizacja nakreślonych zadań programowych',
'zmusza nas do przeanalizowania',
'istniejących warunków administracyjno--finansowych.'],
['Z drugiej strony',
'zakres i miejsce szkolenia kadr',
'spełnia istotną rolę wkształtowaniu',
'dalszych kierunków rozwoju.'],
['Podobnie',
'stały wzrost ilości i zakres naszej aktywności',
'wymaga sprecyzowania i określenia',
'systemu powszechnego uczestnictwa.'],
['Nie zapominajmy jednak, że',
'aktualna struktura organizacji',
'pomaga w przygotowaniu i realizacji',
'postaw uczestników wobec zadań stawianych przez organizację.'],
['W ten oto sposób',
'nowy model działalności organizacyjnej',
'zabezpiecza udział szerokiej grupie wkształtowaniu',
'nowych propozycji.'],
['Praktyka dnia codziennego dowodzi, że',
'dalszy rozwój różnych form działalności',
'spełnia ważne zadania wwypracowaniu',
'kierunków postępowego wychowania.'],
['Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
'stałe zabezpieczenie informacyjno programowe naszej działalności',
'umożliwia w większym stopniu tworzenie',
'systemu szkolenia kadry odpowiadającego potrzebom.'],
['Różnorakie i bogate doświadczenia',
'wzmacnianie i rozwijanie struktur',
'powoduje docenianie wagi',
'odpowiednich warunków aktywizacji.'],
['Troska organizacji, a szczególnie',
'konsultacja z szerokim aktywem',
'przedstawia interesującą próbę sprawdzenia',
'modelu rozwoju.'],
['Wyższe założenia ideowe, a także',
'rozpoczęcie powszechnej akcji kształtowania postaw',
'pociąga za sobą proces wdrażania i unowocześniania',
'form oddziaływania.']]

array = [list(item) for item in zip(*array)]
number = input('Type number of the sentences: ')
number = int(number)

for i in range(number):
    for j in range(4):
        random_number = random.randint(0, 9)
        sys.stdout.write(array[j][random_number])
        sys.stdout.write(' ')
    sys.stdout.write('\n')
