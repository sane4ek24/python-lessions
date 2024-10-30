from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
but = InlineKeyboardButton(text='Купить')
but_1 = InlineKeyboardButton(text='Рассчитать')
but_2 = InlineKeyboardButton(text='Информация')
kb.add(but)
kb.add(but_1)
kb.add(but_2)

kb1 = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_1 = InlineKeyboardButton(text='Формула расчета', callback_data='formulas')
kb1.add(button)
kb1.add(button_1)

kb2 = InlineKeyboardMarkup()
button_2 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
button_3 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
button_4 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
button_5 = InlineKeyboardButton(text='Product4', callback_data="product_buying")
kb2.add(button_2)
kb2.add(button_3)
kb2.add(button_4)
kb2.add(button_5)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет, выбери нужную клавишу: ', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я помощник по подсчету калорий и могу продавать ремешки для смарт-часов')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb1)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('img/DSN-11-40-BL 1.jpg', 'rb') as bl:
        await message.answer_photo(bl, 'Название: Ремешок Черный | Описание: для Apple Watch 40mm | Цена: 100')
    with open('img/DSN-11-40-PK 1.jpg', 'rb') as pk:
        await message.answer_photo(pk, 'Название: Ремешок Розовый | Описание: для Apple Watch 40mm | Цена: 200')
    with open('img/DSN-11-40-RD 1.jpeg', 'rb') as rd:
        await message.answer_photo(rd, 'Название: Ремешок Красный | Описание: для Apple Watch 40mm | Цена: 300')
    with open('img/DSN-11-40-SC 1.jpg', 'rb') as sc:
        await message.answer_photo(sc, 'Название: Ремешок Цветной | Описание: для Apple Watch 40mm | Цена: 400')
    await message.answer('Выберите продукт для покупки: ', reply_markup=kb2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула для расчета: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    await message.answer(f'Ваша норма калорий:{10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
