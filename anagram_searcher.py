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
        #sign = "".join(char_list)
        #print(char_list)

        center_words = linecache.getline(self.dict, (low+high) / 2)
        print(center_words.split())


if __name__ == '__main__':
    anagram_searcher = AnagramSearcher()
    anagram_searcher.search("star")
