import telebot
import sqlite3
from telebot import types

main_dict = {}

token = '5094128473:AAFB7VdacZhqz9mPkxghcPEMqwahu8d5OOk'

bot = telebot.TeleBot(token)

db = sqlite3.connect('../homework_bot_database.db', check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS info (
    user_id BIGINT,
    rooms_count INT,
    total_area FLOAT,
    total_volume FLOAT
)""")
db.commit()


@bot.message_handler(commands=['start', 'menu'])
def start_menu(message):
    murkup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Записать данные', callback_data='writing')
    item_no = types.InlineKeyboardButton(text='Вывод результата', callback_data='output')

    murkup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Здравствуйте. С помощью данного бота "
                                      "вы можете 'рассчитать' ваш дом.\n"
                                      "Выберите действие.", reply_markup=murkup_inline)


@bot.message_handler(commands=['commit'])
def commit(message):
    sql.execute("INSERT INTO info VALUES (?, ?, ?, ?)",
                (main_dict[message.chat.id]['id'], main_dict[message.chat.id]['rooms'],
                 main_dict[message.chat.id]['total_area'], main_dict[message.chat.id]['total_volume']))
    db.commit()
    bot.send_message(message.chat.id, "Данные успешно записаны.\n"
                                      "Для перехода в меню введите \n"
                                      "'/menu'")


@bot.callback_query_handler(func=lambda call: True)
def question(call):
    if call.data == 'writing':
        main_dict[call.message.chat.id] = {'id': call.message.chat.id,
                                           'room_length': 0,
                                           'room_width': 0,
                                           'room_height': 0,
                                           'room_area': 0,
                                           'room_volume': 0,
                                           'total_area': 0,
                                           'total_volume': 0,
                                           'rooms': 0,
                                           'total_height': 0,
                                           'length_counter': 1,
                                           'width_counter': 1,
                                           'height_counter': 1, }

        sql.execute("DELETE FROM info WHERE user_id = ?", (main_dict[call.message.chat.id]['id'],))
        db.commit()
        msg = bot.send_message(call.message.chat.id, "Начнем, введите количество комнат")
        bot.register_next_step_handler(msg, rooms_count)
    elif call.data == 'output':
        try:
            sql.execute("SELECT * FROM info WHERE user_id = ?",
                        (main_dict[call.message.chat.id]['id'],))
            all_results = sql.fetchone()
            db.commit()
            bot.send_message(call.message.chat.id, f"Полученные значения:\n"
                                                   f"\n"
                                                   f"Количесво комнат: {all_results[1]}\n"
                                                   f"Общая площадь: {all_results[2]} м²\n"
                                                   f"Общий объем: {all_results[3]} м³")
        except TypeError:
            bot.send_message(call.message.chat.id, "Нет данных")

    bot.answer_callback_query(callback_query_id=call.id)


def rooms_count(message):
    try:
        main_dict[message.chat.id]['rooms'] = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Вы ввели не целое число!!!!\n"
                                          "Повторите ввод.")
        bot.register_next_step_handler(message, rooms_count)
        return
    bot.send_message(message.chat.id, "Необходимо ввести длину, ширину и высоту "
                                      "каждой комнаты.\n"
                                      "Введите длину 1й комнаты:")
    bot.register_next_step_handler(message, length)


def length(message):
    try:
        main_dict[message.chat.id]['room_length'] = float(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Вы ввели не число!!!!\n"
                                          "Повторите ввод.")
        bot.register_next_step_handler(message, length)
    main_dict[message.chat.id]['length_counter'] += 1

    bot.send_message(message.chat.id, f"Введите ширину {main_dict[message.chat.id]['width_counter']}й комнаты:")
    bot.register_next_step_handler(message, width)
    

def width(message):
    try:
        main_dict[message.chat.id]['width_counter'] += 1
        main_dict[message.chat.id]['room_width'] = float(message.text)
        main_dict[message.chat.id]['room_area'] = \
            main_dict[message.chat.id]['room_length'] * main_dict[message.chat.id]['room_width']
        main_dict[message.chat.id]['total_area'] += main_dict[message.chat.id]['room_area']

        bot.send_message(message.chat.id, f"Введите высоту"
                                          f" {main_dict[message.chat.id]['height_counter']}й комнаты:")
        bot.register_next_step_handler(message, height)
    except ValueError:
        main_dict[message.chat.id]['width_counter'] -= 1
        bot.send_message(message.chat.id, "Вы ввели не число!!!!\n"
                                          "Повторите ввод.")
        bot.register_next_step_handler(message, width)


def height(message):
    if main_dict[message.chat.id]['length_counter'] == main_dict[message.chat.id]['rooms'] + 1:
        main_dict[message.chat.id]['room_height'] = float(message.text)
        main_dict[message.chat.id]['room_volume'] = \
            main_dict[message.chat.id]['room_area'] * main_dict[message.chat.id]['room_height']
        main_dict[message.chat.id]['total_volume'] += main_dict[message.chat.id]['room_volume']
        bot.send_message(message.chat.id, "Проверьте введенные данные!\n "
                                          "Если вы допустили ошибку, вернитесь обратно"
                                          "и повторите сначала '/menu'\n"
                                          "Для подтверждения данных\n"
                                          "НАЖМИТЕ '/commit'")
        return
    try:
        main_dict[message.chat.id]['height_counter'] += 1
        main_dict[message.chat.id]['room_height'] = float(message.text)
        main_dict[message.chat.id]['room_volume'] = \
            main_dict[message.chat.id]['room_area'] * main_dict[message.chat.id]['room_height']
        main_dict[message.chat.id]['total_volume'] += main_dict[message.chat.id]['room_volume']

        bot.send_message(message.chat.id, f"Введите длину {main_dict[message.chat.id]['length_counter']}й комнаты:")
        bot.register_next_step_handler(message, length)
    except ValueError:
        main_dict[message.chat.id]['height_counter'] -= 1
        bot.send_message(message.chat.id, "Вы ввели не число!!!!\n"
                                          "Повторите ввод.")
        bot.register_next_step_handler(message, height)


bot.infinity_polling()
