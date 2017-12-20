import re
import time
from time import strptime


def modify_format(time_input):
    temp = re.findall(r'\d+', time_input)
    time_output = []
    time_output[0] = temp[1]
    time_output[1] = strptime(time_input.split(' ')[1],'%b').tm_mon
    time_output[2] = temp[0]
    if time_input.split(' ')[len(a.split(' ')) - 1] == 'AM':
        time_output[3] = temp[2]
    else:
        time_output[3] = temp[2] + 12
    time_output[4] = temp[3]
    return time_output

