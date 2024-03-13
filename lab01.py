# 1. Napisz kod, w którym stworzysz po dwa obiekty typu int i float z użyciem różnych wartości dla konstruktorów tych typów
# (np. z inną podstawą niż domyślne 10 dla typu int).

int_obj1 = int(16)
int_obj2 = int(42)

float_obj1 = float(3.14)
float_obj2 = float(2.718)

print("Obiekty typu int:")
print("int_obj1:", int_obj1)
print("int_obj2:", int_obj2)

print("\nObiekty typu float:")
print("float_obj1:", float_obj1)
print("float_obj2:", float_obj2)

# 2. Napisz kod, w którym wykorzystasz poniższe metody: int.bit_count() oraz float.is_integer()

n1 = 5.0
n2 = 5.5
n3 = 3

print("\nSprawdzenie czy n1 i n2 są intami:")
print( n1.is_integer())
print(n2.is_integer())
print("\nSprawdzenie ile bitów ma zmienna n3=3")
print(n3.bit_count())

# 3.  Wykonaj konwersję dowolnej liczby całkowitej na binarną i ponownie na całkowitą

binary_representation_n3 = bin(n3)
print("\nBinarna reprezentacja liczby 3: ", binary_representation_n3)
num = int(binary_representation_n3, 2)
print("\nPowrót do liczby całkowitej z binarnej: ", num)

# 4. Przygotuj 4 przykłady kodu, który wykorzystuje operatory bitowe.

num1 = 10   # 1010
num2 = 6    # 0110

# Operacja bitowe AND (&): Zwraca bitowe AND dwóch liczb.
result1 = num1 & num2
print(result1)   # Output: 2 (0010)

# Operacja bitowe OR (|): Zwraca bitowe OR dwóch liczb.
result2 = num1 | num2
print(result2)   # Output: 14 (1110)

# Operacja bitowe XOR (^): Zwraca bitowe XOR dwóch liczb.
result3 = num1 ^ num2
print(result3)   # Output: 12 (1100)

# Operacja bitowe przesunięcia w lewo (<<): Przesuwa bity liczby w lewo o określoną liczbę pozycji.
result4 = num1 << 2
print(result4)   # Output: 40 (101000)

# 5. Zapisz przykład konwersji wartości zmiennoprzecinkowej do postaci hex i ponownie do wartości typu float.

float_value = 3.14
hex_value = float.hex(float_value)

print("\nWartość float:", float_value)
print("Wartość szesnastkowa:", hex_value)

# Konwersja z powrotem do wartości float
converted_float_value = float.fromhex(hex_value)

print("Po konwersji z powrotem do wartości float:", converted_float_value)