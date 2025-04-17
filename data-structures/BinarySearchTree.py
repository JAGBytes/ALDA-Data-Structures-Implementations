class TreeNode:
    def __init__(self, value):
        self.value = value  # O(1)
        self.left = None    # O(1)
        self.right = None   # O(1)

class BinarySearchTree:
    def __init__(self):
        self.root = None  # O(1) - initialization

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)  # O(1)
        else:
            self._insert_recursive(value, self.root)  # O(log n) avg, O(n) worst

    def _insert_recursive(self, value, node):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)  # O(1)
            else:
                self._insert_recursive(value, node.left)  # recurse left
        else:
            if not node.right:
                node.right = TreeNode(value)  # O(1)
            else:
                self._insert_recursive(value, node.right)  # recurse right

    def search(self, value):
        return self._search_recursive(value, self.root)  # O(log n) avg, O(n) worst

    def _search_recursive(self, value, node):
        if not node:
            return False  # O(1)
        if value == node.value:
            return True  # O(1)
        elif value < node.value:
            return self._search_recursive(value, node.left)  # recurse left
        else:
            return self._search_recursive(value, node.right)  # recurse right

    def delete(self, value):
        self.root = self._delete_recursive(value, self.root)  # O(log n) avg, O(n) worst

    def _delete_recursive(self, value, node):
        if not node:
            return None  # O(1)
        if value < node.value:
            node.left = self._delete_recursive(value, node.left)  # recurse left
        elif value > node.value:
            node.right = self._delete_recursive(value, node.right)  # recurse right
        else:
            if not node.left:
                return node.right  # O(1) - single child
            elif not node.right:
                return node.left   # O(1) - single child
            else:
                successor = self._find_min(node.right)  # O(log n) avg
                node.value = successor.value  # O(1)
                node.right = self._delete_recursive(successor.value, node.right)  # recurse
        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left  # O(log n) avg - traverse left
        return current