class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # ---- Inserción (O(log n)) ----
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Rotaciones basadas en balance, no en valores
        if balance > 1:
            if self._get_balance(node.left) >= 0:  # Left-Left
                return self._right_rotate(node)
            else:  # Left-Right
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:  # Right-Right
                return self._left_rotate(node)
            else:  # Right-Left
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        return node

    # ---- Eliminación (O(log n)) ----
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node
        elif value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.value = temp.value
                node.right = self._delete_recursive(node.right, temp.value)

        if not node:  # Nodo eliminado, no hay nada que balancear
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Balanceo después de eliminar
        if balance > 1:
            if self._get_balance(node.left) >= 0:  # Left-Left
                return self._right_rotate(node)
            else:  # Left-Right
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:  # Right-Right
                return self._left_rotate(node)
            else:  # Right-Left
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        return node

    # ---- Búsqueda (O(log n)) ----
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # ---- Helpers ----
    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        if not y:  # Prevenir rotación inválida
            return z
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        if not y:  # Prevenir rotación inválida
            return z
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current