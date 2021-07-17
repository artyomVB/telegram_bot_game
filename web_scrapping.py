import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


"""
Функция принимает строку вида "Ответы для викторин: ... " и строку с правильным ответом, 
по ним создает массив с вариантами ответа на вопрос, вставляя на рандомную
позицию верный ответ, возвращает этот массив и букву (A, B, c или D) верного ответа
"""


def get_array_of_ans(options_str, right_ans_str):
    final_arr = options_str[21:].split(', ')
    if len(final_arr) > 4:
        final_arr = final_arr[:4]
    pos = random.randint(0, len(final_arr) - 1)
    final_arr.insert(pos, right_ans_str)
    tmp_str = "ABCD"
    return final_arr, tmp_str[pos]


questions = []  # список с вопросами
options = []  # список, содержащий массивы с вариантами ответов
right_ans = []  # список, содержащий букву верного ответа, по этим спискам будем строить датасет

# в этом фор-е обращаемся к страницам сайта и достаем из них текст вопроса, правильный ответ, варианты ответов
for page in range(0, 3160, 10):
    url = f"https://baza-otvetov.ru/categories/view/1/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    arr = soup.find_all(class_="tooltip")
    for item in arr:
        q = item.a.text
        opt = item.find(class_="q-list__quiz-answers")
        if opt is None:
            continue
        o_str = opt.text.strip()  # варианты ответов в виде "Ответы для викторин: ... "
        ra = item.find_all("td")[2].text  # верный ответ
        tmp = get_array_of_ans(o_str, ra)
        questions.append(q)
        options.append(tmp[0])
        right_ans.append(tmp[1])

DATA = pd.DataFrame({
    "Question": questions,
    "Options": options,
    "RightAns": right_ans
})
