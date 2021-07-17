import random
from aiogram import executor, types
from config import dp, bot
from FSM import Answers
from aiogram.dispatcher import FSMContext
from keyboards import Keyboard
from web_scrapping import DATA


@dp.message_handler(commands="start")
async def cmd1(message: types.Message):
    await bot.send_message(message.chat.id, "Для начала нажмите /start_game")


@dp.message_handler(commands="start_game")
async def cmd2(message: types.Message, state: FSMContext):
    await Answers.waiting_for_answer.set()
    await state.update_data(all=0)
    await state.update_data(score=0)
    await question(state, message.chat.id)


async def question(state, chat_id):
    sz = DATA.shape[0]
    r = random.randint(0, sz - 1)
    row = DATA.iloc[[r]]
    question_text = row["Question"].values[0]
    options_arr = row["Options"].values[0]
    right_answer = row["RightAns"].values[0]
    keyboard = Keyboard()
    if len(options_arr) == 4:
        await bot.send_message(chat_id,
                               f"{question_text}\n\n"
                               f"A. {options_arr[0]}\nB. {options_arr[1]}\nC. {options_arr[2]}\nD. {options_arr[3]}",
                               reply_markup=keyboard(len(options_arr)))
    elif len(options_arr) == 3:
        await bot.send_message(chat_id,
                               f"{question_text}\n\nA. {options_arr[0]}\nB. {options_arr[1]}\nC. {options_arr[2]}",
                               reply_markup=keyboard(len(options_arr)))
    else:
        await bot.send_message(chat_id,
                               f"{question_text}\n\nA. {options_arr[0]}\nB. {options_arr[1]}\n",
                               reply_markup=keyboard(len(options_arr)))
    await state.update_data(right_ans=right_answer)


@dp.message_handler(state=Answers.waiting_for_answer)
async def cmd3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ra = data.get("right_ans")
    if message.text == "Завершить":
        keyboard = Keyboard()
        score = data.get("score")
        a = data.get("all")
        await message.answer(
            f"Вы завершили игру!\nСчёт: {score}/{a}\nЧтобы начать заново нажмите /start_game", reply_markup=keyboard(0))
        await state.finish()
    elif message.text != ra:
        await message.answer(f"Ответ неверный, правильный ответ: {ra}")
        tmp = data.get("all")
        tmp += 1
        await state.update_data(all=tmp)
        await question(state, message.chat.id)
    else:
        await message.answer("Верно!")
        tmp1 = data.get("all")
        tmp2 = data.get("score")
        tmp1 += 1
        tmp2 += 1
        await state.update_data(all=tmp1)
        await state.update_data(score=tmp2)
        await question(state, message.chat.id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
