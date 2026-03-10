from structures.queue_structure import Queue


def main():
    queue = Queue(4)

    print("Estado inicial:", queue.state())

    queue.enqueue("A")
    print("Após enqueue(A):", queue.state())

    queue.enqueue("B")
    print("Após enqueue(B):", queue.state())

    queue.enqueue("C")
    print("Após enqueue(C):", queue.state())

    print("dequeue():", queue.dequeue())  # A
    print("Após dequeue():", queue.state())

    queue.enqueue("D")
    print("Após enqueue(D):", queue.state())

    print("dequeue():", queue.dequeue())  # B
    print("dequeue():", queue.dequeue())  # C
    print("dequeue():", queue.dequeue())  # D
    print("Estado final:", queue.state())


if __name__ == "__main__":
    main()
