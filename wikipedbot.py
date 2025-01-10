import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6238789734:AAFs9A6kegII8SH32Z_obHdNWIX5VtDi_3o'
wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        f"Salom    '{message.from_user.full_name}'\nMen Wikipedia botman\nㅤㅤㅤㅤ| aiouz  tomonidan yaratildim!\n")
    await message.reply("Qaysi mavzuda ma'lumot izlaysiz?")


# @dp.message_handler()
# async def sentwiki(message: types.Message):

@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuda maqola mavjud emas!\nIltimos qaytadan urinib ko'ring")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
