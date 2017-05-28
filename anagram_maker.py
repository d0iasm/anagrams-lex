import sys


class AnagramMaker:

    def __init__(self):
        pass

    def read(self, name):
        f = open(name)
        line = f.readline()
        while line:
            print(line)
            line = f.readline()


if __name__ == '__main__':
    anagram_maker = AnagramMaker()
    anagram_maker.read("./dict/original_words_short")
