def func_4_1():
    with open('source/4_1.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            print('stop iteration')


def func_4_2():

    with open('source/4_1.txt') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, child):
        if isinstance(child, Node):
            self.children.append(child)

    def have_child(self):
        return True if len(self.children) != 0 else False

    def __iter__(self):
        print('iter')
        return iter(self.children)

def func_4_3():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = Node(3)

    child2.add_child(child3)

    root.add_child(child1)
    root.add_child(child2)

    def func_print_value(node):
        for item in node:
            print('*')
            if item.have_child():
                func_print_value(item)
            print(item)

    func_print_value(root)


class NodeTwo:

    def __init__(self, value):
        self.value = str(value)
        self.children = []

    def __repr__(self):
        return 'Node({})'.format(self.value)

    def __iter__(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def depth_first(self, prefix=''):
        self.value = prefix + self.value
        yield self
        for child in self.children:
            yield from child.depth_first(prefix + ' ')

def func_4_4():
    root = NodeTwo(0)
    child1 = NodeTwo(1)
    child2 = NodeTwo(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(NodeTwo(3))
    child1.add_child(NodeTwo(4))
    child2.add_child(NodeTwo(5))

    for ch in root.depth_first():
        print(ch)


from collections import deque


class CustomGenerator:

    def __init__(self, lines, max_length_queue=3):
        self.lines = lines
        self.history = deque(maxlen=max_length_queue)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

def func_4_5():
    with open('source/4_1.txt') as f:
        gen = CustomGenerator(f)

        for line in gen:
            if 'python' in  line:
                for lineno, hline in gen.history:
                    print('{} {}'.format(lineno, hline), end='')


import itertools
def func_4_6():
    def count(n):
        while True:
            yield n
            n += 1

    c = count(0)

    for item in itertools.islice(c, 10, 20):
        print(item)



from itertools import dropwhile, islice
def func_4_7():
    with open('source/4_6.txt') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')

def func_4_8():
    with open('source/4_6.txt') as f:
        for line in islice(f, 3, 6):
            print(line, end='')

def func_4_9():
    with open('source/4_6.txt') as f:
        while True:
            line = next(f)
            if not line.startswith('#'):
                break

        while line:
            print(line, end='')
            line = next(f, None)

    print('****')
    with open('source/4_6.txt') as f:
        lines = (line for line in f if not line.startswith('#'))
        for line in lines:
            print(line, end='')


if __name__ == '__main__':
    # func_4_1()
    # func_4_2()
    # func_4_3()
    # func_4_4()
    # func_4_5()
    # func_4_6()
    # func_4_7()
    # func_4_8()
    func_4_9()