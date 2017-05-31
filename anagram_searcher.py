#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache
import itertools


class Node:
    def __init__ (self, id):
        self.id   = id
        self.next = {}
        self.output = []
        self.failure = 0

class Trie:
    def __init__ (self, dict):
        self.node  = [ Node(0) ]
        self._make_goto(dict)
        self._make_failure()

    def _make_goto(self, dict):
        """Create Trie associated with Node and next Node"""

        for word in dict:
            current = self.node[0]
            for char in word:
                if char not in current.next:
                    new_node = Node(len(self.node))
                    current.next[char] = new_node
                    self.node.append(new_node)
                current = current.next[char]
            current.output.append(word)


    def _make_failure(self):
        """Create return positon if no next Node"""
        
        queue = [0]
        while len(queue) > 0:
            id = queue.pop(0)
            for char in self.node[id].next.keys():
                next = self.goto(id, char)
                if next is not None: queue.append(next)
                if id != 0:
                    f = self.node[id].failure
                    while self.goto(f, char) is None:
                        f = self.node[f].failure
                    max_suffix = self.goto(f, char)
                    self.node[next].failure = max_suffix
                    self.node[next].output.extend(self.node[max_suffix].output)


    def goto(self, id, char):
        """Move Node by number of Node and char of query"""

        if char in self.node[id].next:
            return self.node[id].next[char].id
        else:
            if id == 0: return 0
            else: return None


    def lookup(self, query):
        """Look up all words matching the dict from Trie"""

        id = 0
        matched_words = []
        for char in query:
            output = self.node[id].output
            if not len(output) == 0: matched_words.extend(output)

            while self.goto(id, char) is None:
                id = self.node[id].failure
            id = self.goto(id, char)

        print(matched_words)


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
                if char in word: return word

            for char in two_points:
                if char in word: return word

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
            
            if all(x in sign for x in center_sign):
                print(self.high_score(center_words_list))
                return self.search(input('--> '))
            
            if center_sign < sign: low = center + 1
            else: high = center - 1

        print("not find anagrams")
        return self.search(input('--> ') + word)


if __name__ == '__main__':
    anagram_searcher = AnagramSearcher()
    anagram_searcher.search()

    dict_path = './dict/anagram_words'
    dict_list = [line for line in open(dict_path)]
    sign_list = [line.split()[0] for line in dict_list]
    trie = Trie(sign_list)
    print(sign_list)

    word = (input("--> "))
    word = word.lower().strip()
    char_list = list(word)
    char_list.sort()
    sign = "".join(char_list)
    print("sign:" + sign)
    trie.lookup(sign)

