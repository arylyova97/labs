def minInList(lst):
    minEl = lst[0]
    for i in range(1,len(lst)):
        if minEl > lst[i]:
            minEl = lst[i]
    return minEl

def avrInList(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum/len(lst)


if __name__ == '__main__':
    print(minInList([1, 32, 4, 5, -3, 6]))
    print(minInList([1, -2, 4, 5, -3, -6]))
    print(minInList([1, -32, 4, 5, -3, 6]))
    print('{:.2f}'.format(avrInList([1, 2, 3, 4])))
    print('{:.2f}'.format(avrInList([1, 2, 3, 4, 0])))
    print('{:.2f}'.format(avrInList([1, 2, 3, 4, 0, 0])))