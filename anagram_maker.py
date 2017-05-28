from collections import defaultdict
from functools import reduce


class AnagramMaker:

    def __init__(self):
        pass

    def sign(self, file_name):
        
        d = defaultdict(set)

        f = open(file_name)
        line = f.readline()
        while line:
            word = line.lower().strip()
            char_list = list(word)
            char_list.sort()
            sign = "".join(char_list)
            
            d[sign].add(word)
            
            line = f.readline()
        
        
        print(d)
        print(d["aacehn"])

if __name__ == '__main__':
    anagram_maker = AnagramMaker()
    anagram_maker.sign("./dict/original_words_short")
