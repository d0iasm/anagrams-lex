from collections import defaultdict
from functools import reduce


class AnagramMaker:

    def __init__(self):
        pass

    def sign(self, file_name):
        
        d = defaultdict(set)

        with open(file_name) as f:
            for line in f:
                word = line.lower().strip()
                char_list = list(word)
                char_list.sort()
                sign = "".join(char_list)
            
                d[sign].add(word)
            
        #print(d)
        #print(d["aacehn"])
        return d

    def sort(self, sign_dict):
        for k, v in sorted(sign_dict.items()):
            print(k, v)



if __name__ == '__main__':
    anagram_maker = AnagramMaker()
    anagram_maker.sort(anagram_maker.sign("./dict/original_words_short"))
