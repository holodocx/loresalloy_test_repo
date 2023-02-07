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
                    bot.send_photo(user,'https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album', reply_markup=markup_1)
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
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_1')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_2':
                    user = call.message.chat.id
                    markup_realtask2 = types.InlineKeyboardMarkup(row_width=1)
                    realtask2_1 = types.InlineKeyboardButton('Задача 1.', callback_data='realtask_2_1')
                    realtask2_2 = types.InlineKeyboardButton('Задача 2.', callback_data='realtask_2_2')
                    realtask2_3 = types.InlineKeyboardButton('Задача 3.', callback_data='realtask_2_3')
                    realtask2_4 = types.InlineKeyboardButton('Задача 4.', callback_data='realtask_2_4')
                    realtask2_5 = types.InlineKeyboardButton('Задача 5.', callback_data='realtask_2_5')
                    realtask2_6 = types.InlineKeyboardButton('Задача 6.', callback_data='realtask_2_6')
                    realtask2_7 = types.InlineKeyboardButton('Задача 7.', callback_data='realtask_2_7')
                    realtask2_8 = types.InlineKeyboardButton('Задача 8.', callback_data='realtask_2_8')
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_1')
                    markup_realtask2.add(realtask2_1,realtask2_2,realtask2_3,realtask2_4,realtask2_5,realtask2_6,realtask2_7,realtask2_8,back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны даны 8 задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''')
                elif call.data == 'task_3':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_3')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_4':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_4')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_5':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_5')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_6':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_6')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_7':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_7')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_8':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_8')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_9':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_9')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_10':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_10')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_11':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_11')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)


                if call.data == 'task_12':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_12')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_13':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_13')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_14':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_14')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_15':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_15')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_16':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_16')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_17':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_17')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_18':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_18')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_19':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_19')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
              

                if call.data == 'task_20':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_20')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_21':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_21')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_22':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_22')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
              

                if call.data == 'task_23':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_23')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_24':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_24')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_25':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_25')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_26':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_26')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_27':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_27')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_28':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_28')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_29':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_29')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
                elif call.data == 'task_30':
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data='paragraph_30')
                    markup_1.add(back1)
                    bot.send_photo(user,'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album', reply_markup=markup_1)
              

bot.polling(none_stop=True)
