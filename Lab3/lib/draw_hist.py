def _find_max(lst):
    max_age = 0
    for item in lst:
        if item['age'] > max_age:
            max_age = item['age']
    # print(max_age)
    return max_age


def draw(lst):
    count_of_ages = [0 for i in range(0, _find_max(lst))]
    for item in lst:
        count_of_ages[item['age']-1] += 1
    for i in range(len(count_of_ages)):
        print(i+1, '#' * count_of_ages[i])
