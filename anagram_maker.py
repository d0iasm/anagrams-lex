from collections import defaultdict
from functools import reduce


class AnagramMaker:

    def __init__(self):
        pass

    def sign(self, file_name):
        
        d = defaultdict(list)

        f = open(file_name)
        line = f.readline()
        while line:
            word = line.lower().strip()
            char_list = list(word)
            char_list.sort()
            sign = "".join(char_list)
            
            d.update({sign: word})
            
            line = f.readline()
        
        
        print(d.items())
        print(d["aaccr"])

if __name__ == '__main__':
    anagram_maker = AnagramMaker()
    anagram_maker.sign("./dict/original_words_short")
