#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache
import itertools
from dict import anagram_words as dict


class Node(object):
    """Element of trie."""
    def __init__ (self, id):
        self.id   = id
        self.next = {}
        self.output = []
        self.failure = 0
        self.footprint = {}


class Trie(object):
    """Preprocessing to find anagram."""
    def __init__ (self, dict):
        self.matched_words = set()
        self.thread = {}
        self.node = [Node(0)]
        self._make_goto(dict)
        self._make_failure()

    def _make_goto(self, dict):
        """Create Trie associated with current node and next."""
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
        """Create return positon if no next node."""
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

    def reset(self):
        """Reset the variable when finding continuously."""
        self.matched_words = set()
        self.thread = {}
        for node in self.node:
            node.footprint = {}

    def goto(self, id, char):
        """Move node by current position and next char."""
        if char in self.node[id].next:
            return self.node[id].next[char].id
        else:
            if id == 0: return 0
            else: return None

    def find(self, query, id=0):
        """Find all words matching the dict from Trie."""
        for i in range(len(query)):
            output = self.node[id].output
            if not len(output) == 0:
                for matching in output:
                    self.matched_words.add(matching)

            while self.goto(id, query[i]) is None:
                if len(query[i:]) > 1:
                    if query[i+1:] not in self.node[id].footprint.get(id, ""):
                        if id not in self.node[id].footprint:
                            self.node[id].footprint[id] = [query[i+1:]]
                        else:
                            self.node[id].footprint[id].append(query[i+1:])
                        self.thread[id] = query[i+1:]
                id = self.node[id].failure
            id = self.goto(id, query[i])

        while self.thread:
            item = self.thread.popitem()
            self.find(item[1], item[0])

        return list(self.matched_words)


class Anagram(object):
    """Find anagram with high score using Trie."""
    def __init__(self):
        sign_list = dict.data.keys()
        self.trie = Trie(sign_list)

    def high_score(self, words_list):
        """Return highest score and word."""
        high_score_word = words_list[0]
        high_score = 0

        three_points = ['j', 'k', 'q', 'x', 'z']
        two_points = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']

        for word in words_list:
            point = len(word) + 1
            for char in three_points:
                point += word.count(char) * 2

            for char in two_points:
                point += word.count(char)

            if high_score < point:
                high_score = point
                high_score_word = word

            print("{0}: {1}".format(dict.data[word][0], point*point))
        return high_score_word, high_score*high_score

    def find(self, word=input("--> ")):
        """Find anagram matching dictionary."""
        if len(word) < 3:
            print("at least 3 chars")
            return self.find(input("--> "))

        word = word.lower().strip()
        print("input: " + word)
        char_list = list(word)
        char_list.sort()
        sign = "".join(char_list)

        matched_words = self.trie.find(sign)
        self.trie.reset()
        if len(matched_words) == 0:
            print("not find anagrams")
        else:
            sign, high_score = self.high_score(matched_words)
            print("-- recomended word --")
            print("{0}: {1}".format(dict.data[sign][0], high_score))

        return self.find(input("--> "))


if __name__ == '__main__':
    anagram = Anagram()
    anagram.find()
