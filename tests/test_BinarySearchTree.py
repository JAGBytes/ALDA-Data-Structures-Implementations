import unittest
import sys
import os
from pathlib import Path

# Asegurar que el módulo se importe correctamente
sys.path.append(str(Path(__file__).parent.parent))
from data_structures.BinarySearchTree import AVLTree, AVLNode

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()
        self.test_values = [50, 30, 70, 20, 40, 60, 80]

    def _insert_test_values(self):
        """Helper para insertar valores de prueba"""
        for val in self.test_values:
            self.avl.insert(val)

    def test_insert_and_search(self):
        """Prueba inserción y búsqueda de elementos"""
        self._insert_test_values()
        
        # Verificar que todos los valores existen
        for val in self.test_values:
            self.assertTrue(self.avl.search(val), f"El valor {val} debería existir")
            
        # Verificar valores que no existen
        self.assertFalse(self.avl.search(100))
        self.assertFalse(self.avl.search(10))

    def test_delete(self):
        """Prueba eliminación de nodos"""
        self._insert_test_values()
        
        # Eliminar hoja
        self.avl.delete(20)
        self.assertFalse(self.avl.search(20))
        self.assertTrue(self._is_avl_balanced(), "El árbol debe estar balanceado después de eliminar")
        
        # Eliminar nodo con un hijo
        self.avl.delete(30)
        self.assertFalse(self.avl.search(30))
        self.assertTrue(self.avl.search(40))  # El hijo debe permanecer
        
        # Eliminar nodo con dos hijos (raíz)
        self.avl.delete(50)
        self.assertFalse(self.avl.search(50))
        self.assertTrue(self.avl.search(60))  # Sucesor in-order
        self.assertTrue(self._is_avl_balanced(), "El árbol debe estar balanceado después de eliminar la raíz")

    def test_avl_properties_after_insertions(self):
        """Verifica el balance AVL después de inserciones"""
        # Secuencia que requiere rotaciones
        test_cases = [
            [10, 20, 30],  # Rotación LL
            [30, 20, 10],  # Rotación RR
            [10, 30, 20],  # Rotación LR
            [30, 10, 20],  # Rotación RL
        ]
        
        for case in test_cases:
            tree = AVLTree()
            for val in case:
                tree.insert(val)
            self.assertTrue(self._is_tree_balanced(tree.root), f"Caso {case} no está balanceado")

    def test_random_operations(self):
        """Prueba con operaciones aleatorias"""
        import random
        random.seed(42)  # Para reproducibilidad
        
        # Insertar 100 valores aleatorios
        for _ in range(100):
            val = random.randint(0, 1000)
            self.avl.insert(val)
            self.assertTrue(self._is_avl_balanced(), f"Desbalance después de insertar {val}")
            
        # Eliminar 50 valores aleatorios
        for _ in range(50):
            val = random.choice(self._get_tree_values(self.avl.root))
            self.avl.delete(val)
            self.assertTrue(self._is_avl_balanced(), f"Desbalance después de eliminar {val}")

    def test_edge_cases(self):
        """Prueba casos extremos"""
        # Árbol vacío
        self.assertIsNone(self.avl.root)
        self.assertFalse(self.avl.search(0))
        
        # Insertar y eliminar único elemento
        self.avl.insert(100)
        self.assertEqual(self.avl.root.value, 100)
        self.avl.delete(100)
        self.assertIsNone(self.avl.root)

    def _is_avl_balanced(self):
        """Helper para verificar el balance AVL"""
        return self._is_tree_balanced(self.avl.root)

    def _is_tree_balanced(self, node):
        """Verifica el invariante AVL recursivamente"""
        if not node:
            return True
            
        balance = self._get_balance(node)
        if abs(balance) > 1:
            return False
            
        return (self._is_tree_balanced(node.left) and 
                self._is_tree_balanced(node.right))

    def _get_balance(self, node):
        """Calcula el balance de un nodo"""
        left_height = self._get_height(node.left) if node.left else 0
        right_height = self._get_height(node.right) if node.right else 0
        return left_height - right_height

    def _get_height(self, node):
        """Obtiene la altura de un nodo"""
        if not node:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_tree_values(self, node):
        """Devuelve todos los valores del árbol en una lista"""
        if not node:
            return []
        return (self._get_tree_values(node.left) + 
                [node.value] + 
                self._get_tree_values(node.right))

if __name__ == '__main__':
    unittest.main(verbosity=2)