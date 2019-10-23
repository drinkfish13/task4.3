cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}
person = int(input('Введите количество гостей'))
menu = input('Введите блюда через пробел:')
menu = menu.split()
count_s = 0
count_p = 0
count_l = 0
for i in menu:
    if i == 'салат':
        count_s += 1
    elif i == 'пицца':
        count_p += 1
    elif i == 'лимонад':
        count_l += 1

def salad(n):
    d_salad = cook_book['салат']
    for k in d_salad:
        k['quantity'] = k['quantity']*n
    return d_salad
def pizza(n):
    d_pizza = cook_book['пицца']
    for k in d_pizza:
        k['quantity'] = k['quantity']*n
    return d_pizza
def lim(n):
    d_lim = cook_book['лимонад']
    for k in d_lim:
        k['quantity'] = k['quantity']*n
    return d_lim

d_all =[]
if count_s > 0:
    d_all += salad(person)
if count_p > 0:
    d_all += pizza(person)
if count_l > 0:
    d_all += lim(person)

for t in d_all:
    print(t['ingridient_name'],t['quantity'],t['measure'])


