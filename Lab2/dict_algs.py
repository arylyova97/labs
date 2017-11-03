def info(emps, child_age=18):
    prnts = []
    for emp in emps:
        for chd in emp['children']:
            if chd['age'] > child_age:
                prnts.append(emp['name'])
                break
    return prnts

def printLst(lst):
    print('\n'.join(item for item in lst))

    print()
if __name__ == '__main__':
    ivan = {
        'name': 'ivan',
        'age': 34,
        'children': [{
            'name': 'vasja',
            'age': 120,
        }, {
            'name': 'petja',
            'age': 120
        }],
    }
    darja = {
        'name': 'darja',
        'age': 41,
        'children': [{
            'name': 'kirill',
            'age': 21,
        }, {
            'name': 'pavel',
            'age': 150
        }],
    }
    emps = [ivan, darja]
    printLst(info(emps))