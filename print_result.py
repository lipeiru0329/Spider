import modify_time

# Print the information gotten from the page


def print_result(item_name, item_time):
    b = len(item_name)

    for z in range(0, b):
        print item_name.__getitem__(z).get_attribute('text')
        print item_time.__getitem__(1 + 3 * (z - 1)).text
        print modify_time.modify_format(str(item_time.__getitem__(1 + 3 * (z - 1)).text))
        # print item_time.__getitem__(z).text
    print len(item_name)