class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("error: The queue is already empty.")

        return self._items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("error: The queue is already empty.")

        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({self._items})"


def main() -> None:
    queue = Queue()

    while True:
        print("\n--- Queue Operations Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Check if empty")
        print("5. Size")
        print("6. Display queue")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            item = input("Enter value to enqueue: ")
            queue.enqueue(item)
            print(f"Enqueued: {item}")

        elif choice == "2":
            try:
                removed_item = queue.dequeue()
                print(f"Dequeued: {removed_item}")
            except IndexError as error:
                print(error)

        elif choice == "3":
            try:
                print(f"Front element: {queue.front()}")
            except IndexError as error:
                print(error)

        elif choice == "4":
            print(f"Queue is empty: {queue.is_empty()}")

        elif choice == "5":
            print(f"Queue size: {queue.size()}")

        elif choice == "6":
            print(f"Current queue: {queue}")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
