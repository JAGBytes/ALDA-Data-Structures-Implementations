class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Nodo superior
        self._length = 0  # Contador de elementos

    def push(self, item):
        """Apila un elemento (rastreable en memoria)"""
        new_node = Node(item)
        new_node.next = self.top  # El nuevo nodo apunta al antiguo top
        self.top = new_node       # Actualiza el top
        self._length += 1

    def pop(self):
        """Desapila y devuelve el elemento superior (O(1))"""
        if self.top is None:
            return None
        popped = self.top.value
        self.top = self.top.next  # Mueve el top al nodo anterior
        self._length -= 1
        return popped

    def search(self, item):
        """Busca un elemento (O(n))"""
        current = self.top
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def peek(self):
        """Muestra el elemento superior sin desapilar"""
        return self.top.value if self.top else None

    def is_empty(self):
        """Verifica si está vacía (O(1))"""
        return self.top is None

    def __len__(self):
        """Número de elementos (O(1))"""
        return self._length

    @property
    def items(self):
        """Devuelve todos los elementos como lista (para depuración)"""
        elements = []
        current = self.top
        while current:
            elements.append(current.value)
            current = current.next
        return elements