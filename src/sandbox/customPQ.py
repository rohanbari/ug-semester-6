class PriorityQueue:
    """Custom PriorityQueue data structure in Python.
    """

    def __init__(self) -> None:
        self._queue = []

    def enqueue(self, elem) -> None:
        if not self.isEmpty() and type(self._queue[0]) != type(elem):
            print("error: Type mismatch!")
            return

        self._queue.append(elem)
        self._queue.sort(reverse=True)

    def dequeue(self):
        if self.isEmpty():
            print("error: The PQ is already empty.")
            return

        val = self._queue[0]
        del self._queue[0]

        return val

    def peek(self):
        return self._queue[0]

    def isEmpty(self) -> bool:
        return len(self._queue) == 0

    def __str__(self) -> str:
        return self._queue.__str__()


def main() -> None:
    print("Welcome to custom PriorityQueue!")
    pq = PriorityQueue()

    print(pq)
    pq.enqueue(10)
    print(pq)
    pq.enqueue(35)
    print(pq)
    pq.enqueue(20)
    print(pq)
    pq.enqueue(5)
    print(pq)


if __name__ == "__main__":
    main()
