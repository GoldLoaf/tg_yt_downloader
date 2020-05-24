from aiogram import types
from misc import dp, bot

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def yt_download(message: types.Message):
    await bot.send_audio()
