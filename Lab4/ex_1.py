#!/usr/bin/env python3
import librip.gens as gens


def print_list(lst):
    print(' ,'.join(map(str, lst))) # map -функ которая применяет функцию str(к строке) к lst, join (соединяет только строки) ставит запятые и выводит


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'},
    {'title': None, 'price': None, 'color': None},
    {'color': 'white'},
]

res_list = []

for item in gens.field(goods, 'title', 'price'): # генератор возвращает в item нужный элемент
    res_list.append(item)
print_list(res_list) #вот тут скобочик появятся, я от них избавлялся _list

print_list([i for i in gens.gen_random(1, 3, 5)])

