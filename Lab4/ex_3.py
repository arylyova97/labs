#!/usr/bin/env python3

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
print(sorted(data, key=lambda x: abs(x))) #key-опциональный параметр, в который передаешь функ., которая возвращает объект сортировки
#lambda x аналог def ###(x): return abs(x)
