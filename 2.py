import re

def func_2_1():
    test = 'adb dsd,sdsd edwe;asds'
    fields = re.split(r'(;|,|\s)\s*', test)
    print(fields)

    fields2 = re.split(r'(?:;|,|\s)\s*', test)
    print(fields2)
    val = fields[::2]
    delemiter = fields[1::2]
    print(val)
    print(delemiter)
    print(zip(val, delemiter))
    print(''.join(v + d for v, d in zip(val, delemiter)))


import os


def func_2_2():
    filename = 'spam.txt'
    print(filename.startswith('spam'))
    print(filename.endswith('txt'))

    test = os.listdir('.')
    print(test)

    print( [name for name in test if name.endswith('.py')])

    gen = (name for name in test if name.endswith('.py'))

    for item in gen:
        print(item)

    print()



from fnmatch import fnmatch, fnmatchcase
def func_2_3():
    print(fnmatch('test.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Data45.csv', 'Dat2a[0-9]*'))

    test = ['test.txt', 'first.txt', 'second.py']

    print([name for name in test if fnmatch(name, '*.txt')])



def func_2_4():
    text = 'yeah, but no, but yeah, but no, but yeah'

    print(text.startswith('yeah'))
    print(text.endswith('no'))
    print(text.find('but'))


import re
def func_2_5():
    date_1 = '25/12/2019'
    date_2 = '25 12 2019'

    if re.match(r'\d+/\d+/\d+', date_1):
        print('yes')
    else:
        print('no')

    if re.match(r'\d+/\d+/\d+', date_2):
        print('yes')
    else:
        print('no')

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'\d+/\d+/\d+')
    print(datepat.findall(text))

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    f = datepat.findall(text)
    print(f)
    print(f[0])

    m = datepat.match('11/27/2012')
    print(m)
    print(m.group(0))
    print(m.group(1))

    print(m.groups())


from calendar import month_abbr


def func_2_6():
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

    text = 'yeah, but no, but yeah, but no, but yeah'
    text.replace('yeah', 'yep')
    print( text.replace('yeah', 'yep'))

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

    test = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(test)

    datapat = re.compile(r'(\d+)/(\d+)/(\d+)')

    test = datapat.sub(change_date, text)
    print('****', test)
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    print(datepat.sub(r'\3-\1-\2', text))


def func_2_7():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print(re.findall('python', text, flags=re.IGNORECASE))
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

    def matchcase(word):
        def replace(m):
            print(m.group())
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.lower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word

        return replace

    text = 'UPPER PYTHON, lower python, Mixed Python'
    test = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
    print('^^^^', text)

def func_2_8():
    text = 'Computer says "no." Phone says "yes."'
    str_pat = re.compile('\"(.*)\"')
    test = str_pat.findall(text)
    print(test)


    str_pat2 = re.compile('\"(.*?)\"')
    test = str_pat2.findall(text)
    print(test)

def func_2_9():
    test_1 = '''* this is
    a multiline_comment
    *'''

    datapat = re.compile(r'\*((?:.|\n)*?)\*')
    print(datapat.findall(test_1))


def func_2_10():
    test = '---hello---'
    print(test.strip('-'))

    test = '''
    hello
    '''

    print(test.strip())


if __name__ == "__main__":
    # func_2_1()
    # func_2_2()
    # func_2_3()
    # func_2_4()
    # func_2_5()
    # func_2_6()
    # func_2_7()
    # func_2_8()
    # func_2_9()
    func_2_10()