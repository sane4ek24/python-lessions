from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip().splitlines()
        except FileNotFoundError:
            return []

    def add(self, *products):
        existing_products = self.get_products()
        existing_product_names = [line.split(', ')[0] for line in existing_products]

        for product in products:
            if product.name in existing_product_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # str

s1.add(p1, p2, p3)  # Добавляем продукты

print(s1.get_products())  # Выводим список продукто
