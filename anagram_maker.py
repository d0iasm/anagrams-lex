#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict, OrderedDict
import codecs


class AnagramMaker(object):

    def __init__(self, origin, dest):
        self.origin = origin
        self.dest = dest

    def sign(self): 
        d = defaultdict(set)
        
        with open(self.origin, "r") as f:
            for line in f:
                word = line.lower().strip()
                if "qu" in word: word = word.replace("qu", "q")
                chars = list(word)
                chars.sort()
                sign = "".join(chars)
                d[sign].add(word)
        return d

    def sort(self, dict):
        return OrderedDict(sorted(dict.items()))

    def output(self):
        anagrams = self.sort(self.sign())
        with codecs.open(self.dest, "w", "utf-8") as f:
            for k, v in anagrams.items():
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
    anagram_maker.output()

    anagram_maker = AnagramMaker("./dict/anagram_words", "./dict/anagram_words.py")
    anagram_maker.format()
