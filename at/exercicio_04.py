class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableChained:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity
        self.total_comparisons = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def _load_factor(self):
        return self.size / self.capacity

    def _rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        old_size = self.size
        self.size = 0

        for head in old_buckets:
            current = head
            while current is not None:
                self.put(current.key, current.value, rehashing=True)
                current = current.next

        self.size = old_size

    def put(self, key, value, rehashing=False):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            self.total_comparisons += 1
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

        if not rehashing and self._load_factor() > 0.75:
            self._rehash()

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            self.total_comparisons += 1
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        previous = None

        while current is not None:
            self.total_comparisons += 1
            if current.key == key:
                if previous is None:
                    self.buckets[index] = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def __len__(self):
        return self.size



def main():
    print("\n========== QUESTAO 4 ==========")
    table = HashTableChained()

    for i in range(20):
        table.put(f"key_item{i}", i)

    print("size:", len(table))
    print("capacity depois do rehash:", table.capacity)
    print("get key7:", table.get("key7"))
    print("get key15:", table.get("key15"))

    table.put("key7", 700)
    print("key7 updated:", table.get("key7"))

    table.delete("key15")
    print("after deleting key15:", table.get("key15"))
    print("accumulated comparisons:", table.total_comparisons)
    print("final load factor:", len(table) / table.capacity)


if __name__ == "__main__":
    main()
