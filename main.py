import os
from datetime import datetime
import datetime
from time import strftime, time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import sqlite3

token = os.getenv('TOKEN')

bot = Bot(token= token)
dp = Dispatcher(bot)
b1 = KeyboardButton('Открыть смену')
b2 = KeyboardButton('Закрыть смену')
b3 = KeyboardButton('Отправить локацию', request_location=True)

otmetka = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(b1).add(b2)
loc = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(b3)

a = datetime.datetime.now().time()
b = datetime.time(8,30,0,0)
c = datetime.time(23,30,0,0)
d = datetime.time(0,0,0,0)
seychas = datetime.timedelta(hours=a.hour, minutes=a.minute, seconds=a.second)
utro = datetime.timedelta(hours=b.hour, minutes=b.minute, seconds=b.second)
vecher = datetime.timedelta(hours=c.hour, minutes=c.minute, seconds=c.second)
itog_vremya = datetime.timedelta(hours=d.hour, minutes=d.minute, seconds=d.second)
status = ['Пришёл раньше времени на:', 'Опоздал на:', 'Ушёл раньше времени на:']
status_otmetka_var = ['Открыл', 'Закрыл', 'До сих пор не открыл']
status_otmetka = 'Открыл'
status_icon_var = ['✅', '❌', '⚠️']
status_icon = '✅'

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    #if seychas >= utro and seychas < :
    #  status_otmetka = status_otmetka_var[0]
    #  status_icon = status_icon_var[0]
      
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
    await message.answer(' ✅ Смена подтверждена \n 🔓 Не забудьте открыть смену перед работой 😁 \n 🔐 закрыть смену после работы 😁')
    await message.answer('Хорошего рабочего дня 😁, ИззИ любит тебя и ценит ❤️', reply_markup=otmetka)
    await message.answer(f'{message.from_user.id}')
    message = await bot.send_message(
      chat_id=582776432,
      text= f'*Имя: *{message.from_user.first_name}\n----------------------------\n*Фамилия: *{message.from_user.last_name}\n----------------------------\n*Telegram id: *@{message.from_user.username}\n----------------------------\n*{status_otmetka}* смену {status_icon}\n----------------------------\n*Адрес* в момент отметки:',
      parse_mode= 'Markdown'
    )
    message = await bot.send_location(
      chat_id=582776432,
      longitude=lon,
      latitude=lat,
      protect_content=True
    )
    message = await bot.send_message(
      chat_id=582776432,
      text="Время в момент отметки:\n---------"+datetime.now().strftime("%H:%M:%S")+"---------"
    )
    
@dp.message_handler(commands = ['i77it', 'help'])
async def welcome(message: types.Message):
  await message.reply(f"Ассаламу Алеикум родноой💥 \nДля увеличения качества обслуживания и процветания ИззИ✨ мы разработали автоматизированную систему отметки членов команды ИззИ🧡 \nДанная система несет исключительно деловой характер \nKаждый день вам нужно будет отмечаться перед началом работы и после его окончания, а также отправлять данные о геопозиции для подтверждения вашего присутствия на рабочем месте \n", reply_markup=otmetka)
@dp.message_handler()
async def answer(message: types.Message):
    if message.text == 'Открыть смену':
         await message.answer('Отправьте локацию для подтверждения смены 📍 ', reply_markup=loc)
    elif message.text == 'Закрыть смену':
         await message.answer('Отправьте локацию для подтверждения смены 📍', reply_markup=loc)
executor.start_polling(dp)