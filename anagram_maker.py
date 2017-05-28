class AnagramMaker:

    def __init__(self):
        pass

    def sign(self, file_name):
        
        def list_to_dict(key_list, val_list):
            return dict(zip(key_list, val_list))

        f = open(file_name)
        line = f.readline()
        while line:
            lower_line = line.lower().strip()
            char_list = list(lower_line)
            char_list.sort()
            print("".join(char_list))
            line = f.readline()

        key_list = ["a", "b", "c"]
        val_list = ["hoge", "hoge", "hoge"]
        print(list_to_dict(key_list, val_list))


if __name__ == '__main__':
    anagram_maker = AnagramMaker()
    anagram_maker.sign("./dict/original_words_short")
