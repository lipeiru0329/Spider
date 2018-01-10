import print_result

# Get the information on the page such as the paper name and date


def information(driver):
    item_name = []
    item_name = driver.find_elements_by_class_name("commandLink_TITLE-BLUE")
    item_time = []
    item_time = driver.find_elements_by_class_name("formOutputText_VALUE-DIV")

    print_result.print_result(item_name, item_time)