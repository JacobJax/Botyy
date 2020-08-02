from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Dwnl_bot():
    def __init__(self, target = 'https://www.mp3juices.cc/'):
        self.target = target
        self.bot = webdriver.Firefox()

    def get_to_site(self):
        bot = self.bot
        bot.get(self.target)
        time.sleep(3)

    def search(self, song):
        bot = self.bot
        search_box = bot.find_element_by_id('query')

        search_box.clear()
        search_box.send_keys(song)
        
        search_button = bot.find_element_by_class_name('fa-search')
        search_button.click()
        time.sleep(1)
        search_button.click()



# functionality
searching = True
print('\n')
print('Hi there, Welcome to Botty')
print('[Manual]: Botty is a web bot that serches you a song from \'https://www.mp3juices.cc/\' \n Once searched, you can proceed to download or stream from the site')

while  searching:
    song = input('Which song would you like to search: ')
    new_bot = Dwnl_bot()
    new_bot.get_to_site()
    new_bot.search(song)

    print('\n')
    an_try = input('Would you like to search again?: [Yes/No] ')
    if an_try.lower().startswith('n'):
        print('... Bye!!')
        searching = False
        break
    else:
        continue