from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class Keyboard:
    def __init__(self):
        pass

    def __call__(self, number_of_buttons):
        if number_of_buttons == 4:
            keyboard_ans_4 = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="A"),
                        KeyboardButton(text="B")
                    ],
                    [
                        KeyboardButton(text="C"),
                        KeyboardButton(text="D")
                    ],
                    [
                        KeyboardButton(text="Завершить")
                    ]
                ]
            )
            return keyboard_ans_4
        if number_of_buttons == 3:
            keyboard_ans_3 = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="A"),
                        KeyboardButton(text="B")
                    ],
                    [
                        KeyboardButton(text="C"),
                    ],
                    [
                        KeyboardButton(text="Завершить")
                    ]
                ]
            )
            return keyboard_ans_3
        if number_of_buttons == 2:
            keyboard_ans_2 = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="A"),
                        KeyboardButton(text="B")
                    ],
                    [
                        KeyboardButton(text="Завершить")
                    ]
                ]
            )
            return keyboard_ans_2
        keyboard_rem = ReplyKeyboardRemove()
        return keyboard_rem
