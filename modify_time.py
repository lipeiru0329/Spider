import re
import time
from time import strptime

# Format modification in order to make the date gotten from page can be read by people


def modify_format(time_input):
    temp = re.findall(r'\d+', time_input)
    time_output = []
    time_output.append(temp[1])
    time_output.append(strptime(time_input.split(' ')[1],'%b').tm_mon)
    time_output.append(temp[0])
    if time_input.split(' ')[len(time_input.split(' ')) - 1] == 'AM':
        time_output.append(temp[2])
    else:
        time_output.append(str(int(temp[2]) + 12))
    time_output.append(temp[3])
    return time_output

