from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button_1 = KeyboardButton(text='Информация')
kb.add(button)
kb.add(button_1)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я помогу тебе рассчитать твою норму калорий', reply_markup=kb)


@dp.message_handler(text=['Спасибо'])
async def thanks(message):
    await message.answer('Не за что, человек! Кушай правильно!')


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer("Я Бот, который помогает рассчитать норму калорий", reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer("Введите свой возраст:", reply_markup=kb)
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
