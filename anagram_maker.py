from collections import defaultdict, OrderedDict
import codecs
from functools import reduce


class AnagramMaker:

    def __init__(self):
        pass

    def sign(self, file_name): 
        d = defaultdict(set)
        
        with open(file_name, "r") as f:
            for line in f:
                word = line.lower().strip()
                char_list = list(word)
                char_list.sort()
                sign = "".join(char_list)
            
                d[sign].add(word)
            
        return d

    def sort(self, sign_dict):
        return OrderedDict(sorted(sign_dict.items()))

    def output(self, anagram_dict):
        with codecs.open(anagram_dict, "w", "utf-8") as f:
            f.write("hoge")


if __name__ == '__main__':
    anagram_maker = AnagramMaker()
    anagram_maker.sort(anagram_maker.sign("./dict/original_words_short"))

    anagram_maker.output("./dict/anagram_words_short")
