

class Stack(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.size = 0

    def push(self, value):
        if self.size == self.capacity:
            raise OverflowError("Stack overflow: pilha cheia.")
        self.data.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Stack underflow: pilha vazia.")
        self.size -= 1
        return self.data.pop()

    def peek(self):
        if self.size == 0:
            raise IndexError("Pilha vazia.")
        return self.data[-1]

    def state(self):
        return {
            "data": self.data[:],
            "size": self.size,
            "capacity": self.capacity
        }
