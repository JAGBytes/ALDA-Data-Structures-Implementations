import sys
import time
import tracemalloc
from data import constants, data_generator
from data_structures.Stack import Stack
from data_structures.Queue import Queue
from data_structures.BinarySearchTree import AVLTree as BinarySearchTree 
import gc


def measure_performance(min_size, max_size, step, samples):
    """Mide operaciones para Stack, Queue y Binary Tree."""
    results = []
    for size in range(min_size, max_size + 1, step):
        print(f"Testing size: {size}")
        
        # Generar datos específicos para cada estructura
        stack_queue_data = [data_generator.get_sequential_list(size) for _ in range(samples)]
        tree_data = [data_generator.get_random_list(size, shuffle=True) for _ in range(samples)]
        
        # Generar targets usando las listas reales
        stack_queue_targets = [data_generator.get_random_x(size, data_list=data) for data in stack_queue_data]
        tree_targets = [data_generator.get_random_x(size, data_list=data) for data in tree_data]
        
        # Medir estructuras
        stack_results = measure_structure(Stack, stack_queue_data, stack_queue_targets)
        queue_results = measure_structure(Queue, stack_queue_data, stack_queue_targets)
        tree_results = measure_structure(BinarySearchTree, tree_data, tree_targets)
        
        results.append([
            size,
            *stack_results,  # (insert_t, delete_t, search_t, insert_m, delete_m, search_m)
            *queue_results,
            *tree_results
        ])
    return results

def measure_structure(structure_class, data_samples, targets):
    insert_times, insert_mems = [], []
    delete_times, delete_mems = [], []
    search_times, search_mems = [], []
    
    for data, target in zip(data_samples, targets):
        ds = structure_class()

        if tracemalloc.is_tracing():
            tracemalloc.stop()
        
        gc.collect()
        # ---- Inserción (N elementos) ----
        tracemalloc.start()
        tracemalloc.reset_peak()
        initial_mem = tracemalloc.get_traced_memory()[0]
        start = time.perf_counter()
        for item in data:
            if isinstance(ds, Stack):
                ds.push(item)
            elif isinstance(ds, Queue):
                ds.enqueue(item)
            elif isinstance(ds, BinarySearchTree):
                ds.insert(item)
        insert_time = (time.perf_counter() - start) * 1e6  / len(data)# Tiempo total para N inserciones
        _, peak_mem = tracemalloc.get_traced_memory()
        insert_mems.append(peak_mem - initial_mem)
        tracemalloc.stop()
        
        # ---- Búsqueda (1 elemento) ----
        found = False
        gc.collect() 
        tracemalloc.start()
        tracemalloc.reset_peak()
        initial_mem = tracemalloc.get_traced_memory()[0]
        start = time.perf_counter()

        if isinstance(ds, BinarySearchTree):
            found = ds.search(target)
        elif isinstance(ds, Stack):
            found = ds.search(target)
        elif isinstance(ds, Queue):
            found = ds.search(target)


        search_time = (time.perf_counter() - start) * 1e6
        _, peak_mem = tracemalloc.get_traced_memory()
        search_mems.append(peak_mem - initial_mem)
        tracemalloc.stop()
        
        # ---- Eliminación (1 elemento) ----
        gc.collect()
        tracemalloc.start()
        tracemalloc.reset_peak()
        initial_mem = tracemalloc.get_traced_memory()[0]
        start = time.perf_counter()
        if isinstance(ds, BinarySearchTree) and found:
            ds.delete(target)
        elif isinstance(ds, Stack) and not ds.is_empty():
            ds.pop()
        elif isinstance(ds, Queue) and not ds.is_empty():  # Usa is_empty() en lugar de len()
            ds.dequeue()
        delete_time = (time.perf_counter() - start) * 1e6
        _, peak_mem = tracemalloc.get_traced_memory()
        delete_mems.append(peak_mem - initial_mem)
        tracemalloc.stop()
        
        # Guardar métricas
        insert_times.append(insert_time)
        search_times.append(search_time)
        delete_times.append(delete_time)
    
    # Cálculo de medianas
    def _median(lst):
        sorted_lst = sorted(lst)
        mid = len(sorted_lst) // 2
        return sorted_lst[mid]
    
    return (
        _median(insert_times), 
        _median(delete_times), 
        _median(search_times),
        _median(insert_mems), 
        _median(delete_mems), 
        _median(search_mems)
    )