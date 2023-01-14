import telebot
from telebot import types

token = "5833332883:AAEEkix40TB1s8BJewF4UIzhykDJ5rUTQCE"
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    name = message.from_user.first_name
    bot.send_message(chat_id, text=('''Здравствуй,'''+' '+name+'''! :-)
Это бот, разработанный учениками школы 1561, в котором собраны краткие конспекты, видео-уроки и дополнительные задания по физике!
Для вызова нашей библиотеки используй команду /assortment.'''))

@bot.message_handler(commands=['assortment'])
def assortment(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    theme0 = types.InlineKeyboardButton('Что такое механика?', callback_data='theme_0')
    theme1 = types.InlineKeyboardButton('Кинематика', callback_data='theme_1')
    theme2 = types.InlineKeyboardButton('Динамика', callback_data='theme_2')
    theme3 = types.InlineKeyboardButton('Статика', callback_data='theme_3')
    theme4 = types.InlineKeyboardButton('Законы сохранения в механике', callback_data='theme_4')
    markup.add(theme0, theme1, theme2, theme3, theme4)

    bot.send_message(message.chat.id, 'Выбери главу:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def undersortment(call):
    if call.message:
        if call.data == 'theme_0':
            user = call.message.chat.id
            markup0 = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
            markup0.add(back)
            bot.send_photo(user, 'https://sun9-38.userapi.com/impg/uZVjjRZXQsJ15txHmixOclsq_Fwp-SRlDtY7XQ/5rsD01q3n6w.jpg?size=1280x1198&quality=95&sign=fc7415730078f90988e0aa61eab792cf&type=album',reply_markup=markup0)
        elif call.data == 'theme_1':
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            paragraph1 = types.InlineKeyboardButton('Механическое движение', callback_data='paragraph_1')
            paragraph2 = types.InlineKeyboardButton('Траектория,путь,перемещение', callback_data='paragraph_2')
            paragraph3 = types.InlineKeyboardButton('Скорость равномер.прямолин.движения', callback_data='paragraph_3')
            paragraph4 = types.InlineKeyboardButton('Сложение скоростей', callback_data='paragraph_4')
            paragraph5 = types.InlineKeyboardButton('Скорость при неравномер. движении', callback_data='paragraph_5')
            paragraph6 = types.InlineKeyboardButton('Ускорение', callback_data='paragraph_6')
            paragraph7 = types.InlineKeyboardButton('Перемещение при прямолин.равноускор.движении', callback_data='paragraph_7')
            paragraph8 = types.InlineKeyboardButton('Свободное падение тел', callback_data='paragraph_8')
            paragraph9 = types.InlineKeyboardButton('Движение тел,брошенных под углом к горизонту',  callback_data='paragraph_9')
            paragraph10 = types.InlineKeyboardButton('Равномер.движение по окружности', callback_data = 'paragraph_10')
            paragraph11 = types.InlineKeyboardButton('Центростремительное ускорение', callback_data = 'paragraph_11')
            back = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
            markup1.add(paragraph1, paragraph2, paragraph3, paragraph4, paragraph5, paragraph6, paragraph7, paragraph8, paragraph9, paragraph10, paragraph11, back)
            bot.send_message(call.message.chat.id, '''Выбери параграф из раздела "Кинематика":''', reply_markup=markup1)
        elif call.data == 'theme_2':
            markup2 = types.InlineKeyboardMarkup(row_width=1)
            paragraph12 = types.InlineKeyboardButton('1-й закон Ньютона', callback_data='paragraph_12')
            paragraph13 = types.InlineKeyboardButton('Сила', callback_data='paragraph_13')
            paragraph14 = types.InlineKeyboardButton('2-й закон Ньютона', callback_data='paragraph_14')
            paragraph15 = types.InlineKeyboardButton('3-й закон Ньютона', callback_data='paragraph_15')
            paragraph16 = types.InlineKeyboardButton('Закон всемирного тяготения', callback_data='paragraph_16')
            paragraph17 = types.InlineKeyboardButton('Вес.Невесомость.Перегрузка', callback_data='paragraph_17')
            paragraph18 = types.InlineKeyboardButton('1-я космическая скорость', callback_data='paragraph_18')
            paragraph19 = types.InlineKeyboardButton('Сила трения', callback_data='paragraph_19')
            back = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
            markup2.add(paragraph12, paragraph13, paragraph14, paragraph15, paragraph16, paragraph17, paragraph18, paragraph19, back)
            bot.send_message(call.message.chat.id, '''Выбери параграф из раздела "Динамика":''', reply_markup=markup2)
        elif call.data == 'theme_3':
            markup3 = types.InlineKeyboardMarkup(row_width=1)
            paragraph20 = types.InlineKeyboardButton('Условия равновесия тел', callback_data='paragraph_20')
            paragraph21 = types.InlineKeyboardButton('Центр тяжести', callback_data='paragraph_21')
            paragraph22 = types.InlineKeyboardButton('Виды равновесия.Устойчивость тел', callback_data='paragraph_22')
            back = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
            markup3.add(paragraph20, paragraph21, paragraph22, back)
            bot.send_message(call.message.chat.id, '''Выбери параграф из раздела "Статика":''', reply_markup=markup3)
        elif call.data == 'theme_4':
            markup4 = types.InlineKeyboardMarkup(row_width=1)
            paragraph23 = types.InlineKeyboardButton('Импульс тела', callback_data='paragraph_23')
            paragraph24 = types.InlineKeyboardButton('Закон сохранения импульса', callback_data='paragraph_24')
            paragraph25 = types.InlineKeyboardButton('Реактивное движение', callback_data='paragraph_25')
            paragraph26 = types.InlineKeyboardButton('Механическая работа.Мощность', callback_data='paragraph_26')
            paragraph27 = types.InlineKeyboardButton('Кинетическая энергия тела', callback_data='paragraph_27')
            paragraph28 = types.InlineKeyboardButton('Рябота силы тяжести.Потенц.энергия', callback_data='paragraph_28')
            paragraph29 = types.InlineKeyboardButton('Работа силы упругости', callback_data='paragraph_29')
            paragraph30 = types.InlineKeyboardButton('Закон сохранения механич.энергии', callback_data='paragraph_30')
            back = types.InlineKeyboardButton('Назад', callback_data='back_to_menu')
            markup4.add(paragraph23, paragraph24, paragraph25, paragraph26, paragraph27, paragraph28, paragraph29, paragraph30, back)
            bot.send_message(call.message.chat.id, '''Выбери параграф из раздела "Законы сохранения в механике":''', reply_markup=markup4)
        
        elif call.data == 'back_to_menu':
            assortment(call.message)


        if call.data == 'paragraph_1':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-19.userapi.com/impg/slX9DbqscJxKAraZSIN8uSdxgljpHBcilS9Xnw/HyIi1OAh5Dg.jpg?size=1645x2122&quality=95&sign=799d51b03e58d813166f0ac9175622f3&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_2':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-52.userapi.com/impg/5kX92f2BkyUpb631oF6OYVIs3lijE26o2J9yvg/9VJwREZ4vmc.jpg?size=1527x2160&quality=96&sign=d839048c43e2ea3dd35a988b8b925d9d&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_3':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_4':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_5':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_6':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_7':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_8':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_9':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_10':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        elif call.data == 'paragraph_11':
            user = call.message.chat.id
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
            markup_1.add(back1)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
        

        if call.data == 'paragraph_12':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_13':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_14':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_15':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_16':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_17':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_18':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)
        elif call.data == 'paragraph_19':
            user = call.message.chat.id
            markup_2 = types.InlineKeyboardMarkup(row_width=1)
            back2 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
            markup_2.add(back2)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_2)


        if call.data == 'paragraph_20':
            user = call.message.chat.id
            markup_3 = types.InlineKeyboardMarkup(row_width=1)
            back3 = types.InlineKeyboardButton('Назад', callback_data='theme_3')
            markup_3.add(back3)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_3)
        elif call.data == 'paragraph_21':
            user = call.message.chat.id
            markup_3 = types.InlineKeyboardMarkup(row_width=1)
            back3 = types.InlineKeyboardButton('Назад', callback_data='theme_3')
            markup_3.add(back3)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_3)
        elif call.data == 'paragraph_22':
            user = call.message.chat.id
            markup_3 = types.InlineKeyboardMarkup(row_width=1)
            back3 = types.InlineKeyboardButton('Назад', callback_data='theme_3')
            markup_3.add(back3)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_3)


        if call.data == 'paragraph_23':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_24':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_25':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_26':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_27':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_28':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_29':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)
        elif call.data == 'paragraph_30':
            user = call.message.chat.id
            markup_4 = types.InlineKeyboardMarkup(row_width=1)
            back4 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
            markup_4.add(back4)
            bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album',reply_markup=markup_4)


bot.polling(none_stop=True)