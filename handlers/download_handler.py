from aiogram import types
from misc import dp, bot
from dl import Audio

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def yt_download(message: types.Message):
    audio = Audio(message.text)
    await bot.send_audio(message.chat.id, audio.tg_file)
