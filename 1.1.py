def func_1_1():
    print('func_1_1')
    p = (4, 5)
    x, y = p
    print("x {}; y {}".format(x, y))

    data =['TEST', 50, 15.1, (2012, 1, 1)]
    a, b, c, d = data
    print('a {} b {} c {} d {}'.format(a, b, c, d))

    a, b, c, (x, y, z) = data

    print('a {} b {} c {} d {} ___ x {} y {} z {}'.format(a, b, c, d, x, y, z))

    str = 'Hello'

    x, y, z, e, f, = str

    print('x {} y {} z {} e {} f {}'.format(x, y, z, e, f))

def func_1_2():
    list = [1, 2, 3, 4, 5, 6, 7]
    first, *middle, last = list
    print('firts {} middle {} last {}'.format(first, middle, last))

    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
    ]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(x):
        print('bar', x)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    def sum(data):
        head, *tail = data
        return head + sum(tail) if tail else head
    data = [1, 2, 3, 4, 5, 6]
    print('sum {}'.format(sum(data)))


def func_1_3():
    import heapq
    nums = [1,8, 2, 23,7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

    print('cheap {} expensive {}'.format(cheap, expensive))

    cheap = sorted(nums)[:4]
    expensive = sorted(nums)[:-1]
    print('sorted {}'.format(sorted(nums)))
    print('cheap1 {} expensive1 {}'.format(cheap, expensive))


import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def func_1_4():

    priority_queue = PriorityQueue()

    priority_queue.push('pr_1', 1)
    priority_queue.push('pr_2', 3)
    priority_queue.push('pr_3', 4)
    priority_queue.push('pr_4', 2)

    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())


from collections import defaultdict, OrderedDict


def func_1_5():
    # d = defaultdict(list)
    # for key, value in pairs:
    #     d[key].append(value)

    d = OrderedDict()

    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['f'] = 4

    for key, value in d.items():
        print('key {} value {}'.format(key, value))


def func_1_6():
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    print(min(zip(test_dict.values(), test_dict.keys())))


def func_1_7():
    test_dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    test_dict2 = {'a': 1, 'b': 222, 'c': 3, 'd': 4, 'z': 33, 'f': 23}

    print(test_dict1.keys() & test_dict2.keys())
    print(test_dict1.items() & test_dict2.items())

import os

def func_1_8():

    def dedupe(items, key=None):
        seen = set()

        for item in items:
            val = item if key == None else key(item)
            if val not in seen:
                seen.add(val)
                yield val


    file = os.getcwd() + '/test.txt'
    with open(file, 'r') as f:
        for line in dedupe(f):
            print(line)


def func_1_9():
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])
    print('func_1_9')
    print(cost)

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)

    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)





if __name__ == "__main__":
    func_1_1()
    func_1_2()
    func_1_3()
    func_1_4()
    func_1_5()
    func_1_6()
    func_1_7()
    func_1_8()
    func_1_9()
