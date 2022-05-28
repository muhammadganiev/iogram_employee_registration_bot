from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from requests import request

bot = Bot(token='5453501886:AAE49LmQsZ6vZDC-_sg4muhfUH5pKqMVppk')
dp = Dispatcher(bot)

b1 = KeyboardButton('Открыть смену')
b2 = KeyboardButton('Закрыть смену')
b3 = KeyboardButton('Отправить локацию', request_location=True)

otmetka = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(b1).add(b2)
loc = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(b3)

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
    await message.answer(' ✅ Смена подтверждена \n 🔓 Не забудьте открыть смену перед работой 😁 \n 🔐 закрыть смену после работы 😁')
    await message.answer('Хорошего рабочего дня 😁, ИззИ любит тебя и ценит ❤️', reply_markup=otmetka)
@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply(f"Ассаламу Алеикум родноой💥 \nДля увеличения качества обслуживания и процветания ИззИ✨ мы разработали автоматизированную систему отметки членов команды ИззИ🧡 \nДанная система несет исключительно деловой характер \nKаждый день вам нужно будет отмечаться перед началом работы и после его окончания, а также отправлять данные о геопозиции для подтверждения вашего присутствия на рабочем месте \n", reply_markup=otmetka)

@dp.message_handler()
async def answer(message: types.Message):
    if message.text == 'Открыть смену':
         await message.answer('Отправьте локацию для подтверждения смены 📍 ', reply_markup=loc)
    elif message.text == 'Закрыть смену':
         await message.answer('Отправьте локацию для подтверждения смены 📍', reply_markup=loc)
executor.start_polling(dp)