import os
import time


def print_dir():
    directory = os.getcwd()
    for root, dirs, files in os.walk(directory):
        if dirs != []:
            print(f'Корневая директория  = "{root}"\nВ корневой директории директории = "{dirs}"')
        else:
            print(f'Корневая директория  = "{root}"\nВ корневой директории директорий нет')
        for i, file in enumerate(files):
            print(f'{i + 1}:', end=' ')
            file_path = os.path.join(root, file)
            file_time = os.path.getmtime(file_path)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
            file_size = os.path.getsize(file_path)
            parent_dir = os.path.dirname(root)
            print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, '
                  f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


print_dir()
