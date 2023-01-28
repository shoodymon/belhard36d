from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Bot определяет, на какие команды от пользователя и каким способом отвечать;
# Dispatcher позволяет отслеживать обновления;
# Executor запускает бота и выполняет функции, которые следует выполнить.
# types позволит нам использовать базовые классы для аннотирования, то есть восприятия сообщений.

API_TOKEN = '5959882859:AAHSwG_rho8W_e4oRi0Gvy4AL_v7Iv9Coz0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def begin(messsage: types.Message):
    markup = InlineKeyboardMarkup()
    button_loan = InlineKeyboardButton('Онлайн займы', callback_data='button_loan')
    button_credit = InlineKeyboardButton('Кредиты', callback_data='button_credit')
    button_credit_card = InlineKeyboardButton('Кредитные карты', callback_data='button_credit_card')
    markup.add(button_loan, button_credit, button_credit_card)
    await bot.send_message(messsage.chat.id, "Привет!👋\nДля начала давай познакомимся\nМеня зовут – Займер-бот.\nЯ помогу подобрать для тебя самые выгодные условия:", reply_markup=markup)

@dp.callback_query_handler(lambda loan: loan.data == 'button_loan')
async def button_loan(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Займы')

@dp.callback_query_handler(lambda credit: credit.data == 'button_credit')
async def button_credit(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Credit')

@dp.callback_query_handler(lambda credit_card: credit_card.data == 'button_credit_card')
async def button_credit_card(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Credit_card')

@dp.message_handler(commands=['new_start'])
async def begin_2(message: types.Message):
    markup_2 = InlineKeyboardMarkup(row_width=2)
    button_russia = InlineKeyboardButton('Россия', callback_data='button_russia')
    button_kazakhstan = InlineKeyboardButton('Казахстан', callback_data='button_kazakhstan')
    button_belarus = InlineKeyboardButton('Беларусь', callback_data='button_belarus')
    button_ukraine = InlineKeyboardButton('Украина', callback_data='button_ukraine')
    markup_2.add(button_russia, button_kazakhstan, button_belarus, button_ukraine)
    await bot.send_message(message.chat.id, "Отлично!\nДавай приступим😊\nГражданином какой страны ты являешься?", reply_markup=markup_2)

@dp.callback_query_handler(lambda russia: russia.data == 'button_russia')
async def button_russia(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Russia')

@dp.callback_query_handler(lambda kazakhstan: kazakhstan.data == 'button_kazakhstan')
async def button_kazakhstan(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Kazakhstan')

@dp.callback_query_handler(lambda belarus: belarus.data == 'button_belarus')
async def button_belarus(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Belarus')

@dp.callback_query_handler(lambda ukraine: ukraine.data == 'button_ukraine')
async def button_ukraine(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,'Ukraine')

executor.start_polling(dp)