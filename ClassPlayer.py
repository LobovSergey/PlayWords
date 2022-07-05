class Player:
    def __init__(self, username, used_words=None):
        if used_words is None:
            used_words = []
        self.username = username
        self.used_words = used_words

    def __repr__(self):
        return f'{self.username} нашел {self.used_words} '

    def counter_used_words(self):
        return len(self.used_words)

    def add_word_in_used_words(self, word):
        self.used_words.append(word)

    def valid_word(self, word):
        if word in self.used_words:
            return True
        return False
