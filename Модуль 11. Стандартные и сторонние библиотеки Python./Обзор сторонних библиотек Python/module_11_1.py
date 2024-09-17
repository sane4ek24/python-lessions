import requests
from PIL import Image

# requests - запросить данные с сайта и вывести их в консоль.


the_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"

result = []

for i in range(1, 11):
    a = requests.get(the_URL)
    b = a.text
    result.append(b)

print(result)
"""благодаря библиотеке requests я смог вытащить данные с сайта и теперь мне не придется
    вытаскивать их руками, это удобно и есть огромное колличество методов для упрощения работы"""

#pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

img = Image.open('1.jpg')
new_name = "1.webp"
img.save(new_name)

img2 = Image.open("1.webp")
new_size = (500, 500)
img2.thumbnail(new_size)
img2.save("final1.webp")

"""благода библиотеке PIL я смог легко изменить формат фотографии и ее размер, это очень удобно"""
