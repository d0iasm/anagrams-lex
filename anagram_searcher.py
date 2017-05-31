#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache
import itertools
from dict import anagram_words as dict


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

        return matched_words


class Searcher:

    def __init__(self):
        sign_list = dict.data.keys()
        self.trie = Trie(sign_list)

    def high_score(self, words_list):
        three_points = ['j', 'k', 'q', 'x', 'z']
        two_points = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']

        for word in words_list:
            for char in three_points:
                if char in word: return word

            for char in two_points:
                if char in word: return word

        return words_list[0]

    def search(self, word=input("--> ")):
        if len(word) < 3:
            print("at least 3 chars")
            return self.search(input("--> "))

        word = word.lower().strip()
        print("input: " + word)
        char_list = list(word)
        char_list.sort()
        sign = "".join(char_list)

        matched_words = self.trie.lookup(sign)
        if len(matched_words) == 0:
            print("not find anagrams")
        else:
            high_score_sign = self.high_score(matched_words)
            print(dict.data[high_score_sign])

        return self.search(input("--> "))


if __name__ == '__main__':
    searcher = Searcher()
    searcher.search()
