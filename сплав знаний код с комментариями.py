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
                        "url": "1. На диске отмечены белая и чёрная точки. При равномерном вращении диска скорость белой точки в 2 раза больше, чем чёрной. Во сколько раз центростремительное ускорение одной точки больше, чем другой?",
                        "answer": ""
                    },
                    {
                        "url": "2. Длина секундной стрелки настенных часов равна 25 см. Чему равно центростремительное ускорение конца стрелки?",
                        "answer": ""
                    },{
                        "url": "3. На равномерно вращающемся диске отмечены белая и чёрная точки. Расстояние от белой точки до центра диска в 3 раза меньше, чем от чёрной. Во сколько раз центростремительное ускорение одной точки больше, чем другой?",
                        "answer": ""
                    },{
                        "url": "4. Колесо радиусом 50 см катится без проскальзывания по прямой дороге и делает полный оборот за 2 с. Чему равна скорость верхней точки колеса относительно дороги?",
                        "answer": ""
                    },{
                        "url": "5. Материальная точка равномерно движется по окружности радиусом 40 см и совершает 3 оборота в минуту. Чему равно центростремительное ускорение точки?",
                        "answer": ""
                    },{
                        "url": "6. Длина минутной стрелки настенных часов равна 30 см. Чему равно центростремительное ускорение конца стрелки?",
                        "answer": ""
                    },{
                        "url": "7. Материальная точка равномерно движется по окружности радиусом 50 см со скоростью 2 м/с. Чему равно центростремительное ускорение точки?",
                        "answer": ""
                    },{
                        "url": "8. Колесо катится без проскальзывания по прямой дороге со скоростью 2 м/с. Чему равна скорость точки обода колеса, находящейся на одной горизонтали с осью колеса?",
                        "answer": ""
                    }
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
                        "url": "1. К телу массой 3 кг приложены две силы, одна из которых направлена вертикально вниз и равна 30 Н. Тело движется с постоянной скоростью, направленной вверх и равной 2 м/с. Как надо изменить вторую силу, чтобы скорость тела начала уменьшаться и пройденный им до остановки путь был равен 2 м?",
                        "answer": ""
                    },
                    {
                        "url": "2. Тело массой 0,5 кг брошено под углом 30° к горизонту со скоростью 20 м/с. Сопротивлением воздуха можно пренебречь. Через сколько времени после броска равнодействующая приложенных к телу сил будет перпендикулярна скорости тела?",
                        "answer": ""
                    },{
                        "url": "3. К телу, движущемуся в положительном направлении оси x со скоростью 4 м/с, в начальный момент прикладывают две силы, направленные вдоль оси x, проекции которых равны 3 Н и –5 Н. Какой путь прошло тело за 2 с?",
                        "answer": ""
                    },{
                        "url": "4. Тело брошено под углом 60° к горизонту со скоростью 30 м/с. Равнодействующая приложенных к телу сил в верхней точке траектории равна 10 Н. Сопротивлением воздуха можно пренебречь. Через сколько времени после броска равнодействующая приложенных к телу сил будет перпендикулярна скорости тела?",
                        "answer": ""
                    },{
                        "url": "5. К телу массой 2 кг приложены две силы, равные 3 Н и 4 Н. Как направлены силы, если тело движется с ускорением 2,5 м/с2?",
                        "answer": ""
                    },{
                        "url": "6. Тело массой 2 кг равномерно движется по окружности радиусом 60 см со скоростью 3 м/с. Какой стала скорость тела, когда равнодействующая приложенных к нему сил увеличилась в 4 раза, а радиус окружности остался прежним?",
                        "answer": ""
                    },{
                        "url": "7. К телу массой 3 кг приложены две силы, каждая из которых равна 6 Н. Равнодействующая этих сил равна по модулю 6 Н. С каким ускорением будет двигаться тело, если угол между силами уменьшить в 2 раза?",
                        "answer": ""
                    },{
                        "url": "8. Тело равномерно движется по окружности радиусом 1,5 м и совершает три оборота в минуту. Равнодействующая приложенных к телу сил равна 0,2 Н. Каким станет период обращения тела, если равнодействующая приложенных к нему сил станет в 16 раз больше, а радиус окружности останется прежним?",
                        "answer": ""
                    }
                ],
                "summary": ""
            },
            {
                "title": '3-й закон Ньютона',
                "code": "paragraph_15",
                'conspect': "https://sun9-19.userapi.com/impg/dZ8GaN3Adv_DIrf5XSZiS-I1w4esDmVTrjvjWA/OHFuP0VGubg.jpg?size=1280x865&quality=95&sign=c027f9f6233ffb936847f73a9a618335&type=album",
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
                'conspect': "https://sun9-38.userapi.com/impg/73h_WLzRbK6y1rQ40yvvzyBxDIO_7mEQaIXuKA/BCi3Y7kne-M.jpg?size=1280x975&quality=95&sign=67174e38ccedeae6d5daef375404c4d1&type=album",
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
                'conspect': "https://sun9-52.userapi.com/impg/xcoRHk47mLQuYOzNk5tYRijyzJbI6IP2y9a7PQ/vWgHK4obQa8.jpg?size=1280x1058&quality=95&sign=99c6e22f4e043e6373ea0e3dbb7494e6&type=album",
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
                'conspect': "https://sun9-12.userapi.com/impg/PI85Ugm9pRgY5_3Cm-K0PQkt8vZUVT_73wlihg/DeE-N8KdrDA.jpg?size=1280x1145&quality=95&sign=63c164ac263106c265ddb8714ef32139&type=album",
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
                'conspect': "https://sun9-60.userapi.com/impg/DYIVeRiDKSTElmSC6LIeBkzJrl4u2t-G_1OvFg/4j_EoxbBbAA.jpg?size=905x1280&quality=95&sign=4b14b3cbc63fdb8930c2ecef562a4e4a&type=album",
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
                'conspect': "https://sun9-49.userapi.com/impg/HQ3Q52D-NkUmEtaOj3G8KzYgZq6ChOCaO5zC_g/MnhqYUapQWY.jpg?size=1174x1280&quality=95&sign=9c558e8159933ada0a3fdb5662002457&type=album",
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
                'conspect': "https://sun9-68.userapi.com/impg/uFY-fipvdoU-WKhXnBCQeZbFZWtlarjJmZm2LQ/UQ0AJfRprgg.jpg?size=1280x1093&quality=95&sign=8b148ea8a8d019f9790ae0827f58aba1&type=album",
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
                'conspect': "https://sun9-22.userapi.com/impg/Zrhq6sMhrpgoPZj3lDa-4Sv032TAeZ8inkzgpQ/QjEvu-A5p4E.jpg?size=1280x1247&quality=95&sign=32b08d6f5d4658a1dc2c3eae37387cba&type=album",
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
                'conspect': "https://sun9-15.userapi.com/impg/5fgU4s2LguSQdeeo2Euk2OnNc6Cxyq7h_3aW2g/oK3qQszO2Do.jpg?size=1280x1067&quality=95&sign=632e3349cb7eb4e9d0145a067fa4666e&type=album",
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
                'conspect': "https://sun9-8.userapi.com/impg/1coSvByo5pIxT_jZQlkecP9EF4wzStLtSYzhJQ/vADoYkrtKBc.jpg?size=1189x1280&quality=95&sign=a79a550a89a2fc8156aa7b9e31431f01&type=album",
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
                'conspect': "https://sun9-38.userapi.com/impg/OGN3YL__kr6_IRQnSYZZn8xrc-lNWOKSh4nTCA/hMGiuVKEDYQ.jpg?size=1020x627&quality=95&sign=906504cf13c899206d648791c78e2450&type=album",
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
                'conspect': "https://sun9-28.userapi.com/impg/P45j4vf70QYhwbRyVUm_bPN4QnpCiTLZlP1uOg/7CoCGPmsTE0.jpg?size=1129x1280&quality=95&sign=bd6e6ad4da15b7ef9e8d941404363f53&type=album",
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
                'conspect': "https://sun1-85.userapi.com/impg/N4DoJoAkervtpIKYkaDJpO5tlHnUwdfwkirnDg/5KRqVcC42aA.jpg?size=1271x1280&quality=95&sign=eb1e03c9ba2157fb43ff076be2ffb33b&type=album",
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
                "title": 'Потенциальная энергия тела',
                "code": "paragraph_28",
                'conspect': "https://sun1-27.userapi.com/impg/JRIfy-K-DpeeQ4tUyaSMSZqHEDdX_aaPiXHWlw/n3N68CmHY9g.jpg?size=1280x1216&quality=95&sign=a1202e5d62a93f2663115e9981263364&type=album",
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
                "title": "Работа силы упр. и силы тяж.",
                "code": "paragraph_29",
                'conspect': "https://sun9-43.userapi.com/impg/I2sNf4Z_FWeMdb2DSr27dtkpyYNYY6fGv-4f-w/JgRGJDRSrO4.jpg?size=1115x1280&quality=95&sign=780651f8b4caa9ec032e53378651e5af&type=album",
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
                'conspect': "https://sun9-74.userapi.com/impg/FMgnznwJK0gd9ARBjyO1lMIaaOmHcu0d6XuhFw/ZbIUtzEyRKM.jpg?size=1138x1280&quality=95&sign=1e415b24c5eb404f13de972b9329ff41&type=album",
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
                    print('задача')     #инсайд для терминала, не обращать внимание
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
