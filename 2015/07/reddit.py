import sys
import functools

data = {}

for line in sys.stdin.readlines():
    cmd, key = line.split(" -> ")
    data[key.strip()] = cmd

@functools.lru_cache()
def get_value(key):
    """ key e un numar sau un literal"""
    try:
        return int(key)
    except ValueError:
        """ echivalent cu No Operation """
        pass    

    """ tot timpul data[key] este o lista """
    cmd = data[key].split(" ") 

    if "NOT" in cmd:
        return ~get_value(cmd[1])
    elif "AND" in cmd:
        return get_value(cmd[0]) & get_value(cmd[2])
    elif "OR" in cmd:
        return get_value(cmd[0]) | get_value(cmd[2])
    elif "LSHIFT" in cmd:
        return get_value(cmd[0]) << get_value(cmd[2])
    elif "RSHIFT" in cmd:
        return get_value(cmd[0]) >> get_value(cmd[2])
    else:
        return get_value(cmd[0])

print('first result is: ', get_value("a"))
data['b'] = str(get_value("a"))
get_value.cache_clear()
print('second result is: ', get_value("a"))