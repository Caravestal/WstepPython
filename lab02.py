# 1. Napisz fragment kodu, który wczyta trzy zmienne z klawiatury:
# linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
# separator źródłowy
# separator docelowy
# Następnie zaimplementuj z użyciem metod split oraz join podzielenie danych wejściowych pierwszym separatorem, połączenie i wypisanie danych połączonych drugim separatorem. Czy można to zrobić prościej wykorzystując wbudowane metody?

writing = input("Type something like: 2,4,5 : ")
source_separator = input("Enter the source separator: ")
target_separator = input("Enter the target separator: ")

separated = writing.split(source_separator)
print('Separated: ', separated)
joined = target_separator.join(separated)
print('Joined: ', joined)

# 2. Użyj funkcji input() aby pobrać łańcuch znaków z klawiatury i z użyciem wycinków (slice) wykonaj:
# -podziel łańcuch na dwie części, w miarę możliwości równe, ale jeżeli długość łańcucha jest nieparzysta, np. 11 znaków to pierwszy ma długość 5, a drugi 6. Wyświetl te łańcuchy w oknie konsoli.
# -wyświetl łańcuch składający się z co drugiego znaku licząc od końca łańcucha.

writing = input("Your input: ")
if len(writing)%2 == 1:
    length1 = (len(writing)-1)//2
    length2 = len(writing)
    print(writing[:length1])
    print(writing[length1:length2])
else:
    length1 = len(writing)//2
    length2 = len(writing)
    print(writing[:length1])
    print(writing[length1:length2])

print(writing[::-2])

# 3. Wyświetl na konsoli dowolny ciąg znaków i wykorzystaj wbudowane metody: title(), capitalize(), zfill(), upper(), count(), center().

print('title is here'.title())
print('this is the sentence'.capitalize())
print('big letters'.upper())
print('101'.zfill(4))
print('this this is'.count('this'))
print('text'.center(10, '-'))

# 4. Wprowadź z klawiatury dowolny łańcuch znaków i zapisz go do zmiennej. 
# Następnie bazując na przykładzie poniżej zapisz również wyniki dla metod isalpha(), isascii(), isprintable(), istitle(), isupper(). wejscie = input() print("Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}").

inp = input(('Your input: '))
print(f"Łańcuch {inp} isalpha: {inp.isalpha()}")
print(f"Łańcuch {inp} isascii: {inp.isascii()}")
print(f"Łańcuch {inp} isprintable: {inp.isprintable()}")
print(f"Łańcuch {inp} istitle: {inp.istitle()}")
print(f"Łańcuch {inp} isupper: {inp.isupper()}")

#6. Wykorzystując listing 7 wypisz na konsoli 10 wybranych znaków niestandardowych (np. litery z alfabetu greckiego, symbole walut - (funt, bitcoin)) wypisując jednocześnie jego kod z tablicy unicode.

print("\u16A2 /U+16A2")
print("\u16A6 /U+16A6")
print("\u16AC /U+16AC")
print("\u16B1 /U+16B1")
print("\u16B4 /U+16B4")
print("\u16BC /U+16BC")
print("\u16BE /U+16BE")
print("\u16C1 /U+16C1")
print("\u16C5 /U+16C5")
print("\u16CB /U+16CB")
print("\u16CF /U+16CF")
