def func_2_14():
    text = 'Hello world'
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))

    print(text.ljust(20, '='))
    print(text.center(20, '*'))

    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))

    print('_____')
    print(format(text, '=>20s'))
    print(format(text, '*^20'))
    print('_____')
    print('{:>10s} {:>10s}'.format('Hello', 'World'))

def func_2_15():
    test = '{a}, {b}'

    print(test.format(a='var a', b='var b'))

    dict_test = {'a': 10, 'b': 20}

    print(test.format(**dict_test))
    print(type(dict_test))

    for a in dict_test.items():
        print(a)
        print(type(a))

def func_2_16():
    test_list = ['test1', 'test2', 'test3', 'test4']
    ' '.join(test_list)

    b = 'test' 'test2'
    print(b)


def func_2_17():
    data = ['10', 100, 'test_1']

    test = ' '.join(str(d) for d in data)
    print(test)
    # a = '1'
    # b = '2'
    # c = '3'
    # print(a, b, c, sep=':')

    def sample():
        yield 'test1'
        yield 'test2'
        yield 'test3'
        yield 'test4'

    for item in sample():
        print(item)

    print(' '.join(sample()))



def combine(source, maxsize):
    parts = []
    size = 0

    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            print('if')
            yield ' '.join(parts)
            parts = []
            size = 0
    print(size)
    yield ' '.join(parts)


def func_2_18():
    def sample():
        yield 'test1'
        yield 'test2'
        yield 'test3'
        yield 'test4'

    for part in combine(sample(), 10):
        print(part)


class Car:
    def __init__(self):
        self.color = 'red'
        self.mark = 'audi'


def func_2_19():
    str_car = 'Mark {mark} color {color}'

    color = 'red'
    mark = 'audi'
    print(vars())
    print(str_car.format_map(vars()))



    car = Car()


    print(str_car.format_map(vars(car)))


class CustomDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

import sys
def func_2_20():
    color = 'black'
    custom_dict = CustomDict(vars())
    str_car = 'Mark {mark} color {color}'

    print(str_car.format_map(custom_dict))


    print(sys._getframe(1).f_locals)


import os
import textwrap

def func_2_21():
    columns = os.get_terminal_size().columns
    print(columns)
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    print(textwrap.fill(s, columns, initial_indent='___', subsequent_indent='___'))
    print(textwrap.fill(s, 20, initial_indent='___', subsequent_indent='****'))


import html
def func_2_21():
    s = 'Elements are written as "<tag>text</tag>".'

    print(html.escape(s))
    print(html.escape(s, quote=False))

    s_un = 'Spicy &quot;Jalape&#241;o&quot.'

    print(html.unescape(s_un))


if __name__ == '__main__':
    # func_2_14()
    # func_2_15()
    # func_2_16()
    # func_2_17()
    # func_2_18()
    # func_2_19()
    # func_2_20()
    func_2_21()