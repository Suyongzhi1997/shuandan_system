from random import Random


def random_str(random_length=8):
    r_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        r_str += chars[random.randint(0, length)]
    return r_str