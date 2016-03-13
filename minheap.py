#! /usr/bin/env python

"""
Function of minimum heap optimization
"""

from __future__ import print_function, division


class Node(object):

#  Class, which defines a features and behavour of heap's node

# The function initializes the object's item and priority
    def __init__(self, item, priority):
        self._item = item
        self._priority = priority

# Why is two same decorators here?!
    @property
    def item(self):
        return self._item

    @property
    def priority(self):
        return self._priority

# The function brings decorator's output data into string format
    def __str__(self):
        return str((self.item, self.priority))

# N O  I D E A
    def __ne__(self, other):
        """
        :type other: Node
        :return:
        """
        return not self == other

    def __eq__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority == other.priority

    def __gt__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority > other.priority

    def __ge__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority >= other.priority

    def __lt__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority <= other.priority


class MinHeap(object):
# Class, which defines a heap's features and behavour
    """
    :type _heap: list
    """
# 0 is the first erzats-element in list of nodes. It's index is 0
# We do it to make index corresponding with the number of element
    def __init__(self):
        self._heap = [0]

# The function counts the quantity of elements wihout erzats-element
    def __len__(self):
        return len(self._heap) - 1

# The function check the heap to be non-empty(has at least 1 node)
    def __nonzero__(self):
        return bool(len(self))

# The function exchanges two nodes in pair parent-child
    def _exchange(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

# The following 2 functions check the main heap property and the exchange nessesity
    def _percolate_up(self, i):
        cur_pos = i
        while cur_pos // 2 > 0:
            parent_idx = self._parent_idx(i)
            if self._heap[cur_pos] >= self._heap[parent_idx]:
                break
            self._exchange(cur_pos, parent_idx)
            cur_pos //= 2

    def _percolate_down(self, i):
        while (i * 2) <= len(self):
            min_child_index = self._min_child_idx(i)
            if self._heap[i] > self._heap[min_child_index]:
                self._exchange(i, min_child_index)
            i = min_child_index

# The function match children with their indices and returns the child, whose index is lowest
    def _min_child_idx(self, i):
        children_indices = self._children_indices(i)
        if not children_indices:
            return None
        children = [self._heap[idx] for idx in children_indices]
        return sorted(zip(children, children_indices))[0][1]

    @staticmethod
    def _parent_idx(i):
        return i // 2

# The function returns a tuple with 2 children, if they are in the heap
    def _children_indices(self, i):
        possible_children = [i * 2, (i * 2) + 1]
        return tuple(idx for idx in possible_children if idx <= len(self))

# The function takes the first node in heap and checks the heap is non-empty
    def get_min(self):
        if not self:
            raise ValueError("The heap is empty")
        return self._heap[1]

# The function returns the first heap element and removes it from a heap
    def pop_min(self):
        min_val = self.get_min()
        self._exchange(1, len(self))
        self._heap.pop()
        self._percolate_down(1)
        return min_val

# The function adds item to the heap
    def push(self, item):
        """
        :type item: Node
        """
        if not isinstance(item, Node):
            raise ValueError("`item` should be a `Node` instance")
        self._heap.append(item)
        self._percolate_up(len(self))

# The class for memoization???
class Memoize(object):
    def __init__(self, func):
        self._func = func
        self._cache = {}

    def __call__(self, *args):
        return args not in self.cache and self.cache.update(
            {args: self.func(*args)}) or self.cache.get(args)

    @property
    def cache(self):
        return self._cache

    @property
    def func(self):
        return self._func

    def is_cached(self, *args):
        return frozenset(args) in self.cache


@Memoize               # sqrt = Memoize(sqrt)
def sqrt(num):
    return num ** 0.5


def test_heap():
    heap = MinHeap()
    nodes = [Node(val, val) for val in xrange(9, -1, -1)]
    for node in nodes:
        heap.push(node)
    while heap:
        print(heap.pop_min())


def main():
    test_heap()

if __name__ == "__main__":
    main()
