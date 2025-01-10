from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

t = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t.content, 'html.parser')

s = requests.get('https://sinoptik.ua/погода-сырдарья')
html_s = BS(s.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]
    print(t_min, t_max)

for el in html_s.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    s_min = min[4:]
    s_max = max[5:]


def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01"),
         InlineKeyboardButton("Sirdaryo", callback_data=f"20")],
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "20":
        query.message.edit_text(f"Bugun Sirdaryo viloyatida havo o`zgarib turadi\nmin {s_min}\nmax "
                                f"{s_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "7970621056:AAFt5UCHBMRWXZmiYroMO-WCaD0RL9K4tgg"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# Davomini o`zingiz mustaqil bajaring!!!
