import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    # Необходимо реализовать генератор
    assert len(args) > 0 #он проверяет длину массивчика аругментов (тайтл, прайс)

    if len(args) == 1: #выдает только значение по ключу
        for item in items:
            if args[0] in item and item[args[0]]:
                yield item[args[0]]  #вывод
    else:
        for item in items:
            result = {}
            for arg in args:
                if arg in item and item[arg]:
                    result[arg] = item[arg]
            if (result): #если словарь result не пустой в результате то мы вернем
                yield result



# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for count in range(num_count):
        yield random.randint(begin, end)
    # Необходимо реализовать генератор
