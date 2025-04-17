class Queue:
    def __init__(self):
        self.items = []  # O(1) - initialization

    def enqueue(self, item):
        self.items.append(item)  # O(1) - append to end of list

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # O(n) - remove from front (inefficient)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # O(1) - access first element
        return None

    def is_empty(self):
        return len(self.items) == 0  # O(1) - check list length