# This is a sample Python script.

import telebot

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

teleName = "TELE_NAME"
teleToken = "TELE_TOKEN"

bot = telebot.TeleBot(teleToken, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
print(f'Hiafasdfdsaf,')
