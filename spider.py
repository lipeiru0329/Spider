#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import print_result
import get_information
import modify_time


def spide_main(key_word):
    driver = webdriver.Chrome()
    driver.get('https://www.gebiz.gov.sg')

    driver.find_element_by_id('contentForm:searchBar_searchBar_INPUT-SEARCH').send_keys(key_word)
    # 3s
    time.sleep(3)

    driver.find_element_by_id('contentForm:searchBar_searchBar_BUTTON-GO').send_keys(Keys.ENTER)
    time.sleep(3)

    get_information.information(driver)

    next_page = "contentForm:j_idt765:j_idt816_Next_"
    page_number = 2

    while(driver.find_element_by_id(next_page + str(page_number)).is_enabled()):
        driver.find_element_by_id(next_page + str(page_number)).send_keys(Keys.ENTER)
        time.sleep(3)

        get_information.information(driver)
        page_number = page_number + 1
    # item_name = []
    # item_name = driver.find_elements_by_class_name("commandLink_TITLE-BLUE")
    # item_time = []
    # item_time = driver.find_elements_by_class_name("formOutputText_VALUE-DIV")
    #
    # print_result.print_result(item_name, item_time)



