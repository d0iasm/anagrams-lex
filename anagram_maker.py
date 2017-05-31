#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict, OrderedDict
import codecs


class AnagramMaker:

    def __init__(self, origin, dest):
        self.origin = origin
        self.dest = dest

    def sign(self): 
        d = defaultdict(set)
        
        with open(self.origin, "r") as f:
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
        with codecs.open(self.dest, "w", "utf-8") as f:
            for k, v in anagram_dict.items():
                f.write("%s %s\n" %(k, " ".join(v)))

    def format(self):
        dict_list = [line for line in open(self.origin)]
        key_list = [line.split()[0] for line in dict_list]
        value_list = [line.split()[1:] for line in dict_list]
        anagram_dict = dict(zip(key_list, value_list))

        with codecs.open(self.dest, "w", "utf-8") as f:
            f.write("data = ")
            f.write(str(anagram_dict))



if __name__ == '__main__':
    anagram_maker = AnagramMaker("./dict/original_words", "./dict/anagram_words")
    anagram_maker.output(anagram_maker.sort(anagram_maker.sign()))

    anagram_maker = AnagramMaker("./dict/anagram_words", "./dict/anagram_words.py")
    anagram_maker.format()
