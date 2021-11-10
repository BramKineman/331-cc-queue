"""
CC6 - It's As Easy As 01-10-11
Name: 
"""

from typing import Generator, Any


class Node:
    """
    Node Class
    :value: stored value
    :next: reference to next node
    """

    def __init__(self, value) -> None:
        """
        Initializes the Node class
        """
        self.value: str = value
        self.next: Node = None

    def __str__(self) -> str:
        """
        Returns string representation of a Node
        """
        return self.value


class Queue:
    """
    Queue Class
    :first: reference to first node in the queue
    :last: reference to last node in the queue
    """

    def __init__(self):
        """Create an empty queue."""
        self._size = 0
        self.first: Node = None
        self.last: Node = None

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def pop(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        :return: Value of Node removed from queue.
        """
        if self.first is None:
            return ""
        answer = self.first.value
        self.first = self.first.next
        self._size -= 1
        return answer

    def insert(self, value: str):
        """
        Add an element to the back of queue.
        :param value: String value to be added to queue.
        :return: None
        """
        # check q size: if empty, assign self.first and self.last -> same thing
        if self.first is None:
            initial_node = Node(value)
            self.first = initial_node
            self.last = initial_node
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

        self._size += 1


def alien_communicator(n: Any) -> Generator[str, None, None]:
    """
    Creates a generator object of strings representing binary numbers of 0 to n inclusive.
    :param n: any built-in type in python.
    :return: Generator object of strings representing binary numbers of 0 to n inclusive
    if n is an int, None otherwise.
    """
    is_int = isinstance(n, int)
    # special case with bools
    if is_int and not isinstance(n, bool) and n >= 0:
        yield "0"
        my_q = Queue()
        my_q.insert("1")
        while n > 0:
            first = my_q.pop()
            second = first
            my_q.insert(first + "0")
            my_q.insert(second + "1")
            yield first
            n -= 1
