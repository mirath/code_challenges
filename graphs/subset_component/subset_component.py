#!python3

import os
import cProfile, pstats, io
from itertools import combinations as combinations_generator

def ones(n):
    ons = 0
    while n > 0:
        ons += n & 1
        n = n >> 1
    return ons

class DisjointElement(object): #pylint: disable=too-few-public-methods
    '''
    Class that holds the information of an element of a disjoint set
    This should really only be a dictionary/tuple, but the readibility of the code would suffer
    '''
    def __init__(self, elem):
        self.element = elem
        self.parent = None
        self.rank = 0
        self.component = elem

class Parents(object):
    def __init__(self, disjoint_set):
        self.disjoint_set = disjoint_set
        self.current_numbers = None
        self.ds_len = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.ds_len and \
              self.current_numbers[self.current].parent != self.current_numbers[self.current]:
            self.current += 1
        if self.current < self.ds_len:
            self.current += 1
            return self.current_numbers[self.current-1]
        else:
            raise StopIteration

    def reset(self):
        self.current = 0
        self.current_numbers = self.disjoint_set.current_numbers
        self.ds_len = len(self.current_numbers)

class DisjointSet(object):
    '''
    Disjoint Set data structure with find and union methods.
    It also implements path compression and union by rank, making the worst case for the find and
    union methods the inverse of the Ackerman function (so essentially constant)
    '''

    def __init__(self, elements):
        self.lookup = {}
        self.set = []
        self.current_numbers = None
        self.parents = None
        for elem in elements:
            disjoint_elem = DisjointElement(elem)
            self.lookup[elem] = disjoint_elem
            self.set.append(disjoint_elem)

    def init_combination(self, numbers):
        self.current_numbers = [self.lookup[n] for n in numbers]
        for number in numbers:
            disjoint_elem = self.lookup[number]
            disjoint_elem.parent = disjoint_elem

    def reset(self):
        for disjoint_elem in self.set:
            disjoint_elem.parent = None
            disjoint_elem.rank = 0
            disjoint_elem.component = disjoint_elem.element

    def components(self):
        ret = 64
        for e in self.current_numbers:
            if e.parent == e:
                ret -= ones(e.component)-1
        return ret

    def __find(self, disjoint_elem): #pylint: disable=missing-docstring
        if disjoint_elem.parent != disjoint_elem:
            root = self.__find(disjoint_elem.parent)
            disjoint_elem.parent = root
            return root

        return disjoint_elem

    def union(self, element_1, element_2): #pylint: disable=missing-docstring
        de1 = self.__find(self.lookup[element_1])
        de2 = self.__find(self.lookup[element_2])

        if de1.rank > de2.rank:
            de2.parent = de1
            de1.component |= de2.component
        elif de1.rank < de2.rank:
            de1.parent = de2
            de2.component |= de1.component
        else:
            de2.parent = de1
            de1.component |= de2.component
            de1.rank += 1


def findConnectedComponents(d):
    connected_components = 0

    disjoint_set = DisjointSet(d)
    for n in range(1, len(d)+1):
        combinations = combinations_generator(d, n)

        for comb in combinations:
            disjoint_set.init_combination(comb)
            for num_a in comb:
                for num_b in comb:
                    if num_a != num_b:
                        if num_a+num_b != num_a ^ num_b:
                            disjoint_set.union(num_a, num_b)
            connected_components += disjoint_set.components()
            disjoint_set.reset()

    return connected_components


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input())

    d = list(map(int, input().rstrip().split()))

    pr = cProfile.Profile()
    pr.enable()
    components = findConnectedComponents(d)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    '''
    components = findConnectedComponents(d)
    '''
    print(components+64) # +64 because the empty set will keep every node isolated

    #fptr.write(str(components+64) + '\n')

    #fptr.close()
