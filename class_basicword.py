class Basicword:
    def __init__(self, basic_word, allowed_subwords):
        self.basic_word = basic_word
        self.allowed_subwords = allowed_subwords

    def __repr__(self):
        return f'Основное слово {self.basic_word} с подсловами {self.allowed_subwords}'

    def check_input_word(self, input_word):
        if input_word in self.allowed_subwords:
            return True
        return False

    def count_subwords(self):
        return len(self.allowed_subwords)
