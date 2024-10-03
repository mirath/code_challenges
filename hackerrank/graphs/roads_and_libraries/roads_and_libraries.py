#!/bin/python3

import sys

class DisjointElement(object):
    def __init__(self, elem):
        self.element = elem
        self.parent = self
        self.rank = 0


class DisjointSet(object):
    def __init__(self, elements):
        self.lookup = {}
        self.set = []
        for e in elements:
            de = DisjointElement(e)
            self.lookup[e] = de
            self.set.append(de)

    def find(self, e):
        de = self.lookup[e]
        return self.__find(de, []).element

    def __find(self, de, path):
        if de.parent != de:
            path.append(de)
            return self.__find(de.parent, path)

        for e in path:
            e.parent = de

        return de

    def union(self, e1, e2):
        de1 = self.__find(self.lookup[e1], [])
        de2 = self.__find(self.lookup[e2], [])

        if de1.rank > de2.rank:
            de2.parent = de1
        elif de1.rank < de2.rank:
            de1.parent = de2
        else:
            de2.parent = de1
            de1.rank += 1


def roadsAndLibraries(n, c_lib, c_road, cities):
    elements = set()

    if c_road < c_lib:
        for c in cities:
            elements.add(c[0])
            elements.add(c[1])
        djs = DisjointSet(elements)

        repair_cost = 0
        graphs_n = n # The number of connected graphs
        for c in cities:
            a = c[0]
            b = c[1]

            # Find out in which set is each node
            s1 = djs.find(a)
            s2 = djs.find(b)

            # If they are not in the same set, add it to the MST and join the sets
            if s1 != s2:
                repair_cost += c_road
                djs.union(s1, s2)
                graphs_n -= 1

        return repair_cost + c_lib * graphs_n
    else:
        return n * c_lib


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
           cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
