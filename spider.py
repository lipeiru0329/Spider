#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def spide_main(key_word):
    driver = webdriver.Chrome()
    driver.get('https://www.gebiz.gov.sg')

    driver.find_element_by_id('contentForm:searchBar_searchBar_INPUT-SEARCH').send_keys(key_word)
    # 3s
    time.sleep(3)

    driver.find_element_by_id('contentForm:searchBar_searchBar_BUTTON-GO').send_keys(Keys.ENTER)
    time.sleep(3)

    item_name = []
    item_name = driver.find_elements_by_class_name("commandLink_TITLE-BLUE")
    item_time = []
    item_time = driver.find_elements_by_class_name("formOutputText_VALUE-DIV")

    b = len(item_name)

    for z in range(0, b):
        print item_name.__getitem__(z).get_attribute('text')
        print item_time.__getitem__(1 + 3 * (z - 1)).text
        # print item_time.__getitem__(z).text
    print len(item_name)