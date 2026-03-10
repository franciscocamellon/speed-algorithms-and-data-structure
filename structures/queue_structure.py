
class Queue(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise OverflowError("Queue overflow: fila cheia.")

        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue underflow: fila vazia.")

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def peek(self):
        if self.size == 0:
            raise IndexError("Fila vazia.")
        return self.data[self.front]

    def state(self):
        return {
            "data": self.data[:],
            "front": self.front,
            "rear": self.rear,
            "size": self.size,
            "capacity": self.capacity
        }


