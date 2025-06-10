#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio
from config import TG_TOKEN

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(TG_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет! Я твой новый boss \n What\'s happening man!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


if __name__ == '__main__':
    asyncio.run(bot.polling())