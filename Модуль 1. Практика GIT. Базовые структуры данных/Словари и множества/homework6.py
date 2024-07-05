my_dict = {'Oleg': 1995, 'Stas': 1996, 'Boris': 1985}
print(my_dict)
print(my_dict.get('Stas'))
print(my_dict.get('Sasha', 'Такого имени нет'))
my_dict.update({'Sasha': 1990, 'Sergey': 1992})
print(my_dict)
del my_dict['Oleg']
print(my_dict)


my_set = {1, 2, 3, 3, 5, True, 'str', True}
print(my_set)
my_set.add(4)
my_set.add(False)
my_set.discard(3)
print(my_set)
