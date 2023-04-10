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
def paragraphs(call):
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


        if call.message:
            if call.data == 'paragraph_1':
                markup_1 = types.InlineKeyboardMarkup(row_width=1)
                conspect1 = types.InlineKeyboardButton('Конспект', callback_data='conspect_1')
                videourok1 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_1')
                task1 = types.InlineKeyboardButton('Задачи', callback_data='task_1')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_1.add(conspect1,videourok1,task1,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_1)
            elif call.data == 'paragraph_2':
                markup_2 = types.InlineKeyboardMarkup(row_width=1)
                conspect2 = types.InlineKeyboardButton('Конспект', callback_data='conspect_2')
                videourok2 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_2')
                task2 = types.InlineKeyboardButton('Задачи', callback_data='task_2')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_2.add(conspect2,videourok2,task2,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_2)
            elif call.data == 'paragraph_3':
                markup_3 = types.InlineKeyboardMarkup(row_width=1)
                conspect3 = types.InlineKeyboardButton('Конспект', callback_data='conspect_3')
                primerzadach3 = types.InlineKeyboardButton('Примеры решения задач', callback_data='primerzadach_3')
                videourok3 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_3')
                task3 = types.InlineKeyboardButton('Задачи', callback_data='task_3')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_3.add(conspect3,primerzadach3,videourok3,task3,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_3)
            elif call.data == 'paragraph_4':
                markup_4 = types.InlineKeyboardMarkup(row_width=1)
                conspect4 = types.InlineKeyboardButton('Конспект', callback_data='conspect_4')
                videourok4 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_4')
                task4 = types.InlineKeyboardButton('Задачи', callback_data='task_4')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_4.add(conspect4,videourok4,task4,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_4)
            elif call.data == 'paragraph_5':
                markup_5 = types.InlineKeyboardMarkup(row_width=1)
                conspect5 = types.InlineKeyboardButton('Конспект', callback_data='conspect_5')
                videourok5 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_5')
                task5 = types.InlineKeyboardButton('Задачи', callback_data='task_5')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_5.add(conspect5,videourok5,task5,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_5)
            elif call.data == 'paragraph_6':
                markup_6 = types.InlineKeyboardMarkup(row_width=1)
                conspect6 = types.InlineKeyboardButton('Конспект', callback_data='conspect_6')
                videourok6 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_6')
                task6 = types.InlineKeyboardButton('Задачи', callback_data='task_6')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_6.add(conspect6,videourok6,task6,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_6)
            elif call.data == 'paragraph_7':
                markup_7 = types.InlineKeyboardMarkup(row_width=1)
                conspect7 = types.InlineKeyboardButton('Конспект', callback_data='conspect_7')
                videourok7 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_7')
                task7 = types.InlineKeyboardButton('Задачи', callback_data='task_7')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_7.add(conspect7,videourok7,task7,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_7)
            elif call.data == 'paragraph_8':
                markup_8 = types.InlineKeyboardMarkup(row_width=1)
                conspect8 = types.InlineKeyboardButton('Конспект', callback_data='conspect_8')
                videourok8 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_8')
                task8 = types.InlineKeyboardButton('Задачи', callback_data='task_8')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_8.add(conspect8,videourok8,task8,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_8)
            elif call.data == 'paragraph_9':
                markup_9 = types.InlineKeyboardMarkup(row_width=1)
                conspect9 = types.InlineKeyboardButton('Конспект', callback_data='conspect_9')
                videourok9 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_9')
                task9 = types.InlineKeyboardButton('Задачи', callback_data='task_9')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_9.add(conspect9,videourok9,task9,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_9)
            elif call.data == 'paragraph_10':
                markup_10 = types.InlineKeyboardMarkup(row_width=1)
                conspect10 = types.InlineKeyboardButton('Конспект', callback_data='conspect_10')
                videourok10 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_10')
                task10 = types.InlineKeyboardButton('Задачи', callback_data='task_10')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_10.add(conspect10,videourok10,task10,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_10)
            elif call.data == 'paragraph_11':
                markup_11 = types.InlineKeyboardMarkup(row_width=1)
                conspect11 = types.InlineKeyboardButton('Конспект', callback_data='conspect_11')
                videourok11 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_11')
                task11 = types.InlineKeyboardButton('Задачи', callback_data='task_11')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_1')
                markup_11.add(conspect11,videourok11,task11,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_11)


            if call.data == 'paragraph_12':
                markup_12 = types.InlineKeyboardMarkup(row_width=1)
                conspect12 = types.InlineKeyboardButton('Конспект', callback_data='conspect_12')
                videourok12 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_12')
                task12 = types.InlineKeyboardButton('Задачи', callback_data='task_12')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_12.add(conspect12,videourok12,task12,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_12)
            elif call.data == 'paragraph_13':
                markup_13 = types.InlineKeyboardMarkup(row_width=1)
                conspect13 = types.InlineKeyboardButton('Конспект', callback_data='conspect_13')
                videourok13 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_13')
                task13 = types.InlineKeyboardButton('Задачи', callback_data='task_13')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_13.add(conspect13,videourok13,task13,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_13)
            elif call.data == 'paragraph_14':
                markup_14 = types.InlineKeyboardMarkup(row_width=1)
                conspect14 = types.InlineKeyboardButton('Конспект', callback_data='conspect_14')
                videourok14 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_14')
                task14 = types.InlineKeyboardButton('Задачи', callback_data='task_14')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_14.add(conspect14,videourok14,task14,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_14)
            elif call.data == 'paragraph_15':
                markup_15 = types.InlineKeyboardMarkup(row_width=1)
                conspect15 = types.InlineKeyboardButton('Конспект', callback_data='conspect_15')
                videourok15 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_15')
                task15 = types.InlineKeyboardButton('Задачи', callback_data='task_15')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_15.add(conspect15,videourok15,task15,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_15)
            elif call.data == 'paragraph_16':
                markup_16 = types.InlineKeyboardMarkup(row_width=1)
                conspect16 = types.InlineKeyboardButton('Конспект', callback_data='conspect_16')
                videourok16 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_16')
                task16 = types.InlineKeyboardButton('Задачи', callback_data='task_16')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_16.add(conspect16,videourok16,task16,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_16)
            elif call.data == 'paragraph_17':
                markup_17 = types.InlineKeyboardMarkup(row_width=1)
                conspect17 = types.InlineKeyboardButton('Конспект', callback_data='conspect_17')
                videourok17 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_17')
                task17 = types.InlineKeyboardButton('Задачи', callback_data='task_17')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_14.add(conspect17,videourok17,task17,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_17)
            elif call.data == 'paragraph_18':
                markup_18 = types.InlineKeyboardMarkup(row_width=1)
                conspect18 = types.InlineKeyboardButton('Конспект', callback_data='conspect_18')
                videourok18 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_18')
                task18 = types.InlineKeyboardButton('Задачи', callback_data='task_18')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_18.add(conspect18,videourok18,task18,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_18)
            elif call.data == 'paragraph_19':
                markup_19 = types.InlineKeyboardMarkup(row_width=1)
                conspect19 = types.InlineKeyboardButton('Конспект', callback_data='conspect_19')
                videourok19 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_19')
                task19 = types.InlineKeyboardButton('Задачи', callback_data='task_19')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_2')
                markup_19.add(conspect19,videourok19,task19,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_19)


            elif call.data == 'paragraph_20':
                markup_20 = types.InlineKeyboardMarkup(row_width=1)
                conspect20 = types.InlineKeyboardButton('Конспект', callback_data='conspect_20')
                videourok20 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_20')
                task20 = types.InlineKeyboardButton('Задачи', callback_data='task_20')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_3')
                markup_20.add(conspect20,videourok20,task20,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_20)
            elif call.data == 'paragraph_21':
                markup_21 = types.InlineKeyboardMarkup(row_width=1)
                conspect21 = types.InlineKeyboardButton('Конспект', callback_data='conspect_21')
                videourok21 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_21')
                task21 = types.InlineKeyboardButton('Задачи', callback_data='task_21')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_3')
                markup_21.add(conspect21,videourok21,task21,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_21)
            elif call.data == 'paragraph_22':
                markup_22 = types.InlineKeyboardMarkup(row_width=1)
                conspect22 = types.InlineKeyboardButton('Конспект', callback_data='conspect_22')
                videourok22 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_22')
                task22 = types.InlineKeyboardButton('Задачи', callback_data='task_22')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_3')
                markup_22.add(conspect22,videourok22,task22,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_22)


            if call.data == 'paragraph_23':
                markup_23 = types.InlineKeyboardMarkup(row_width=1)
                conspect23 = types.InlineKeyboardButton('Конспект', callback_data='conspect_23')
                videourok23 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_23')
                task23 = types.InlineKeyboardButton('Задачи', callback_data='task_23')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_23.add(conspect23,videourok23,task23,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_23)
            elif call.data == 'paragraph_24':
                markup_24 = types.InlineKeyboardMarkup(row_width=1)
                conspect24 = types.InlineKeyboardButton('Конспект', callback_data='conspect_24')
                videourok24 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_24')
                task24 = types.InlineKeyboardButton('Задачи', callback_data='task_24')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_24.add(conspect24,videourok24,task24,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_24)
            elif call.data == 'paragraph_25':
                markup_25 = types.InlineKeyboardMarkup(row_width=1)
                conspect25 = types.InlineKeyboardButton('Конспект', callback_data='conspect_25')
                videourok25 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_25')
                task25 = types.InlineKeyboardButton('Задачи', callback_data='task_25')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_25.add(conspect25,videourok25,task25,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_25)
            elif call.data == 'paragraph_26':
                markup_26 = types.InlineKeyboardMarkup(row_width=1)
                conspect26 = types.InlineKeyboardButton('Конспект', callback_data='conspect_26')
                videourok26 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_26')
                task26 = types.InlineKeyboardButton('Задачи', callback_data='task_26')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_26.add(conspect26,videourok26,task26,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_26)
            elif call.data == 'paragraph_27':
                markup_27 = types.InlineKeyboardMarkup(row_width=1)
                conspect27 = types.InlineKeyboardButton('Конспект', callback_data='conspect_27')
                videourok27 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_27')
                task27 = types.InlineKeyboardButton('Задачи', callback_data='task_27')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_27.add(conspect27,videourok27,task27,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_27)
            elif call.data == 'paragraph_28':
                markup_28 = types.InlineKeyboardMarkup(row_width=1)
                conspect28 = types.InlineKeyboardButton('Конспект', callback_data='conspect_28')
                videourok28 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_28')
                task28 = types.InlineKeyboardButton('Задачи', callback_data='task_28')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_28.add(conspect28,videourok28,task28,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_28)
            elif call.data == 'paragraph_29':
                markup_29 = types.InlineKeyboardMarkup(row_width=1)
                conspect29 = types.InlineKeyboardButton('Конспект', callback_data='conspect_29')
                videourok29 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_29')
                task29 = types.InlineKeyboardButton('Задачи', callback_data='task_29')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_29.add(conspect29,videourok29,task29,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_29)
            elif call.data == 'paragraph_30':
                markup_30 = types.InlineKeyboardMarkup(row_width=1)
                conspect30 = types.InlineKeyboardButton('Конспект', callback_data='conspect_30')
                videourok30 = types.InlineKeyboardButton('Видео-урок', callback_data='videourok_30')
                task30 = types.InlineKeyboardButton('Задачи', callback_data='task_30')
                back1 = types.InlineKeyboardButton('Назад', callback_data='theme_4')
                markup_30.add(conspect30,videourok30,task30,back1)
                bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markup_30)


            if call.message:
                if call.data == 'conspect_1':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_1')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-19.userapi.com/impg/slX9DbqscJxKAraZSIN8uSdxgljpHBcilS9Xnw/HyIi1OAh5Dg.jpg?size=1645x2122&quality=95&sign=799d51b03e58d813166f0ac9175622f3&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_2':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_2')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-52.userapi.com/impg/5kX92f2BkyUpb631oF6OYVIs3lijE26o2J9yvg/9VJwREZ4vmc.jpg?size=1527x2160&quality=96&sign=d839048c43e2ea3dd35a988b8b925d9d&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_3':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_3')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-34.userapi.com/impg/z6lK3B858L0nE8Zk8UbKhPvwgScxto8yFaJQ6g/-fD1krEFZhg.jpg?size=1527x2160&quality=95&sign=9ca8fc5ab20fd16b5f37ee1d722ef7e5&type=album', reply_markup=markup_1)
                elif call.data == 'primerzadach_3':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1) 
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_3')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-61.userapi.com/impg/OORWRPONILSls-VZM9kbj-DbTuXOkq-91j8WRg/kqyhMkuPWtM.jpg?size=1527x2160&quality=95&sign=399455a3d12d835200b0b046b65efd84&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_4':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_4')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_5':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_5')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_6':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_6')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-51.userapi.com/impg/WTCMbzv6_4e2YFJ3iQ6xk2fWfaoh-Axfz9AmqQ/7QRKVDoAtgI.jpg?size=1644x2032&quality=95&sign=52c5d86e66f977295da3569c9ff399e9&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_7':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_7')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_8':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_8')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_9':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_9')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_10':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_10')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_11':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_11')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                
                
                if call.data == 'conspect_12':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_12')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_13':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_13')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-19.userapi.com/impg/slX9DbqscJxKAraZSIN8uSdxgljpHBcilS9Xnw/HyIi1OAh5Dg.jpg?size=1645x2122&quality=95&sign=799d51b03e58d813166f0ac9175622f3&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_14':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_14')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-52.userapi.com/impg/5kX92f2BkyUpb631oF6OYVIs3lijE26o2J9yvg/9VJwREZ4vmc.jpg?size=1527x2160&quality=96&sign=d839048c43e2ea3dd35a988b8b925d9d&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_15':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_15')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_16':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_16')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_17':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_17')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_18':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_18')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_19':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_19')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)

                
                if call.data == 'conspect_20':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_20')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_21':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_21')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_22':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_22')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)


                if call.data == 'conspect_23':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_23')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-19.userapi.com/impg/slX9DbqscJxKAraZSIN8uSdxgljpHBcilS9Xnw/HyIi1OAh5Dg.jpg?size=1645x2122&quality=95&sign=799d51b03e58d813166f0ac9175622f3&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_24':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_24')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-52.userapi.com/impg/5kX92f2BkyUpb631oF6OYVIs3lijE26o2J9yvg/9VJwREZ4vmc.jpg?size=1527x2160&quality=96&sign=d839048c43e2ea3dd35a988b8b925d9d&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_25':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_25')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_26':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_26')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_27':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_27')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_28':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_28')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_29':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_29')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
                elif call.data == 'conspect_30':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_30')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)



            if call.message:
                if call.data == 'videourok_1':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    video1 =  types.InlineKeyboardButton('Перейти к видеоуроку', url = 'https://youtu.be/eZy2wp5XINY' )
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_1')
                    markup_1.add(video1, back1)
                    bot.send_message(call.message.chat.id, '''Видеоурок по теме "Механическое движение" доступен по кнопке ниже:''', reply_markup=markup_1)
                elif call.data == 'videourok_2':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    video2 = types.InlineKeyboardButton('Перейти к видеоуроку', url = 'https://youtu.be/I_u9Ut-g-q4')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_2')
                    markup_1.add(video2, back1)
                    bot.send_message(call.message.chat.id, '''Видеоурок по теме "Траектория,путь,перемещение" доступен по кнопке ниже:''', reply_markup=markup_1)
                elif call.data == 'videourok_3':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_3')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_4':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_4')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_5':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_5')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_6':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_6')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_7':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_7')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_8':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_8')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_9':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_9')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_10':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_10')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_11':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_11')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                

                if call.data == 'videourok_12':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_12')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_13':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_13')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_14':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_14')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_15':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_15')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_16':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_16')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_17':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_17')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_18':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_18')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_19':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_19')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)




                if call.data == 'videourok_20':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_20')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_21':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_21')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_22':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_22')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                 

                if call.data == 'videourok_23':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_23')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_24':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_24')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_25':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_25')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_26':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_26')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_27':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_27')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_28':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_28')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_29':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_29')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)
                elif call.data == 'videourok_30':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_30')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album', reply_markup=markup_1)



            if call.message:
                if call.data == 'task_1':
                    user = call.message.chat.id
                    markup_realtask1 = types.InlineKeyboardMarkup(row_width=2)
                    realtask1_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_1_1')
                    realtask1_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_1_2')
                    realtask1_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_1_3')
                    realtask1_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_1_4')
                    realtask1_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_1_5')
                    realtask1_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_1_6')
                    realtask1_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_1_7')
                    realtask1_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_1_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_1')
                    markup_realtask1.add(realtask1_1,realtask1_2,realtask1_3,realtask1_4,realtask1_5,realtask1_6,realtask1_7,realtask1_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask1)
                elif call.data == 'task_2':
                    user = call.message.chat.id
                    markup_realtask2 = types.InlineKeyboardMarkup(row_width=2)
                    realtask2_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_2_1')
                    realtask2_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_2_2')
                    realtask2_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_2_3')
                    realtask2_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_2_4')
                    realtask2_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_2_5')
                    realtask2_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_2_6')
                    realtask2_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_2_7')
                    realtask2_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_2_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_2')
                    markup_realtask2.add(realtask2_1,realtask2_2,realtask2_3,realtask2_4,realtask2_5,realtask2_6,realtask2_7,realtask2_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask2)
                elif call.data == 'task_3':
                    user = call.message.chat.id
                    markup_realtask3 = types.InlineKeyboardMarkup(row_width=2)
                    realtask3_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_3_1')
                    realtask3_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_3_2')
                    realtask3_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_3_3')
                    realtask3_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_3_4')
                    realtask3_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_3_5')
                    realtask3_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_3_6')
                    realtask3_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_3_7')
                    realtask3_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_3_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_3')
                    markup_realtask3.add(realtask3_1,realtask3_2,realtask3_3,realtask3_4,realtask3_5,realtask3_6,realtask3_7,realtask3_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask3)
                elif call.data == 'task_4':
                    user = call.message.chat.id
                    markup_realtask4 = types.InlineKeyboardMarkup(row_width=2)
                    realtask4_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_4_1')
                    realtask4_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_4_2')
                    realtask4_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_4_3')
                    realtask4_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_4_4')
                    realtask4_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_4_5')
                    realtask4_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_4_6')
                    realtask4_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_4_7')
                    realtask4_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_4_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_4')
                    markup_realtask4.add(realtask4_1,realtask4_2,realtask4_3,realtask4_4,realtask4_5,realtask4_6,realtask4_7,realtask4_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask4)
                elif call.data == 'task_5':
                    user = call.message.chat.id
                    markup_realtask5 = types.InlineKeyboardMarkup(row_width=2)
                    realtask5_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_5_1')
                    realtask5_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_5_2')
                    realtask5_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_5_3')
                    realtask5_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_5_4')
                    realtask5_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_5_5')
                    realtask5_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_5_6')
                    realtask5_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_5_7')
                    realtask5_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_5_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_5')
                    markup_realtask5.add(realtask5_1,realtask5_2,realtask5_3,realtask5_4,realtask5_5,realtask5_6,realtask5_7,realtask5_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask5)
                elif call.data == 'task_6':
                    user = call.message.chat.id
                    markup_realtask6 = types.InlineKeyboardMarkup(row_width=2)
                    realtask6_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_6_1')
                    realtask6_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_6_2')
                    realtask6_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_6_3')
                    realtask6_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_6_4')
                    realtask6_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_6_5')
                    realtask6_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_6_6')
                    realtask6_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_6_7')
                    realtask6_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_6_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_6')
                    markup_realtask6.add(realtask6_1,realtask6_2,realtask6_3,realtask6_4,realtask6_5,realtask6_6,realtask6_7,realtask6_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask6)
                elif call.data == 'task_7':
                    user = call.message.chat.id
                    markup_realtask7 = types.InlineKeyboardMarkup(row_width=2)
                    realtask7_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_7_1')
                    realtask7_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_7_2')
                    realtask7_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_7_3')
                    realtask7_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_7_4')
                    realtask7_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_7_5')
                    realtask7_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_7_6')
                    realtask7_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_7_7')
                    realtask7_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_7_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_7')
                    markup_realtask7.add(realtask7_1,realtask7_2,realtask7_3,realtask7_4,realtask7_5,realtask7_6,realtask7_7,realtask7_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask7)
                elif call.data == 'task_8':
                    user = call.message.chat.id
                    markup_realtask8 = types.InlineKeyboardMarkup(row_width=2)
                    realtask8_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_8_1')
                    realtask8_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_8_2')
                    realtask8_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_8_3')
                    realtask8_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_8_4')
                    realtask8_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_8_5')
                    realtask8_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_8_6')
                    realtask8_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_8_7')
                    realtask8_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_8_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_8')
                    markup_realtask8.add(realtask8_1,realtask8_2,realtask8_3,realtask8_4,realtask8_5,realtask8_6,realtask8_7,realtask8_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask8)
                elif call.data == 'task_9':
                    user = call.message.chat.id
                    markup_realtask9 = types.InlineKeyboardMarkup(row_width=2)
                    realtask9_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_9_1')
                    realtask9_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_9_2')
                    realtask9_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_9_3')
                    realtask9_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_9_4')
                    realtask9_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_9_5')
                    realtask9_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_9_6')
                    realtask9_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_9_7')
                    realtask9_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_9_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_9')
                    markup_realtask9.add(realtask9_1,realtask9_2,realtask9_3,realtask9_4,realtask9_5,realtask9_6,realtask9_7,realtask9_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask9)
                elif call.data == 'task_10':
                    user = call.message.chat.id
                    markup_realtask10 = types.InlineKeyboardMarkup(row_width=2)
                    realtask10_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_10_1')
                    realtask10_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_10_2')
                    realtask10_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_10_3')
                    realtask10_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_10_4')
                    realtask10_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_10_5')
                    realtask10_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_10_6')
                    realtask10_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_10_7')
                    realtask10_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_10_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_10')
                    markup_realtask10.add(realtask10_1,realtask10_2,realtask10_3,realtask10_4,realtask10_5,realtask10_6,realtask10_7,realtask10_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask10)
                elif call.data == 'task_11':
                    user = call.message.chat.id
                    markup_realtask11 = types.InlineKeyboardMarkup(row_width=2)
                    realtask11_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_11_1')
                    realtask11_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_11_2')
                    realtask11_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_11_3')
                    realtask11_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_11_4')
                    realtask11_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_11_5')
                    realtask11_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_11_6')
                    realtask11_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_11_7')
                    realtask11_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_11_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_11')
                    markup_realtask11.add(realtask11_1,realtask11_2,realtask11_3,realtask11_4,realtask11_5,realtask11_6,realtask11_7,realtask11_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask11)


                if call.data == 'task_12':
                    user = call.message.chat.id
                    markup_realtask12 = types.InlineKeyboardMarkup(row_width=2)
                    realtask12_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_12_1')
                    realtask12_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_12_2')
                    realtask12_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_12_3')
                    realtask12_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_12_4')
                    realtask12_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_12_5')
                    realtask12_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_12_6')
                    realtask12_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_12_7')
                    realtask12_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_12_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_12')
                    markup_realtask12.add(realtask12_1,realtask12_2,realtask12_3,realtask12_4,realtask12_5,realtask12_6,realtask12_7,realtask12_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask12)
                elif call.data == 'task_13':
                    user = call.message.chat.id
                    markup_realtask13 = types.InlineKeyboardMarkup(row_width=2)
                    realtask13_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_13_1')
                    realtask13_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_13_2')
                    realtask13_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_13_3')
                    realtask13_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_13_4')
                    realtask13_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_13_5')
                    realtask13_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_13_6')
                    realtask13_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_13_7')
                    realtask13_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_13_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_13')
                    markup_realtask13.add(realtask13_1,realtask13_2,realtask13_3,realtask13_4,realtask13_5,realtask13_6,realtask13_7,realtask13_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask13)
                elif call.data == 'task_14':
                    user = call.message.chat.id
                    markup_realtask14 = types.InlineKeyboardMarkup(row_width=2)
                    realtask14_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_14_1')
                    realtask14_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_14_2')
                    realtask14_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_14_3')
                    realtask14_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_14_4')
                    realtask14_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_14_5')
                    realtask14_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_14_6')
                    realtask14_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_14_7')
                    realtask14_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_14_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_14')
                    markup_realtask14.add(realtask14_1,realtask14_2,realtask14_3,realtask14_4,realtask14_5,realtask14_6,realtask14_7,realtask14_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask14)
                elif call.data == 'task_15':
                    user = call.message.chat.id
                    markup_realtask15 = types.InlineKeyboardMarkup(row_width=2)
                    realtask15_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_15_1')
                    realtask15_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_15_2')
                    realtask15_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_15_3')
                    realtask15_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_15_4')
                    realtask15_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_15_5')
                    realtask15_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_15_6')
                    realtask15_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_15_7')
                    realtask15_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_15_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_15')
                    markup_realtask15.add(realtask15_1,realtask15_2,realtask15_3,realtask15_4,realtask15_5,realtask15_6,realtask15_7,realtask15_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask15)
                elif call.data == 'task_16':
                    user = call.message.chat.id
                    markup_realtask16 = types.InlineKeyboardMarkup(row_width=2)
                    realtask16_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_16_1')
                    realtask16_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_16_2')
                    realtask16_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_16_3')
                    realtask16_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_16_4')
                    realtask16_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_16_5')
                    realtask16_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_16_6')
                    realtask16_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_16_7')
                    realtask16_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_16_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_16')
                    markup_realtask16.add(realtask16_1,realtask16_2,realtask16_3,realtask16_4,realtask16_5,realtask16_6,realtask16_7,realtask16_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask16)
                elif call.data == 'task_17':
                    user = call.message.chat.id
                    markup_realtask17 = types.InlineKeyboardMarkup(row_width=2)
                    realtask17_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_17_1')
                    realtask17_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_17_2')
                    realtask17_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_17_3')
                    realtask17_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_17_4')
                    realtask17_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_17_5')
                    realtask17_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_17_6')
                    realtask17_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_17_7')
                    realtask17_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_17_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_17')
                    markup_realtask17.add(realtask17_1,realtask17_2,realtask17_3,realtask17_4,realtask17_5,realtask17_6,realtask17_7,realtask17_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask17)
                elif call.data == 'task_18':
                    user = call.message.chat.id
                    markup_realtask18 = types.InlineKeyboardMarkup(row_width=2)
                    realtask18_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_18_1')
                    realtask18_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_18_2')
                    realtask18_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_18_3')
                    realtask18_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_18_4')
                    realtask18_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_18_5')
                    realtask18_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_18_6')
                    realtask18_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_18_7')
                    realtask18_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_18_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_18')
                    markup_realtask18.add(realtask18_1,realtask18_2,realtask18_3,realtask18_4,realtask18_5,realtask18_6,realtask18_7,realtask18_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask18)
                elif call.data == 'task_19':
                    user = call.message.chat.id
                    markup_realtask19 = types.InlineKeyboardMarkup(row_width=2)
                    realtask19_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_19_1')
                    realtask19_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_19_2')
                    realtask19_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_19_3')
                    realtask19_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_19_4')
                    realtask19_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_19_5')
                    realtask19_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_19_6')
                    realtask19_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_19_7')
                    realtask19_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_19_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_19')
                    markup_realtask19.add(realtask19_1,realtask19_2,realtask19_3,realtask19_4,realtask19_5,realtask19_6,realtask19_7,realtask19_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask19)
              

                if call.data == 'task_20':
                    user = call.message.chat.id
                    markup_realtask20 = types.InlineKeyboardMarkup(row_width=2)
                    realtask20_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_20_1')
                    realtask20_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_20_2')
                    realtask20_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_20_3')
                    realtask20_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_20_4')
                    realtask20_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_20_5')
                    realtask20_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_20_6')
                    realtask20_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_20_7')
                    realtask20_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_20_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_20')
                    markup_realtask20.add(realtask20_1,realtask20_2,realtask20_3,realtask20_4,realtask20_5,realtask20_6,realtask20_7,realtask20_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask20)
                elif call.data == 'task_21':
                    user = call.message.chat.id
                    markup_realtask21 = types.InlineKeyboardMarkup(row_width=2)
                    realtask21_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_21_1')
                    realtask21_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_21_2')
                    realtask21_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_21_3')
                    realtask21_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_21_4')
                    realtask21_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_21_5')
                    realtask21_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_21_6')
                    realtask21_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_21_7')
                    realtask21_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_21_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_21')
                    markup_realtask21.add(realtask21_1,realtask21_2,realtask21_3,realtask21_4,realtask21_5,realtask21_6,realtask21_7,realtask21_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask21)
                elif call.data == 'task_22':
                    user = call.message.chat.id
                    markup_realtask22 = types.InlineKeyboardMarkup(row_width=2)
                    realtask22_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_22_1')
                    realtask22_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_22_2')
                    realtask22_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_22_3')
                    realtask22_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_22_4')
                    realtask22_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_22_5')
                    realtask22_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_22_6')
                    realtask22_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_22_7')
                    realtask22_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_22_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_22')
                    markup_realtask22.add(realtask22_1,realtask22_2,realtask22_3,realtask22_4,realtask22_5,realtask22_6,realtask22_7,realtask22_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask22)
              

                if call.data == 'task_23':
                    user = call.message.chat.id
                    markup_realtask23 = types.InlineKeyboardMarkup(row_width=2)
                    realtask23_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_23_1')
                    realtask23_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_23_2')
                    realtask23_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_23_3')
                    realtask23_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_23_4')
                    realtask23_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_23_5')
                    realtask23_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_23_6')
                    realtask23_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_23_7')
                    realtask23_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_23_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_23')
                    markup_realtask23.add(realtask23_1,realtask23_2,realtask23_3,realtask23_4,realtask23_5,realtask23_6,realtask23_7,realtask23_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask23)
                elif call.data == 'task_24':
                    user = call.message.chat.id
                    markup_realtask24 = types.InlineKeyboardMarkup(row_width=2)
                    realtask24_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_24_1')
                    realtask24_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_24_2')
                    realtask24_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_24_3')
                    realtask24_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_24_4')
                    realtask24_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_24_5')
                    realtask24_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_24_6')
                    realtask24_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_24_7')
                    realtask24_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_24_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_24')
                    markup_realtask24.add(realtask24_1,realtask24_2,realtask24_3,realtask24_4,realtask24_5,realtask24_6,realtask24_7,realtask24_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask24)
                elif call.data == 'task_25':
                    user = call.message.chat.id
                    markup_realtask25 = types.InlineKeyboardMarkup(row_width=2)
                    realtask25_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_25_1')
                    realtask25_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_25_2')
                    realtask25_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_25_3')
                    realtask25_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_25_4')
                    realtask25_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_25_5')
                    realtask25_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_25_6')
                    realtask25_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_25_7')
                    realtask25_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_25_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_25')
                    markup_realtask25.add(realtask25_1,realtask25_2,realtask25_3,realtask25_4,realtask25_5,realtask25_6,realtask25_7,realtask25_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask25)
                elif call.data == 'task_26':
                    user = call.message.chat.id
                    markup_realtask26 = types.InlineKeyboardMarkup(row_width=2)
                    realtask26_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_26_1')
                    realtask26_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_26_2')
                    realtask26_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_26_3')
                    realtask26_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_26_4')
                    realtask26_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_26_5')
                    realtask26_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_26_6')
                    realtask26_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_26_7')
                    realtask26_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_26_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_26')
                    markup_realtask26.add(realtask26_1,realtask26_2,realtask26_3,realtask26_4,realtask26_5,realtask26_6,realtask26_7,realtask26_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask26)
                elif call.data == 'task_27':
                    user = call.message.chat.id
                    markup_realtask27 = types.InlineKeyboardMarkup(row_width=2)
                    realtask27_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_27_1')
                    realtask27_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_27_2')
                    realtask27_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_27_3')
                    realtask27_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_27_4')
                    realtask27_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_27_5')
                    realtask27_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_27_6')
                    realtask27_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_27_7')
                    realtask27_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_27_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_27')
                    markup_realtask27.add(realtask27_1,realtask27_2,realtask27_3,realtask27_4,realtask27_5,realtask27_6,realtask27_7,realtask27_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask27)
                elif call.data == 'task_28':
                    user = call.message.chat.id
                    markup_realtask28 = types.InlineKeyboardMarkup(row_width=2)
                    realtask28_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_28_1')
                    realtask28_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_28_2')
                    realtask28_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_28_3')
                    realtask28_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_28_4')
                    realtask28_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_28_5')
                    realtask28_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_28_6')
                    realtask28_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_28_7')
                    realtask28_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_28_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_28')
                    markup_realtask28.add(realtask28_1,realtask28_2,realtask28_3,realtask28_4,realtask28_5,realtask28_6,realtask28_7,realtask28_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask28)
                elif call.data == 'task_29':
                    user = call.message.chat.id
                    markup_realtask29 = types.InlineKeyboardMarkup(row_width=2)
                    realtask29_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_29_1')
                    realtask29_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_29_2')
                    realtask29_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_29_3')
                    realtask29_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_29_4')
                    realtask29_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_29_5')
                    realtask29_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_29_6')
                    realtask29_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_29_7')
                    realtask29_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_29_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_29')
                    markup_realtask29.add(realtask29_1,realtask29_2,realtask29_3,realtask29_4,realtask29_5,realtask29_6,realtask29_7,realtask29_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask29)
                elif call.data == 'task_30':
                    user = call.message.chat.id
                    markup_realtask30 = types.InlineKeyboardMarkup(row_width=2)
                    realtask30_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_30_1')
                    realtask30_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_30_2')
                    realtask30_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_30_3')
                    realtask30_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_30_4')
                    realtask30_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_30_5')
                    realtask30_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_30_6')
                    realtask30_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_30_7')
                    realtask30_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_30_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_30')
                    markup_realtask30.add(realtask30_1,realtask30_2,realtask30_3,realtask30_4,realtask30_5,realtask30_6,realtask30_7,realtask30_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask30)



            #if call.message:
                #if call.data == 'realtask_1_1':

              
              
bot.polling(none_stop=True)
