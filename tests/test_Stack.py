import unittest
import sys
from pathlib import Path

# Añadir el directorio padre al path para importar Stack
sys.path.append(str(Path(__file__).parent.parent))
from data_structures.Stack import Stack, Node

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_pop(self):
        """Prueba push y pop básicos"""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        self.assertIsNone(self.stack.pop())  # Stack vacío

    def test_peek(self):
        """Prueba peek sin modificar el stack"""
        self.stack.push("A")
        self.stack.push("B")
        self.assertEqual(self.stack.peek(), "B")
        self.assertEqual(len(self.stack), 2)  # No modifica el tamaño

    def test_length(self):
        """Prueba de conteo de elementos"""
        self.assertEqual(len(self.stack), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 2)
        self.stack.pop()
        self.assertEqual(len(self.stack), 1)

    def test_is_empty(self):
        """Prueba de verificación de stack vacío"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(3.14)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_search(self):
        """Prueba de búsqueda de elementos"""
        self.stack.push(100)
        self.stack.push(200)
        self.assertTrue(self.stack.search(100))
        self.assertFalse(self.stack.search(300))

    def test_items_property(self):
        """Prueba de la propiedad items (orden LIFO)"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.items, [3, 2, 1])  # Orden inverso

    def test_edge_cases(self):
        """Prueba casos límite"""
        # Pop en stack vacío
        self.assertIsNone(self.stack.pop())
        
        # Peek en stack vacío
        self.assertIsNone(self.stack.peek())
        
        # Search en stack vacío
        self.assertFalse(self.stack.search(99))

    def test_large_stack(self):
        """Prueba con muchos elementos"""
        test_size = 1000
        for i in range(test_size):
            self.stack.push(i)
        
        self.assertEqual(len(self.stack), test_size)
        
        # Verificar orden LIFO
        for i in range(test_size-1, -1, -1):
            self.assertEqual(self.stack.pop(), i)
        
        self.assertTrue(self.stack.is_empty())

    def test_memory_management(self):
        """Prueba de liberación de memoria (opcional)"""
        import weakref
        
        # Crear nodo débilmente referenciado
        self.stack.push("test")
        node_ref = weakref.ref(self.stack.top)
        
        # Eliminar el nodo
        self.stack.pop()
        
        # Verificar que el nodo fue liberado
        self.assertIsNone(node_ref())

if __name__ == "__main__":
    unittest.main(verbosity=2)