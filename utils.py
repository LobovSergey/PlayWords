def load_random_word(dictionary):
    """ Функция выбора случайного слова и его составных подслов"""
    from course_work1.class_basicword import Basicword
    from random import shuffle
    shuffle(dictionary)
    random_word = dictionary[0]
    return Basicword(random_word['word'], random_word['subwords'])


def hello(name, word, subwords):
    """ Функция приветсвия """
    from time import sleep
    print(f'Привет, \033[32m{name}\033[0m')
    sleep(1)
    print(f'\033[32m{name}\033[0m, составьте {len(subwords)} слов из слова {word.upper()}')
    sleep(1)
    print(f'Слова должны быть не короче {len(min(subwords))} букв')
    sleep(1)
    print('Чтобы закончить игру, угадайте все слова или напишите \033[31m"stop"\033[0m')
    sleep(1)
    print('Поехали, ваше первое слово?')


def statisctics(player, basicword):
    """ Фунцкия статистики """
    correct = player.counter_used_words()
    all_subwords = basicword.count_subwords()
    print(f'Игра завершена, вы угадали {correct} из {all_subwords} слов')
    return f'Игрок {player.username}. Прогресс {correct}/{all_subwords}. Для слова {basicword.basic_word}\n'


def ask_while_not_stop(basicword, player):
    """ Функция бесконечного цикла"""
    while player.counter_used_words() != basicword.count_subwords():
        user_input = input('').lower()
        if user_input == 'stop':
            break
        elif basicword.check_input_word(user_input):
            if not player.valid_word(user_input):
                print('Верно!')
                player.add_word_in_used_words(user_input)
            else:
                print('Уже использовалось')
        else:
            if len(user_input) < len(min(basicword.allowed_subwords)):
                print('Слишком короткое слово')
            elif not player.valid_word(user_input):
                print('Неверно')
    return statisctics(player, basicword)
