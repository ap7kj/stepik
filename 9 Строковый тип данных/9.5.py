// step 1 //
Что покажет приведенный ниже фрагмент кода?
s = 'aabbAA111ccDDaa'
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
---
True
False
False
---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
--- True ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
s = 'AAb!@#$11CC'
print(s.isupper())
--- False ---

// step 4 //
Что покажет приведенный ниже фрагмент кода?
s = '    abbc    '
print(s.isspace())
--- False ---

// step 5 //
Дополните приведенный код, используя форматирование строк с помощью метода format, так чтобы он вывел текст:
«In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
s = 'In {0}, someone paid {1}k Bitcoin for two pizzas.'.format(2010, 10)
print(s)

// step 6 //
Дополните приведенный код, используя форматирование строк с помощью f-строк, так чтобы он вывел текст:
«In 2010, someone paid 10K Bitcoin for two pizzas.» (без кавычек).
year = 2010
amount = '10K'
currency
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
