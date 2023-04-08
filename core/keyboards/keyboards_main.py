from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    KeyboardButtonPollType  # create keyboard, button. вопросы
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    main_keyboard = ReplyKeyboardBuilder()

    main_keyboard.add(KeyboardButton(text="Уроки"))
    main_keyboard.add(KeyboardButton(text="Что - то"))
    main_keyboard.add(KeyboardButton(text="Что - то"))
    main_keyboard.add(KeyboardButton(text="Обратная связь"))

    main_keyboard.adjust(2)
    return main_keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                   input_field_placeholder="Выберете кнопку", selective=True)


def main_back_kb():
    back = ReplyKeyboardBuilder()
    back.add(KeyboardButton(text="Назад", callback_data="back_to_main_menu"))

    back.adjust(1)
    return back.as_markup(resize_keyboard=True, one_time_keyboard=True,
                          input_field_placeholder="Выберете кнопку", selective=True)


def lessons_kb():
    less_name = ['Работа с сообщениями', 'Кнопки', 'Роутеры, структура', 'Фильтры']
    lessons = InlineKeyboardBuilder()

    number_less: int = 1
    for i in less_name:
        lessons.add(InlineKeyboardButton(text=f"Урок №{number_less} {i}", callback_data=f"less_{number_less}"))
        number_less += 1

    lessons.add(InlineKeyboardButton(text="Назад", callback_data="back_to_main_menu"))

    lessons.adjust(2)
    return lessons.as_markup()
