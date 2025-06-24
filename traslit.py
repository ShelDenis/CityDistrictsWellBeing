import streamlit as st


trans_dict_1 = {
    'a': 'а',
    'b': 'б',
    'v': 'в',
    'g': 'г',
    'd': 'д',
    'e': 'е',
    'j': 'ж',
    'z': 'з',
    'i': 'и',
    'y': 'ы',
    'k': 'к',
    'l': 'л',
    'm': 'м',
    'n': 'н',
    'o': 'о',
    'p': 'п',
    'r': 'р',
    's': 'с',
    't': 'т',
    'u': 'у',
    'f': 'ф',
    'h': 'х',
    'c': 'ц',
    '_': ' '
}

trans_dict_2 = {
    'ch': 'ч',
    'sh': 'ш',
    'yu': 'ю',
    'ya': 'я',
    'yy': 'ый',
    'ay': 'ая',
    'zm': 'зьм',
    'cr': 'кр',
    'iy': 'ий',
    'oy': 'ой',
    'ey': 'ей',
    'uy': 'уй',
    'brs': 'брь',
    'ln': 'льн',
    'ftyn': 'фтя',
    'silv': 'сильв'
}

trans_dict_many = {
    'cottages': '(коттеджи)',
    'houses': '(частный сектор)',
    'mkd': '(многоэтажки)',
    'far': ' (дальний мкр.)',
    'near': ' (ближний мкр.)',
    'medium': ' (средний мкр.)',
    'main': ' (главный мкр.)',
    'north': ' (северный мкр.)',
    'old': 'Старый',
    'sch': 'щ',
    'csh': 'щ',
    'post': 'пость',
    'eco': 'эко',
    'lsh': 'льш',
    'may': 'май',
    'zor': 'зорь',
    'iish': 'иисх',
    'zal': 'заль',
    'prot': 'порт',
    'molsk': 'мольск',
    'chh': 'чн',
    'ochie': 'очие',
    'chie': 'чье'
}

okruga = {
    'k': 'Кировский',
    's': 'Советский',
    'c': 'Центральный',
    'o': 'Октябрьский',
    'l': 'Ленинский'
}


def translit(word):
    if '_mr' in word:
        return f'{word.split("_")[0]}-й микрорайон'
    else:
        dicts = [trans_dict_many, trans_dict_2, trans_dict_1]
        for dct in dicts:
            for key, val in dct.items():
                if key in word:
                    word = word.replace(key, val)
        return word.capitalize()


def get_okrug(s):
    return okruga[s]
