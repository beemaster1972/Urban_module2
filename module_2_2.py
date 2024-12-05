first, second, third = [int(input(f'Введите число N {_+1}')) for _ in range(3)]
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
