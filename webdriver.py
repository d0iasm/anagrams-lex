from selenium import webdriver
from time import sleep
import anagram_finder


class WebDriver(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://icanhazwordz.appspot.com/')
        self.finder = anagram_finder.Anagram()

    def solve(self):
        chars = self.driver.find_elements_by_class_name('letter')
        word = []
        for char in chars:
            word.append(char.text)
        word = "".join(word)

        anagram = self.finder.find(word)
        self.driver.find_element_by_id('MoveField').send_keys(anagram)

        inputs = self.driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute("value") == "Submit":
                submit = input
                break
        submit.click()

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    webdriver = WebDriver()
    for i in range(10):
        webdriver.solve()
    webdriver.close()
