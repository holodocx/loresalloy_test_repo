import telebot
from telebot import types

themes = [
    {
        "title": "Кинематика",
        "code": "theme_1",
        "paragraphs": [
            {
                "title": "Механическое движение",
                "code": "paragraph_1",
                'conspect': "https://sun9-19.userapi.com/impg/slX9DbqscJxKAraZSIN8uSdxgljpHBcilS9Xnw/HyIi1OAh5Dg.jpg?size=1645x2122&quality=95&sign=799d51b03e58d813166f0ac9175622f3&type=album",
                "videourok": "https://youtu.be/eZy2wp5XINY",
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
                "summary": ""
            },
            {
                "title": 'Скорость равномер.прямолин.движения',
                "code": "paragraph_3",
                'conspect': "https://sun9-34.userapi.com/impg/z6lK3B858L0nE8Zk8UbKhPvwgScxto8yFaJQ6g/-fD1krEFZhg.jpg?size=1527x2160&quality=95&sign=9ca8fc5ab20fd16b5f37ee1d722ef7e5&type=album",
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
                "title": "Сложение скоростей",
                "code": "paragraph_4",
                'conspect': "https://sun9-61.userapi.com/impg/OORWRPONILSls-VZM9kbj-DbTuXOkq-91j8WRg/kqyhMkuPWtM.jpg?size=1527x2160&quality=95&sign=399455a3d12d835200b0b046b65efd84&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "title": 'Перемещение при прямолин.равноускор.движении',
                "code": "paragraph_7",
                'conspect': "https://sun9-77.userapi.com/impg/mJv60mwqQz5T1eiXf4vtfHhusViN4-J1v-2uGQ/s57aoLAnDNM.jpg?size=1653x1943&quality=95&sign=a60dec4dbc1c466d23e5bb18b5978252&type=album",
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
                "title": 'Свободное падение тел',
                "code": "paragraph_8",
                'conspect': "https://sun9-44.userapi.com/impg/qXe0UINvC-ImmltBiwXvzrG_9qOo0GbxtkoEkg/y6RQWBrOzOI.jpg?size=1280x1043&quality=95&sign=73fe866dc1bc00976516979d2dd6d1c7&type=album",
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
                "title": "Движение тел,брошенных под углом к горизонту",
                "code": "paragraph_9",
                'conspect': "https://sun9-3.userapi.com/impg/1lDUve3HU47xA6M8EfffOAHcHh7lev1zVSkbbA/4kG3qQ4ES9E.jpg?size=904x1280&quality=95&sign=0974da2170cbb342ad316352b354b9ab&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": 'Центростремительное ускорение',
                "code": "paragraph_11",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": "Сила",
                "code": "paragraph_13",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": '3-й закон Ньютона',
                "code": "paragraph_15",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": 'Закон всемирного тяготения',
                "code": "paragraph_16",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": 'Вес.Невесомость.Перегрузка',
                "code": "paragraph_17",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": "1-я космическая скорость",
                "code": "paragraph_18",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "title": "Центр тяжести",
                "code": "paragraph_21",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "title": "Закон сохранения импульса",
                "code": "paragraph_24",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "title": 'Механическая работа.Мощность',
                "code": "paragraph_26",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": 'Кинетическая энергия тела',
                "code": "paragraph_27",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": 'Рябота силы тяжести.Потенц.энергия',
                "code": "paragraph_28",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
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
                "title": "Работа силы упругости",
                "code": "paragraph_29",
                'conspect': "https://sun9-68.userapi.com/impg/BupTxIbwvs4myt_bPoTmjZrIjhTx5mUiYbLnIQ/icAcLr_BAA0.jpg?size=2560x2560&quality=95&sign=32cee20697613a4ba065970e118d1f0e&type=album",
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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
                "videourok": "https://sun9-72.userapi.com/impg/Z5SRN-PkFazUANXhXI7s3-Wrcg1E5jVkgcM13w/heSJYb1_iZ4.jpg?size=2560x2560&quality=95&sign=1f6625705e4abdff3176030be73612d6&type=album",
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

def find_theme_by_code(code):
    for theme in themes:
        if theme['code'] == code:
            return theme
    
    return None

def find_paragraph_by_code(code):
    for theme in themes:
        for paragraph in theme['paragraphs']:
            if paragraph['code'] == code:
                return paragraph, theme
    
    return None

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
    markup_themes = types.InlineKeyboardMarkup(row_width=1)
    for theme in themes:
        markup_themes.add(types.InlineKeyboardButton(theme['title'], callback_data=theme['code']))
    bot.send_message(message.chat.id, 'Выбери главу:', reply_markup=markup_themes)


@bot.callback_query_handler(func=lambda call:True)
def paragraphs(call):
    print(call.data, call.message)
    user = call.message.chat.id
    if call.message:
        print(1)
        if call.data == 'themes':
           assortment(call.message)
        if 'theme_' in call.data:
            print("finding theme")
            theme = find_theme_by_code(call.data)
            if theme:
                markup_parag = types.InlineKeyboardMarkup(row_width=1)
                for paragraph in theme['paragraphs']:
                    markup_parag.add(types.InlineKeyboardButton(paragraph['title'], callback_data=paragraph['code']))
                markup_parag.add(types.InlineKeyboardButton('Назад', callback_data='themes'))
                bot.send_message(call.message.chat.id, 'Выбери параграф:', reply_markup=markup_parag)


        if 'paragraph' in call.data:
            code = call.data

            if 'conspect' in call.data:
                # paragraph_?conspect
                code = call.data.rstrip('conspect')
                paragraph, theme = find_paragraph_by_code(code)
                markup_1 = types.InlineKeyboardMarkup(row_width=1)
                back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])
                markup_1.add(back1)
                bot.send_photo(user, paragraph['conspect'], reply_markup=markup_1)

            elif 'videourok' in call.data:
                # paragraph_?videourok
                code = call.data.rstrip('videourok')
                paragraph, theme = find_paragraph_by_code(code)
                markup_1 = types.InlineKeyboardMarkup(row_width=1)
                video =  types.InlineKeyboardButton('Перейти к видеоуроку', url=paragraph['videourok']) 
                back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])
                markup_1.add(video, back1)
                bot.send_message(call.message.chat.id, '''Видеоурок доступен по кнопке ниже:''', reply_markup=markup_1)

            elif 'task' in call.data:
                if call.data.endswith('task'):
                    code = call.data.rstrip('task')
                    paragraph, theme = find_paragraph_by_code(code)
                    
                    print(paragraph)
                    markup_realtask = types.InlineKeyboardMarkup(row_width=2)
                    for i in range(0, len(paragraph['task']), 2):
                        btn1 = types.InlineKeyboardButton(f'Задача {i+1}.', callback_data=paragraph['code'] + f'task_{i}' )
                        btn2 = types.InlineKeyboardButton(f'Задача {i+2}.', callback_data=paragraph['code'] + f'task_{i+1}' )
                        markup_realtask.add(btn1, btn2)
                    back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])
                    markup_realtask.add(back1)
                    bot.send_message(call.message.chat.id, '''Тебе даны восемь задач. Можешь решать их в любом порядке.
В случае ошибки ты можешь взять ещё одну попытку или сразу посмотреть решение.''', reply_markup=markup_realtask)
                
                else:
                    task_num = int(call.data.split('_')[-1])
                    code = call.data.rstrip(f'task_{task_num}')
                    print(code, task_num)
                    paragraph, theme = find_paragraph_by_code(code)
                    task = paragraph['task'][task_num]
                    user = call.message.chat.id
                    markup_1 = types.InlineKeyboardMarkup(row_width=1)
                    back1 = types.InlineKeyboardButton('Назад', callback_data=paragraph['code'])
                    markup_1.add(back1)
                    bot.send_photo(user, 'https://sun9-7.userapi.com/impg/f9Vq8nQ16CpMwfvzki7aSRDfzGow7mzpw_CT6w/NUJIpgn0iFc.jpg?size=2560x2560&quality=95&sign=764217999699eb764ff6e6df301e88a1&type=album',reply_markup=markup_1)


                

            else:        
                # paragraph_?
                paragraph, theme = find_paragraph_by_code(call.data)
                if paragraph:

                    markupp = types.InlineKeyboardMarkup(row_width=1)
                    conspect = types.InlineKeyboardButton('Конспект', callback_data=code + 'conspect')
                    videourok = types.InlineKeyboardButton('Видео-урок', callback_data=code + 'videourok')
                    task = types.InlineKeyboardButton('Задачи', callback_data=code + 'task')
                    back1 = types.InlineKeyboardButton('Назад', callback_data=theme['code'])
                    markupp.add(conspect, videourok, task, back1)
                    bot.send_message(call.message.chat.id, 'Выбери интересующий тебя ресурс:', reply_markup=markupp)



bot.polling(none_stop=True)
