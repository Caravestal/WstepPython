# 5. Przejdź na stronę https://pyformat.info/, a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w 
# przykładach z tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby, znakiem, wypełnieniem spacji itp.). Przerób zaprezentowane tam przykłady na postać z użyciem f-string.

text = '12345'
print('{:^10}'.format(text))
print('{:.3}'.format(text))
print('{:10.3}'.format(text))
print('{:6d}'.format(int(text)))
print('{:08.4f}'.format(3.1237312))
