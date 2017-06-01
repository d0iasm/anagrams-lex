from selenium import webdriver
from time import sleep


class WebDriver(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://icanhazwordz.appspot.com/')

    def solve(self):
        words = self.driver.find_elements_by_class_name('letter')
        for word in words:
            print(word.text)
        self.driver.find_element_by_id('MoveField').send_keys("anagram")
        
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
    webdriver.solve()
