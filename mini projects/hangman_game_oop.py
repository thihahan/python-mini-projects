from random import *
from words import words

class hangman:
    def __init__(self):
        self.word = list(choice(words))
        # self.word = list('hello')
        self.lives = 0
        self.qus_word = []
        self.given_words = [randint(0, len(self.word)), randint(0, len(self.word))]
        self.word_index_filter = []
        self.element_position = []

    def question(self):
        for i in self.word:
            self.qus_word.append('_')

        for x in self.given_words:
            self.qus_word[x] = self.word[x]
        value = ' '.join(map(str, self.qus_word))
        print(value)

    def word_position(self, ele):
        count = 0
        bool = True
        while bool:
            try:
                pos = self.word.index(ele, count)
                self.element_position.append(pos)
                count += 1
            except ValueError as e:
                bool = False

    def word_filter(self, ele):
        for i in self.element_position:
            if i not in self.word_index_filter:
                self.word_index_filter.append(i)

    def correct(self, ele):
        print(f'word_index_filter {self.word_index_filter}')
        for i in self.word_index_filter:
            self.qus_word[i] = ele
            print(f"i {i}")
            print("ele: ", ele)
        value = '  '.join(map(str, self.qus_word))
        print(f"correct {value}")

    def uncorrect(self, ele):
        print(f"There is no {ele.upper()} in word. You have only {10 - self.lives} lives ")
        if self.lives == 10:
            self.qus_word = self.word
            value = ' '.join(map(str, self.qus_word))
            print(f'correct word is {value}')
            return
        self.lives += 1
        value = '  '.join(map(str, self.qus_word))
        print(value)

    def start(self):
        self.question()
        while '_' in self.qus_word:
            self.element_position = []
            self.word_index_filter = []
            ele = input("Enter a alphabet: ")
            if ele in self.word:
                self.word_position(ele)
                self.word_filter(ele)
                self.correct(ele)
            else:
                self.uncorrect(ele)




if __name__ == '__main__':
    game = hangman()
    game.start()
