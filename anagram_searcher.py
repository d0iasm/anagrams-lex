#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache


class AnagramSearcher:

    def __init__(self):
        self.dict = "./dict/anagram_words"
        self.num = sum(1 for line in open(self.dict))

    def search(self, word):
        low = 0
        high = self.num

        word = word.lower().strip()
        char_list = list(word)
        char_list.sort()
        sign = "".join(char_list)
        #print(char_list)

        while low != high:
            center = int((low+high) / 2)
            center_words = linecache.getline(self.dict, center).split()
            center_sign = center_words[0]
            if center_sign < word:
                low = center + 1
            elif center_sign > word:
                high = center - 1
            
        print(center_words)


if __name__ == '__main__':
    anagram_searcher = AnagramSearcher()
    anagram_searcher.search("star")
