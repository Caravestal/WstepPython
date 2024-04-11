# 1. Wczytaj plik zamowienia.csv i dokonaj w nim kilku przekształceń:
# pozbądź się znaku z (właściwie zł) z kolumny Utarg
# zamień separator wartości dziesiętnej w tej samej kolumnie na '.'
# pozbądź się spacji jako separatora tysięcy w kolumnie Utarg
# zamień format daty w pliku na RRRR-MM-DD (wykorzystaj moduł datetime)
# Podziel plik na dwie części i zapisz je tak, aby dane dla każdego kraju (Polska, Niemcy) znajdowały się w oddzielnych plikach o nazwach zamowienia_polska.csv i zamowienia_niemcy.csv.

flag = True
with open('zamowienia.csv', 'r', encoding='utf-8') as file_reader: 
    for line in file_reader:
        line_as_array = line.split(';')
        if flag is False:
            temp_date = line_as_array[2].split('.')
            line_as_array[2] = temp_date[2] + '-' + temp_date[1] + '-' + temp_date[0]
            line_as_array[4] = line_as_array[4].replace('\n', '')
            line_as_array[4] = line_as_array[4].replace('z\x88', '')
            line_as_array[4] = line_as_array[4].replace(' ', '')
            line_as_array[4] = line_as_array[4].replace(',', '.')
            if line_as_array[0] == 'Polska': 
                with open('zamowienia_polska.csv', 'a') as plik:
                    output_line = line_as_array[0]+';'+line_as_array[1]+';'+line_as_array[2]+';'+line_as_array[3]+';'+line_as_array[4]+'\n'
                    plik.write(output_line)
            else:
                with open('zamowienia_niemcy.csv', 'a') as plik:
                    output_line = line_as_array[0]+';'+line_as_array[1]+';'+line_as_array[2]+';'+line_as_array[3]+';'+line_as_array[4]+'\n'
                    plik.write(output_line)            
        else:
            with open('zamowienia_polska.csv', 'a') as plik:
                output_line = line_as_array[0]+';'+line_as_array[1]+';'+line_as_array[2]+';'+line_as_array[3]+';'+line_as_array[4]
                plik.write(output_line)
            with open('zamowienia_niemcy.csv', 'a') as plik:
                output_line = line_as_array[0]+';'+line_as_array[1]+';'+line_as_array[2]+';'+line_as_array[3]+';'+line_as_array[4]
                plik.write(output_line)   
            flag = False

# 2. Napisz funkcję, która przyjmuje listę plików oraz nazwę nowego pliku jako argumenty wejściowe. Funkcja scala zawartość plików w jeden plik wynikowy o podanej wcześniej nazwie.

def merge_files(file_list, new_file_name):
    with open(new_file_name, 'w') as output_file:
        for file_name in file_list:
            with open(file_name, 'r') as file:
                content = file.read()
                output_file.write(content)
                output_file.write('\n')

file_list = ['zamowienia_niemcy.csv', 'zamowienia_polska.csv']
new_file_name = 'result.csv'
merge_files(file_list, new_file_name)

# 3. Napisz funkcję, która będzie zwracała n największych lub najmniejszych wartości (odpowiednia wartość parametru) z listy numerycznej. Lista jest parametrem wejściowym funkcji. W funkcji sprawdzaj czy lista zawiera tylko liczby.

def n_smallest_numbers(list, number, reverse=False):
    try:
        return sorted(list, reverse=reverse)[:number]
    except:
        return 'Given array includes non-numeric values'

print(n_smallest_numbers([1, 2, 6, 2, '4', 1], 3))

# 4. Mając listę mieszana = [1, 2.3, ‘Zbyszek’, 5, ‘Marian’, 3.0] napisz funkcję, która zapisze wartości dla każdego typu do słownika gdzie pod kluczem równym nazwie typu zmiennej (int, float, str, itp.) 
# wartością będzie lista elementów z listy 'mieszana' danego typu. 
# Przykład: {'int': [1,5], 'str': ['Zbyszek','Marian']} itd.

def sort_by_types(array):
    types = list(dict.fromkeys([type(element).__name__ for element in array]))
    dic = {}
    for typ in types:
        dic[typ] = [i for i in array if type(i).__name__ == typ]
    return dic


mixed = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
print(sort_by_types(mixed))

# 5. Napisz funkcję:
# -parametr wejściowy to lista stringów z nazwiskami
# -funkcja zapisuje do dwóch oddzielnych plików o nazwach ‘A-M_nazwiska.txt’ oraz ‘N-Ż_nazwiska.txt’ odpowiednie nazwiska z podanej listy
# Możesz wykorzystać moduł unidecode, który należy uprzednio zainstalować.

def sort_surnames(surnames):
    for i in surnames:
        if i[0] <= 'M':
            with open('A-M_nazwiska.txt', 'a') as plik:
                plik.write(i + '\n')
        else:
            with open('N-Ż_nazwiska.txt', 'a') as plik:
                plik.write(i + '\n')   
    
surnames = ["Kowalski", "Nowak", "Wiśniewski", "Dąbrowski", "Lewandowski"]
sort_surnames(surnames)

# 6. Napisz funkcję, która wyświetla podany tekst odwracając kolejność liter w wyrazach. Np. „Ala ma kota” wyświetli „alA am atok”

def reverse_words(sentence):
    tab_of_words = sentence.split(' ')
    tab_of_words = [word[::-1] for word in tab_of_words]
    ' '.join(tab_of_words)
    print(tab_of_words)
    
reverse_words("Ala ma kota")

# 7. Napisz funkcję, która:
# -„rozdaje” karty z talii 52 kart (np. As pik, Dama karo, itd.) dla 4 graczy
# -karty rozdawane są bez powtórzeń po 5 dla każdego gracza
# -wyświetlana jest informacja jak wygląda „ręka” każdego z graczy, np. Alan [As pik, 9 karo, itd.]

import random

def deal_cards():
    deck = [
        "As pik", "2 pik", "3 pik", "4 pik", "5 pik", "6 pik", "7 pik", "8 pik", "9 pik", "10 pik", "Walet pik", "Dama pik", "Król pik",
        "As karo", "2 karo", "3 karo", "4 karo", "5 karo", "6 karo", "7 karo", "8 karo", "9 karo", "10 karo", "Walet karo", "Dama karo", "Król karo",
        "As trefl", "2 trefl", "3 trefl", "4 trefl", "5 trefl", "6 trefl", "7 trefl", "8 trefl", "9 trefl", "10 trefl", "Walet trefl", "Dama trefl", "Król trefl",
        "As kier", "2 kier", "3 kier", "4 kier", "5 kier", "6 kier", "7 kier", "8 kier", "9 kier", "10 kier", "Walet kier", "Dama kier", "Król kier"
    ]


    random.shuffle(deck)

    players = {f"Player {i+1}": [] for i in range(4)}

    for _ in range(5):
        for player in players:
            card = deck.pop()
            players[player].append(card)

    for player, hand in players.items():
        print(f"{player}: {hand}")

deal_cards()


# 8. Napisz funkcję, która wczytuje z pliku zawierającego imiona i nazwiska osób zapisane po jednym w linii, np.
# Marek Markowski
# Paweł Budzikowski
# Funkcja generuje dla podanej listy adresy e-mail postaci: imie.nazwisko@domena (parametr funkcji) i zapisuje dane do nowego pliku dopisując przy wcześniejszym nazwisku wygenerowany adres, np.
# Marek Markowski, marek.markowski@student.uwm.edu.pl itd.
#W nazwach e-mail powinny być zastępowane ewentualne polskie znaki (ż,ź na z, ą na a itd.).

def generate_email_address(filename, domain):
    def remove_polish_characters(name):
        polish_characters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
        for polish_char, repl_char in polish_characters.items():
            name = name.replace(polish_char, repl_char)
        return name

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open('output.txt', 'w') as output_file:
        for line in lines:
            name = line.strip()
            first_name, last_name = name.split()
            email = f"{remove_polish_characters(first_name.lower())}.{remove_polish_characters(last_name.lower())}@{domain}"
            output_file.write(f"{name}, {email}\n")

generate_email_address("names.txt", "student.uwm.edu.pl")

# 9. Przygotuj plik z kilkoma hasłami, które nadają się do gry 'Koło fortuny'. Wczytaj te hasła do listy i losuj jedno z nich. 
# Na ekranie wyświetlaj hasło bez ujawniania poszczególnych liter, np.:___ _____ ___ __ _______ dla hasła 'Bez pracy nie ma kołaczy'. 
# Nastepnie w pętli pozwalaj uzytkownikowi na podawanie jednej litery, która będzie podstawiana w miejscach gdzie występuje lub wyświetlaj komunikat, że takiej litery nie ma w haśle. 
# Dodaj też funkcjonalność, która pozwala na odgadnięcie (wpisanie) całego hasła.

import random

def load_passwords(filename):
    with open(filename, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

def hide_password(password):
    hidden = ''
    for char in password:
        if char != ' ':
            hidden += '_'
        else:
            hidden += ' '
    return hidden

def reveal_letters(password, hidden, letter):
    revealed = ''
    for i in range(len(password)):
        if password[i].lower() == letter.lower():
            revealed += password[i]
        elif password[i] == ' ':
            revealed += ' '
        else:
            revealed += hidden[i]
    return revealed

def play_hangman():
    passwords = load_passwords('passwords.txt')
    password = random.choice(passwords)
    hidden_password = hide_password(password)

    print("Welcome to Hangman!")
    print("Guess the phrase:")
    print(hidden_password)

    guessed_letters = []
    attempts = 7

    while attempts > 0:
        guess = input("Enter a letter or guess the whole password: ").strip()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed this letter.")
            elif guess.lower() in password.lower():
                hidden_password = reveal_letters(password, hidden_password, guess)
                print(hidden_password)
                if hidden_password == password:
                    print("Congratulations! You guessed the password correctly!")
                    break
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
            guessed_letters.append(guess)
        else:
            if guess.lower() == password.lower():
                print("Congratulations! You guessed the password correctly!")
                break
            else:
                print("Wrong guess!")
                attempts -= 1
                print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print("You have run out of attempts. The correct password was:", password)

play_hangman()
