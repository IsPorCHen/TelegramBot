from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API = '7261637303:AAEK9oypxIJ-yrA1eLTKfAHd9YWstSAPEBo'
bot = Bot(token=API)
dp = Dispatcher()

#выводит сообщение при команде start
@dp.message(Command('start'))
async def echo(message: types.Message):
    await message.answer("Привет, я бот")

#ссылка на сайт колледжа
@dp.message(Command('ects'))
async def echo(message: types.Message):
    await message.answer("Очень хороший(нет) колледж")
    await message.answer("https://www.ects.ru/")

#ссылка на страницу изменения в расписании
@dp.message(Command('changes'))
async def echo(message: types.Message):
    await message.answer("Я вас понял, держите страницу изменения в расписании\n")
    await message.answer("https://www.ects.ru/page281.htm")

#повторяет написанный текст
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(on_start())
