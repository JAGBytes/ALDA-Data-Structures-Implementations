import random
from data import constants

# data_generator.py
def get_random_list(size, limit=constants.MAX_VALUE, shuffle=True):
    """Genera una lista aleatoria, opcionalmente desordenada."""
    random_list = [random.randint(0, limit) for _ in range(size)]
    if shuffle:
        random.shuffle(random_list)  # Solo para el árbol
    return random_list

def get_sequential_list(size):
    """Genera una lista ordenada (para pila/cola)."""
    return list(range(size))

def get_random_x(size, data_list=None, limit=constants.MAX_VALUE):
    return random.choice(data_list)