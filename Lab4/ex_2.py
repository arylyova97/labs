#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 2, 1, 1, 4, 5, 2, 2, 2]
data2 = gen_random(1, 3, 10)

un1 = Unique(data1)
un2 = Unique(data2)
print(' ,'.join(map(str, [i for i in un1])))
print(' ,'.join(map(str, [i for i in un2])))

# Реализация задания 2