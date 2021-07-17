from aiogram.dispatcher.filters.state import StatesGroup, State


class Answers(StatesGroup):  # Класс, содержащий состояние, в которое переходит бот, ожидаяя ответ
    waiting_for_answer = State()
