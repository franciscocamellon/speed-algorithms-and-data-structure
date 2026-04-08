class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, value):
        node = SinglyNode(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_last(self, value):
        node = SinglyNode(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

        self.size += 1

    def search(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def delete(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index.")

        if index == 0:
            self.insert_first(value)
            return

        node = SinglyNode(value)
        current = self.head
        position = 0

        while position < index - 1:
            current = current.next
            position += 1

        node.next = current.next
        current.next = node
        self.size += 1

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index.")

        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value

        current = self.head
        position = 0

        while position < index - 1:
            current = current.next
            position += 1

        removed = current.next
        current.next = removed.next
        self.size -= 1
        return removed.value

    def __len__(self):
        return self.size

    def __str__(self):
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.value))
            current = current.next

        return " -> ".join(values) if values else "empty list"



def main():
    print("\n========== QUESTAO 6 ==========")
    linked_list = SinglyLinkedList()
    linked_list.insert_first(20)
    linked_list.insert_first(10)
    linked_list.insert_last(30)
    linked_list.insert_at(1, 15)

    print(linked_list)
    print("search 20:", linked_list.search(20))
    print("delete 15:", linked_list.delete(15))
    print(linked_list)
    print("delete_at(1):", linked_list.delete_at(1))
    print(linked_list)
    print("size:", len(linked_list))



if __name__ == "__main__":
    main()