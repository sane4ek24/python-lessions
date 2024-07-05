immutable_var = ([1, 2], True, "str")
print(immutable_var)
#immutable_var[1] = 12  Кортеж и был придуман для того, чтобы в нем нельзя было изменять значения, но и тип 'tuple' не поддерживает именения
mutable_list = ['1', '2', '3']
mutable_list[1] = '48'
mutable_list[0] = 'privet'
print(mutable_list)