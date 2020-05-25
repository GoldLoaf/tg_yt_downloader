from aiogram import types
from misc import dp, bot
from dl import Audio

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def yt_download(message: types.Message):
    await message.answer('начинаю загрузку')
    audio = Audio(message.text)
    await message.answer_audio(audio.get_audio(), title=audio.get_title(), caption=audio.get_caption(),
                               performer=audio.get_performer())
    # audio.delete_audio()
