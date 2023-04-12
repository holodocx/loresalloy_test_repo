import telebot
from telebot import types
 #оглавление
themes = [
    {
        "title": "Кинематика",      #название главы
        "code": "theme_1",          #"код" главы, его название в программе
        "paragraphs": [         #список параграфов
            {
                "title": "Механическое движение",       #название параграфа
                "code": "paragraph_1",                  #"код" параграфа, название в программе
                'conspect': "https://sun9-19.userapi.com/impg/slX9DbqscJxKAraZSIN8uSdxgljpHBcilS9Xnw/HyIi1OAh5Dg.jpg?size=1645x2122&quality=95&sign=799d51b03e58d813166f0ac9175622f3&type=album",   #содержимое конспекта
                "videourok": "https://youtu.be/eZy2wp5XINY",    #содержимое видеоурока
                "task": [       #список задач
                    {
                        "url": "",      #будущий текст задачи
                        "answer": ""    #будущий ответ к ней
                    },
                    {},{},{},{},{},{},{} #все восемь задач как списки
                ],  #далее всё повторяется
            },
            {
                "title": 'Траектория,путь,перемещение',
                "code": "paragraph_2",
                'conspect': "https://sun9-52.userapi.com/impg/5kX92f2BkyUpb631oF6OYVIs3lijE26o2J9yvg/9VJwREZ4vmc.jpg?size=1527x2160&quality=96&sign=d839048c43e2ea3dd35a988b8b925d9d&type=album",
                "videourok": "https://youtu.be/I_u9Ut-g-q4",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
            },
            {
                "title": 'Скорость равномер.прямолин.движения',
                "code": "paragraph_3",
                'conspect': "https://sun9-34.userapi.com/impg/z6lK3B858L0nE8Zk8UbKhPvwgScxto8yFaJQ6g/-fD1krEFZhg.jpg?size=1527x2160&quality=95&sign=9ca8fc5ab20fd16b5f37ee1d722ef7e5&type=album",
                "videourok": "https://youtu.be/uX2vilBO4tE",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
            },
            {
                "title": "Сложение скоростей",
                "code": "paragraph_4",
                'conspect': "https://sun9-61.userapi.com/impg/OORWRPONILSls-VZM9kbj-DbTuXOkq-91j8WRg/kqyhMkuPWtM.jpg?size=1527x2160&quality=95&sign=399455a3d12d835200b0b046b65efd84&type=album",
                "videourok": "https://youtu.be/gdUh6TNPTzk",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
            },
            {
                "title": 'Скорость при неравномер. движении',
                "code": "paragraph_5",
                'conspect': "https://sun9-21.userapi.com/impg/CcdXy6qpakv70bSmhyQwkEuzNcOyDrzsFmTcfA/znAcVdnWAP0.jpg?size=1280x1048&quality=95&sign=01dca85be1210d503b55bf2fe3bb6797&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Ускорение',
                "code": "paragraph_6",
                'conspect': "https://sun9-51.userapi.com/impg/WTCMbzv6_4e2YFJ3iQ6xk2fWfaoh-Axfz9AmqQ/7QRKVDoAtgI.jpg?size=1644x2032&quality=95&sign=52c5d86e66f977295da3569c9ff399e9&type=album",
                "videourok": "https://youtu.be/6VXvLh3AnUs",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Перемещение при прямолин.равноускор.движении',
                "code": "paragraph_7",
                'conspect': "https://sun9-77.userapi.com/impg/mJv60mwqQz5T1eiXf4vtfHhusViN4-J1v-2uGQ/s57aoLAnDNM.jpg?size=1653x1943&quality=95&sign=a60dec4dbc1c466d23e5bb18b5978252&type=album",
                "videourok": "https://youtu.be/9u2MuzHii7Y",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Свободное падение тел',
                "code": "paragraph_8",
                'conspect': "https://sun9-44.userapi.com/impg/qXe0UINvC-ImmltBiwXvzrG_9qOo0GbxtkoEkg/y6RQWBrOzOI.jpg?size=1280x1043&quality=95&sign=73fe866dc1bc00976516979d2dd6d1c7&type=album",
                "videourok": "https://youtu.be/Io2Nq6f3HuQ",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": "Движение тел,брошенных под углом к горизонту",
                "code": "paragraph_9",
                'conspect': "https://sun9-3.userapi.com/impg/1lDUve3HU47xA6M8EfffOAHcHh7lev1zVSkbbA/4kG3qQ4ES9E.jpg?size=904x1280&quality=95&sign=0974da2170cbb342ad316352b354b9ab&type=album",
                "videourok": "https://youtu.be/rscPxlPHTPU",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": "",
            },
            {
                "title": 'Равномер.движение по окружности',
                "code": "paragraph_10",
                'conspect': "https://sun9-7.userapi.com/impg/2wAIjhP7TzywdMUSfXTIUErytA8qwuxixSDZCA/mhB2YWNUHYE.jpg?size=905x1280&quality=95&sign=addeb48ab9ee8587fec8074a7f36a059&type=album",
                "videourok": "https://youtu.be/JKjXRD4ZmWg",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Центростремительное ускорение',
                "code": "paragraph_11",
                'conspect': "https://sun9-58.userapi.com/impg/81zLT_aQvTlxFwh88sqDNiELREhxa6awbtUToQ/36HpDxC435s.jpg?size=1280x874&quality=95&sign=429d2a08a3baa8d07498a5559c0c47ed&type=album",
                "videourok": "https://youtu.be/2m1Wwj5DEHc",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            }
        ]
    },
    {
        "title": "Динамика",
        "code": "theme_2",
        "paragraphs": [
            {
                "title": "1-й закон Ньютона",
                "code": "paragraph_12",
                'conspect': "https://sun9-74.userapi.com/impg/hVLjFDdzqJ9DPdo4gw9z7xXSDy4WcM6cN3w_wg/-8gESbAqxt0.jpg?size=1280x1119&quality=95&sign=3a7e7344fd7c4aba291ce761e8b1a82a&type=album",
                "videourok": "https://youtu.be/gLxCiIRWtuE",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": "Сила",
                "code": "paragraph_13",
                'conspect': "https://sun9-29.userapi.com/impg/RUQSMHBKUBBgAPwhT0SVdr7yAEuGTUb1wiS5YA/3258dtko7GE.jpg?size=1102x1280&quality=95&sign=748b4dd8b93f21aab25720b034a58803&type=album",
                "videourok": "https://youtu.be/XAsji3sgMg4",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": "",
            },
            {
                "title": '2-й закон Ньютона',
                "code": "paragraph_14",
                'conspect': "https://sun9-57.userapi.com/impg/1sWpXv7OzhE5lXaHhtygSrU2Gv1zh6DhI4FtHQ/pEF1HOBfMaA.jpg?size=1201x1280&quality=95&sign=97a90ed710791d5e452b2173c9d8b4bb&type=album",
                "videourok": "https://youtu.be/XAsji3sgMg4",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": '3-й закон Ньютона',
                "code": "paragraph_15",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/OijNRhnYokY",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Закон всемирного тяготения',
                "code": "paragraph_16",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/TQUIIGeozbQ",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Вес.Невесомость.Перегрузка',
                "code": "paragraph_17",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/vWs4MIZTEwM",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": "1-я космическая скорость",
                "code": "paragraph_18",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/xQOns-yfmJI",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": "",
            },
            {
                "title": 'Сила трения',
                "code": "paragraph_19",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/zi3omRrfurg",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            }
        ]
    },
    {
        "title": "Статика",
        "code": "theme_3",
        "paragraphs": [
            {
                "title": "Условия равновесия тел",
                "code": "paragraph_20",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/d348jsnU5i8",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
             {
                "title": "Центр тяжести",
                "code": "paragraph_21",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/6OyCV7jodYA",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": "",
            },
            {
                "title": 'Виды равновесия.Устойчивость тел',
                "code": "paragraph_22",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/BD_-qrhXH5k",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            }
        ]
    },
    {
        "title": "Законы сохранения в механике",
        "code": "theme_4",
        "paragraphs": [
            {
                "title": "Импульс тела",
                "code": "paragraph_23",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/Ev68eLx6RWA",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": "Закон сохранения импульса",
                "code": "paragraph_24",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/-XPUqhgOVJU",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": "",
            },
            {
                "title": 'Реактивное движение',
                "code": "paragraph_25",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/MM_72FXE7oA",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Механическая работа.Мощность',
                "code": "paragraph_26",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/pkbCHu7zoJk",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Кинетическая энергия тела',
                "code": "paragraph_27",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/rPVKb_leXus",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": 'Рябота силы тяжести.Потенц.энергия',
                "code": "paragraph_28",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/aggu45cT8vI",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            },
            {
                "title": "Работа силы упругости",
                "code": "paragraph_29",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/j1z_LnFKRvg",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": "",
            },
            {
                "title": 'Закон сохранения механич.энергии',
                "code": "paragraph_30",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://youtu.be/dPS3_jE3u2k",
                "task": [
                    {
                        "url": "",
                        "answer": ""
                    },
                    {},{},{},{},{},{},{}
                ],
                "summary": ""
            }
        ]
    }
]

def find_theme_by_code(code):       #дэф для поиска нужной главы
    for theme in themes:
        if theme['code'] == code:
            return theme
    
    return None

def find_paragraph_by_code(code):       #дэф для поиска нужного параграфа
    for theme in themes:
        for paragraph in theme['paragraphs']:
            if paragraph['code'] == code:
                return paragraph, theme
    
    return None

token = "5833332883:AAEEkix40TB1s8BJewF4UIzhykDJ5rUTQCE"
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])        #стартовое сообщение
def start(message):
    chat_id = message.chat.id
    name = message.from_user.first_name
    bot.send_message(chat_id, text=('''Здравствуй,'''+' '+name+'''! :-)
Это бот, разработанный учениками школы 1561, в котором собраны краткие конспекты, видео-уроки и дополнительные задания по физике!
Для вызова нашей библиотеки используй команду /assortment.'''))

@bot.message_handler(commands=['assortment'])       #команда для вызова оглавления(всех глав)
def assortment(message):
    chat_id = message.chat.id
    markup_themes = types.InlineKeyboardMarkup(row_width=1)
    for theme in themes:
        markup_themes.add(types.InlineKeyboardButton(theme['title'], callback_data=theme['code']))
    bot.send_message(message.chat.id, 'Выбери главу:', reply_markup=markup_themes)


@bot.callback_query_handler(func=lambda call:True)      #дэф для открытия нужного параграфа
def paragraphs(call):
    print(call.data, call.message)
    user = call.message.chat.id
    if call.message:
        if call.data == 'themes':       #пользователь вызвал оглавление(все главы)
           assortment(call.message)     #это и есть команда ассортмэнт
        if 'theme_' in call.data:       #происходит выбор конкретной главы
            print("finding theme")      #инсайд для терминала, чтоб спокойней было
            theme = find_theme_by_code(call.data)       #открывается содержание главы, всё, что внутри
            if theme:       #если выбрана глава:
                markup_parag = types.InlineKeyboardMarkup(row_width=1)      #маркап для кнопок
                for paragraph in theme['paragraphs']:       #для параграфа среди параграфов:
                    markup_parag.add(types.InlineKeyboardButton(paragraph['title'], callback_data=paragraph['code']))       #кнопка. на кнопке - имя параграфа, колбэк - открытие инсайда параграфа
                markup_parag.add(types.InlineKeyboardButton('Назад', callback_data='themes'))  #ну собственно добавление кнопок
                bot.send_message(call.message.chat.id, 'Выбери параграф:', reply_markup=markup_parag)


        if 'paragraph' in call.data:        #содержимое параграфа
            code = call.data

            if 'conspect' in call.data:         #отдел конспекта
                # paragraph_?conspect
                code = call.data.rstrip('conspect')         #составляющее конспекта (rstrip для возвращения копии строки с удалёнными символами в конце, т.е. чтоб каждый раз цифры считывать)
                paragraph, theme = find_paragraph_by_code(code)         #использование дэфа для параграфа
                markup_1 = types.InlineKeyboardMarkup(row_width=1)          #маркап для кнопок
                back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])            #кнопка назад
                markup_1.add(back1)
                bot.send_photo(user, paragraph['conspect'], reply_markup=markup_1)

            elif 'videourok' in call.data:          #отдел видеоуроков
                # paragraph_?videourok
                code = call.data.rstrip('videourok')            #составляющее видеоурока (rstrip для возвращения копии строки с удалёнными символами в конце, т.е. чтоб каждый раз цифры считывать)
                paragraph, theme = find_paragraph_by_code(code)         #использование дэфа для параграфа
                markup_1 = types.InlineKeyboardMarkup(row_width=1)          #маркап
                video =  types.InlineKeyboardButton('Перейти к видеоуроку', url=paragraph['videourok'])         #кнопка-ссылка на видеоурок
                back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])            #кнопка назад
                markup_1.add(video, back1)
                bot.send_message(call.message.chat.id, 'Видеоурок доступен по кнопке ниже:', reply_markup=markup_1)

            elif 'task' in call.data:           #отдел задач
                if call.data.endswith('task'):      #если строка заканчивается символами из скобок:
                    code = call.data.rstrip('task')     #составляющее задач (rstrip для возвращения копии строки с удалёнными символами в конце, т.е. чтоб каждый раз цифры считывать)
                    paragraph, theme = find_paragraph_by_code(code)     #использование дэфа для параграфа
                    
                    print(paragraph)            #инсайд для терминала, можно убрать впринципе
                    markup_realtask = types.InlineKeyboardMarkup(row_width=2)       #маркап для кнопок-задачек
                    for i in range(0, len(paragraph['task']), 2):       #а вот тут парилочка с размером кнопок. в общем, эта строка отвечает за то, чтобы кнопок в ряду было две, а не одна
                        btn1 = types.InlineKeyboardButton(f'Задача {i+1}', callback_data=paragraph['code'] + f'task_{i}' )  #первый столбец кнопок. i-ноль. чтобы первая задача не была нулевой и т.д., прибавляем к i один
                        btn2 = types.InlineKeyboardButton(f'Задача {i+2}', callback_data=paragraph['code'] + f'task_{i+1}' )#второй столбец кнопок. схема та же, что и в первом, только теперь к i прибавляем два(чтобы вторая задача не была нулевой и т.д.), а также смещаем ещё и столбец(чтобы он был вторым) с помощью i+1
                        markup_realtask.add(btn1, btn2)     #добавляем кнопки
                    back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])        #кнопка назад
                    markup_realtask.add(back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask)
                
                else:       #если выбрана конкретная задача
                    print('мы щас тут')     #инсайд для терминала, не обращать внимание
                    task_num = int(call.data.split('_')[-1])    #удаляем цифру задачи, чтобы на все задачи колбэк был одинаков
                    code = call.data.rstrip(f'task_{task_num}') #составляющее задачи (rstrip для возвращения копии строки с удалёнными символами в конце, т.е. чтоб каждый раз цифры считывать)
                    print(code, task_num)
                    paragraph, theme = find_paragraph_by_code(code) #использование дэфа для параграфа
                    task = paragraph['task'][task_num]      #из чего состоит сам таск(его содержание и его номер)
                    user = call.message.chat.id     #получаем сообщение от пользователя
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)      #маркап для кнопки
                    back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])        #кнопка назад
                    markup_1.add(back1)
                    bot.send_photo(user, 'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album',reply_markup=markup_1)


                

            else:        
                # paragraph_?
                paragraph, theme = find_paragraph_by_code(call.data)    #использование дэфа для параграфа, чтобы открыть содержимое параграфа
                if paragraph:       #когда выбирается параграф:

                    markupp = types.InlineKeyboardMarkup(row_width=1)       #маркап для кнопок
                    conspect = types.InlineKeyboardButton('Конспект', callback_data=code + 'conspect')      #кнопка конспекта
                    videourok = types.InlineKeyboardButton('Видео-урок', callback_data=code + 'videourok')  #кнопка видеоурока
                    task = types.InlineKeyboardButton('Задачи', callback_data=code + 'task')                #кнопка задач
                    back1 = types.InlineKeyboardButton('Назад', callback_data=theme['code'])                #кнопка назад
                    markupp.add(conspect, videourok, task, back1)
                    bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markupp)



bot.polling(none_stop=True)
