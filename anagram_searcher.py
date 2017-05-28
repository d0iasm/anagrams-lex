#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache


class AnagramSearcher:

    def __init__(self):
        self.dict = "./dict/anagram_words"
        self.num = sum(1 for line in open(self.dict))

    def high_score(self, words_list):
        words_list = words_list[1:]
        
        three_points = ['j', 'k', 'q', 'x', 'z']
        two_points = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']

        for word in words_list:
            for char in three_points:
                if char in word:
                    return word

            for char in two_points:
                if char in word:
                    return word

        return words_list[0]


    def search(self, word=input('--> ')):
        if len(word) < 3:
            print("at least 3 chars")
            return self.search(input('--> '))

        low = 0
        high = self.num

        word = word.lower().strip()
        char_list = list(word)
        char_list.sort()
        sign = "".join(char_list)

        while low != high:
            center = int((low+high) / 2)
            center_words = linecache.getline(self.dict, center)
            center_words_list = center_words.split()
            center_sign = center_words_list[0]
            if center_sign < sign:
                low = center + 1
            elif center_sign > sign:
                high = center - 1
            else:
                print(self.high_score(center_words_list))
                return self.search(input('--> '))
        
        print("not find anagrams")
        self.search(input('--> '))


if __name__ == '__main__':
    anagram_searcher = AnagramSearcher()
    anagram_searcher.search()
