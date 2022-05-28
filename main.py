from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from requests import request
from telegram import Location

bot = Bot(token='TOKEN')
dp = Dispatcher(bot)

b1 = KeyboardButton('Открыть смену')
b2 = KeyboardButton('Закрыть смену')
b3 = KeyboardButton('Отправить локацию', request_location=True, callback_data="call")

otmetka = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(b1).add(b2)
loc = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(b3)

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply(f"Ассалому Алеикум нажми на кнопки", reply_markup=otmetka)

@dp.message_handler()
async def answer(message: types.Message):
    if message.text == 'Открыть смену':
         await message.answer('Отправьте локацию для подтверждения смены', reply_markup=loc)
    elif message.text == 'call':
         await message.answer('Смена подтверждена, Не забудьте открыть смену перед работой и закрыть смену после работы :)', reply_markup=otmetka)
    elif message.text == 'Закрыть смену':
         await message.answer('Отправьте локацию для подтверждения смены', reply_markup=loc)
executor.start_polling(dp)