# 1. Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.

array = [2, 3, 9, 4, 5, 1, 6, 7, 8, 10]

first_array = array[:5]  
second_array = array[5:] 

print(first_array, second_array)

# 2. Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.

third_array = first_array + second_array
third_array.insert(0, 0)
third_array_copy = third_array.copy()
print(sorted(third_array))

# 3. Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funckję input(). Następnie wyświetl ciąg unikalnych znaków z wczytanego zdania, zapisanych alfabetycznie małymi literami.

sentence = input("Your input: ")

sentence = sentence.replace(" ", "").lower()

unique_characters = sorted(set(sentence))

unique_characters = [c for c in unique_characters if sentence.count(c) == 1]

result = ''.join(unique_characters)
print('Result: ', result)

# 4. Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1) a wartościami nazwy polskich miesięcy.

months = {'Styczeń': 1,
        'Luty': 2,
        'Marzec': 3,
        'Kwiecień': 4,
        'Maj': 5,
        'Czerwiec': 6,
        'Lipiec': 7,
        'Sierpień': 8,
        'Wrzesień': 9,
        'Październik': 10,
        'Listopad': 11,
        'Grudzień': 11} 

# 5. Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy. Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

polish_months = {
    1: 'Styczeń',
    2: 'Luty',
    3: 'Marzec',
    4: 'Kwiecień',
    5: 'Maj',
    6: 'Czerwiec',
    7: 'Lipiec',
    8: 'Sierpień',
    9: 'Wrzesień',
    10: 'Październik',
    11: 'Listopad'}

english_months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'}

all_months = {'pl': polish_months, 'en': english_months}
print(all_months['en'][4])
print(all_months['pl'][4])

# 6. Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, który będzie zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie miał przypisaną wartość 1. 
# Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1} Czy można w funkcji feommkeys() użyć dynamicznie podawanej wartości dla każdego klucza słownika?

name = 'Marianna'

unique_characters = sorted(set(name))

result_of_name = dict.fromkeys(unique_characters, 1)
    
print(result_of_name)

# 7. Wykorzystaj moduł string i następnie:
# -wczytaj ze standardowego wejścia dowolny łańcuch znaków,
# -używając formatowania łańcuchów (f-string) wyświetl ileznaków oraz jaki % tych znaków (zamienionych na małe litery) z wprowadzonego tekstu pokrywa się z: string.ascii_lowercase, string.digits.

import string

text = input("Enter any string: ")

total_characters = len(text)

matching_characters = sum(1 for char in text if char.lower() in string.ascii_lowercase + string.digits)

percentage_coverage = (matching_characters / total_characters) * 100

print(f"The text contains {total_characters} characters.")
print(f"{percentage_coverage:.2f}% of characters (converted to lowercase) match with lowercase letters and digits.")
