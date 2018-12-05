import random

import dateparser


def parse_datetime(string):
    """
    parse string to datetime safely
    :param string: str to parse
    :return: datetime
    """
    if not string:
        return None
    return dateparser.parse(str(string))


def first(array):
    """
    get first element of list or None
    :param array:
    :return:
    """
    if isinstance(array, list) and len(array) > 1:
        return array[0]
    return None


def mix(x):
    """mix params for request videos"""
    character = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<>./#:@()`^'
    rst = ''
    for _ in range(x):
        tmp = random.choice(character)
        rst += tmp
    return rst
