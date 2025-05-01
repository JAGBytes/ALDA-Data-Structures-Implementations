import unittest
import sys
from pathlib import Path

# Añadir el directorio padre al path para importar Queue
sys.path.append(str(Path(__file__).parent.parent))
from data_structures.Queue import Queue, Node

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_dequeue(self):
        """Prueba básica de encolado y desencolado"""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertIsNone(self.queue.dequeue())  # Cola vacía

    def test_search(self):
        """Prueba de búsqueda de elementos"""
        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.assertTrue(self.queue.search("A"))
        self.assertFalse(self.queue.search("C"))

    def test_length_and_is_empty(self):
        """Prueba de longitud y estado vacío"""
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(1)
        self.assertEqual(len(self.queue), 1)
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_peek(self):
        """Prueba de peek (ver sin desencolar)"""
        self.queue.enqueue(99)
        self.assertEqual(self.queue.peek(), 99)
        self.assertEqual(len(self.queue), 1)  # Peek no modifica la cola

    def test_items_property(self):
        """Prueba de la propiedad items"""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.items, [1, 2])

if __name__ == "__main__":
    unittest.main(verbosity=2)