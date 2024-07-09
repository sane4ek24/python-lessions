first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    print('Число:3')
elif first == second or first == third or not second != third:
    print("Число:2")
else:
    print('Число:0')
