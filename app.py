import telebot
aa=[]

API_TOKEN = '6191579103:AAHbR8ifnv9SDtZ86363NZEuprABIqR3o10'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    x=message.text
    print(x)
    print(type(x))
    aa=x.split(" ")
    print(aa)
    big=float(aa[0])
    small=float(aa[1])
    ans=big/((big-small)*1.1)
    bot.reply_to(message, ans)


bot.infinity_polling()