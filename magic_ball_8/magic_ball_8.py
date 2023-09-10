# Game: magic ball 8
import random  # Connect the module random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']


def choice(arr):
    num = random.randint(1, 20)
    input('Задай вопрос на который ты хочешь получить ответ: ')
    return arr[num]


def check_answer():
    ans = input('Хочешь задать еще один вопросы [ДА: enter "Y", НЕТ: enter "N"]: ')
    while True:
        if ans.lower() == 'y':
            return True
        elif ans.lower() == 'n':
            return False
        else:
            print('Ошибка, тебе нужно ввести [ДА: enter "Y" или НЕТ: enter "N"]')
            ans = input()


def get_answer(arr):
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как тебя зовут: ')
    print(f'Привет {name}')

    while True:
        print(choice(arr))
        flag = check_answer()
        if not flag:
            break

    print('Возвращайся если возникнут вопросы!')


get_answer(answers)
