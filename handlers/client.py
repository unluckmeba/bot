from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def game_message(message: types.Message):
    if message.from_user.id in ADMINS:
        data = ['🎲', '⚽️', '🎳', '🏀', '🎯', '🎰']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'У тебя не достаточно прав!')


async def mem(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(game_message, commands=['game'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(parsser_wheels, commands=["wheel"])