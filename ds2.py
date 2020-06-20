from ds import DoubleLinkedList


class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self, val):
        self.__list.add(val)

    def deque(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def front(self):
        return self.__list.front()

    def is_empty(self):
        return self.__list.size == 0

    def __len__(self):
        return self.__list.size


from collections import deque

my_queue = Queue()
my_queue.enqueue(1)
print(len(my_queue))
print(my_queue.front())
my_queue.enqueue(1)
my_queue.enqueue(4)
my_queue.enqueue(10)
my_queue.enqueue(111)
print(my_queue.front())
print(len(my_queue))
print(my_queue.deque())
print(my_queue.front())
my_queue.deque()
print(my_queue.front())

