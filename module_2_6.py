def is_multiplicity(value,num1,num2):
    return not (value % (num1+num2))


def create_result(value):
    res = set()
    for num1 in range(1,value):
        for num2 in range(1,value):
            if num2 == num1:
                continue
            if is_multiplicity(value,num1,num2):
                res.add(tuple(sorted([num1,num2])))
    return res


def print_result(res):
    res = sorted(res)
    for paire in res:
        for el in paire:
            print(el, end='')

while True:
    n = int(input('Введите число от 3 до 20:'))
    if n > 20 or n < 3:
        print(f'Число {n} не подходит по условию задачи')
        break
    result = create_result(n)
    print_result(result)
    break