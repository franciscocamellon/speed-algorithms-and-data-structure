class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_first(self, value):
        node = DoublyNode(value)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def insert_last(self, value):
        node = DoublyNode(value)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise IndexError("Empty list.")

        value = self.head.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return value

    def delete_last(self):
        if self.is_empty():
            raise IndexError("Empty list.")

        value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return value


class Deque:
    def __init__(self):
        self.data = DoublyLinkedList()

    def insert_left(self, value):
        self.data.insert_first(value)

    def insert_right(self, value):
        self.data.insert_last(value)

    def remove_left(self):
        return self.data.delete_first()

    def remove_right(self):
        return self.data.delete_last()

    def peek_left(self):
        if self.data.is_empty():
            raise IndexError("Empty deque.")
        return self.data.head.value

    def peek_right(self):
        if self.data.is_empty():
            raise IndexError("Empty deque.")
        return self.data.tail.value



def check_invariants(linked_list):
    if linked_list.size == 0:
        return linked_list.head is None and linked_list.tail is None

    if linked_list.head.prev is not None:
        return False
    if linked_list.tail.next is not None:
        return False

    count = 0
    current = linked_list.head
    last = None

    while current is not None:
        last = current
        if current.next is not None and current.next.prev != current:
            return False
        current = current.next
        count += 1

    if last != linked_list.tail:
        return False

    return count == linked_list.size



def main():
    print("\n========== QUESTAO 7 ==========")
    dq = Deque()

    dq.insert_left(10)
    dq.insert_right(20)
    dq.insert_left(5)
    dq.insert_right(30)

    print("left:", dq.peek_left())
    print("right:", dq.peek_right())
    print("remove_left:", dq.remove_left())
    print("remove_right:", dq.remove_right())
    print("invariants ok:", check_invariants(dq.data))
    print("size:", dq.data.size)


if __name__ == "__main__":
    main()