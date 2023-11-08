# Author: John Jiang
# Date  : 2016/8/21
from random import randint

import requests

try:
    import config
except ImportError:
    pass
else:
    API_KEY = config.key

__all__ = ['set_api_key', 'generate_integers', 'generate_gaussians', 'generate_decimal_fractions', 'generate_strings',
           'generate_UUIDs', 'generate_blobs']


def set_api_key(key):
    global API_KEY
    API_KEY = key


def to_camel(key):
    if not isinstance(key, str):
        return None
    first, *rest = key.split('_')
    if not rest:
        return first
    return first + ''.join(x.capitalize() for x in rest)


def make_api(func):
    def wrapper(**kwargs):
        kwargs = {to_camel(key): value for key, value in kwargs.items()}
        func_name = to_camel(func.__name__)
        func(**kwargs)
        return get_random(func_name, kwargs)

    return wrapper


def get_random(method, params=None, id=None):
    if id is None:
        id = randint(1, 999)
    data = {
        'jsonrpc': '2.0',
        'method': method,
        'params': {'apiKey': API_KEY},
        'id': id
    }
    data['params'].update(params)

    api_url = 'https://api.random.org/json-rpc/1/invoke'
    r = requests.post(api_url, json=data)
    j = r.json()
    if 'error' in j:
        raise AttributeError(j['error']['message'])
    try:
        return j['result']['random']['data']
    except KeyError:
        return j['result']


@make_api
def generate_integers(*, n, min, max, replacement=True, base=10):
    """
    generates true random integers within a user-defined range.

    :param n: How many random integers you need. Must be within the [1,1e4] range.
    :param min: The lower boundary for the range from which the random numbers will be picked. Must be within the [-1e9,1e9] range.
    :param max: The upper boundary for the range from which the random numbers will be picked. Must be within the [-1e9,1e9] range.
    :param replacement: Specifies whether the random numbers should be picked with replacement.
    :param base: Specifies the base that will be used to display the numbers. Values allowed are 2, 8, 10 and 16.
    :return:
    """
    print('geting integers')


@make_api
def generate_decimal_fractions(*, n, decimal_places, replacement=True):
    """
    generates true random decimal fractions from a uniform distribution across the [0,1] interval with a user-defined number of decimal places.

    :param n: How many random decimal fractions you need. Must be within the [1,1e4] range.
    :param decimal_places: The number of decimal places to use. Must be within the [1,20] range.
    :param replacement: Specifies whether the random numbers should be picked with replacement.
    :return: An array containing the sequence of numbers requested.
    """


@make_api
def generate_gaussians(*, n, mean, standard_deviation, significant_digits):
    """
    generates true random numbers from a Gaussian distribution (also known as a normal distribution).

    :param n: How many random numbers you need. Must be within the [1,1e4] range.
    :param mean: The distribution's mean. Must be within the [-1e6,1e6] range.
    :param standard_deviation: The distribution's standard deviation. Must be within the [-1e6,1e6] range.
    :param significant_digits: The number of significant digits to use. Must be within the [2,20] range.
    :return: An array containing the sequence of numbers requested.
    """


@make_api
def generate_strings(*, n, length, characters, replacements=True):
    """
    generates true random strings

    :param n: How many random strings you need. Must be within the [1,1e4] range.
    :param length: The length of each string. Must be within the [1,20] range. All strings will be of the same length
    :param characters: A string that contains the set of characters that are allowed to occur in the random strings. The maximum number of characters is 80.
    :param replacements: Specifies whether the random strings should be picked with replacement.
    :return: An array containing the strings requested.
    """


@make_api
def generate_UUIDs(*, n):
    """
    generates version 4 true random Universally Unique IDentifiers(UUIDs) in accordance with section 4.4 of RFC
    4122.

    :param n: How many random UUIDs you need. Must be within the [1,1e3] range.
    :return: An array containing the sequence of UUIDs requested, represented as strings.
    """


@make_api
def generate_blobs(*, n, size, format='base64'):
    """
    generates Binary Large OBjects (BLOBs) containing true random data.

    :param n: How many random blobs you need. Must be within the [1,100] range.
    :param size: The size of each blob, measured in bits. Must be within the [1,1048576] range and must be divisible by 8.
    :param format: Specifies the format in which the blobs will be returned. Values allowed are base64 and hex.
    :return: An array containing the blobs requested.
    The total size of all blobs requested must not exceed 1,048,576 bits (128 KiB)
    """


@make_api
def get_usage():
    """
     Get the information related to the the usage of a given API key
    """


if __name__ == '__main__':
    print(generate_integers(n=5, min=1, max=10))
    # print(generate_decimal_fractions(n=10, decimal_places=10))
    # print(generate_gaussians(n=10, mean=100, standard_deviation=99, significant_digits=5))
    # print(get_usage())
