class Stack:
    def __init__(self):
        self.items = []  # O(1) - initialization

    def push(self, item):
        self.items.append(item)  # O(1) - append to end of list

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1) - remove from end of list
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # O(1) - access last element
        return None

    def is_empty(self):
        return len(self.items) == 0  # O(1) - check list length