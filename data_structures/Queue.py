class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  # Primer nodo
        self.tail = None  # Último nodo
        self._length = 0  # Contador de elementos

    def enqueue(self, item):
        """Añade un elemento al final (rastreable en memoria)"""
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def dequeue(self):
        """Elimina y devuelve el primer elemento (O(1))"""
        if self.head is None:
            return None
        removed = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._length -= 1
        return removed

    def search(self, item):
        """Busca un elemento (O(n))"""
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def is_empty(self):
        """Verifica si está vacía (O(1))"""
        return self.head is None

    def peek(self):
        """Devuelve el primer elemento sin eliminarlo"""
        return self.head.value if self.head else None

    def __len__(self):
        """Número de elementos (O(1))"""
        return self._length

    @property
    def items(self):
        """Devuelve todos los elementos como lista (para depuración)"""
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements