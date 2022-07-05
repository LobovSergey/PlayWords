import requests

# Импорт модулей
from course_work1.class_player import Player
from course_work1.utils import load_random_word, hello, ask_while_not_stop


def main():
    get_dictionary = requests.get('https://jsonkeeper.com/b/XKZJ')
    dictionary_json = get_dictionary.json()

    username = input('Ввведите имя игрока\n').title()
    player_class = Player(username)
    word_class = load_random_word(dictionary_json)  # Функция генерации случайного слова
    hello(username, word_class.basic_word, word_class.allowed_subwords)  # Функция приветсвия
    with open('history.txt', 'a', encoding='utf-8') as f:
        # Запись статистики и ее вывод
        f.write(f'{ask_while_not_stop(word_class, player_class)}')


# Точка входа
if __name__ == '__main__':
    main()
