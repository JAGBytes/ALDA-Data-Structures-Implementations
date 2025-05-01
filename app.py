import matplotlib.pyplot as plt
from data import execution_time_gathering as etg


def print_results(table):
    """Imprime resultados en formato tabla."""
    print("\nSize | Stack (Insert, Delete, Search) | Queue (Insert, Delete, Search) | Tree (Insert, Delete, Search)")
    print("-" * 120)
    for row in table:
        size = row[0]
        # Stack: insert_t, delete_t, search_t, insert_m, delete_m, search_m
        # Queue: ... (same)
        # Tree: ... (same)
        stack_metrics = f"T:({row[1]:.2f}, {row[2]:.2f}, {row[3]:.2f}) M:({row[4]}, {row[5]}, {row[6]})"
        queue_metrics = f"T:({row[7]:.2f}, {row[8]:.2f}, {row[9]:.2f}) M:({row[10]}, {row[11]}, {row[12]})"
        tree_metrics = f"T:({row[13]:.2f}, {row[14]:.2f}, {row[15]:.2f}) M:({row[16]}, {row[17]}, {row[18]})"
        print(f"{size:5} | {stack_metrics:40} | {queue_metrics:40} | {tree_metrics:40}")

def plot_comparison(table):
    """Genera gráficos comparativos en dos ventanas: tiempo y memoria."""
    sizes = [row[0] for row in table]
    
    # Extraer series de tiempo
    insert_time_stack = [row[1] for row in table]
    delete_time_stack = [row[2] for row in table]
    search_time_stack = [row[3] for row in table]
    
    insert_time_queue = [row[7] for row in table]
    delete_time_queue = [row[8] for row in table]
    search_time_queue = [row[9] for row in table]
    
    insert_time_tree = [row[13] for row in table]
    delete_time_tree = [row[14] for row in table]
    search_time_tree = [row[15] for row in table]
    
    # Extraer series de memoria
    insert_mem_stack = [row[4] for row in table]
    delete_mem_stack = [row[5] for row in table]
    search_mem_stack = [row[6] for row in table]
    
    insert_mem_queue = [row[10] for row in table]
    delete_mem_queue = [row[11] for row in table]
    search_mem_queue = [row[12] for row in table]
    
    insert_mem_tree = [row[16] for row in table]
    delete_mem_tree = [row[17] for row in table]
    search_mem_tree = [row[18] for row in table]
    
    # Ventana 1: Tiempo
    fig_time, axes_time = plt.subplots(3, 1, figsize=(10, 12))
    fig_time.suptitle("Comparación de Tiempos (µs)", fontsize=14)
    
    # Inserción (Tiempo)
    ax = axes_time[0]
    ax.plot(sizes, insert_time_stack, 'bo-', label='Stack')  # Color, marcador, línea
    ax.plot(sizes, insert_time_queue, 'rs--', label='Queue')
    ax.plot(sizes, insert_time_tree, 'g^-.', label='Tree')
    ax.set_title('Inserción')
    ax.set_ylabel('Tiempo (µs)')
    ax.legend()
    ax.grid(True)
    
    # Búsqueda (Tiempo)
    ax = axes_time[1]
    ax.plot(sizes, search_time_stack, 'bo-', label='Stack')
    ax.plot(sizes, search_time_queue, 'rs--', label='Queue')
    ax.plot(sizes, search_time_tree, 'g^-.', label='Tree')
    ax.set_title('Búsqueda')
    ax.set_ylabel('Tiempo (µs)')
    ax.legend()
    ax.grid(True)
    
    # Eliminación (Tiempo)
    ax = axes_time[2]
    ax.plot(sizes, delete_time_stack, 'bo-', label='Stack')
    ax.plot(sizes, delete_time_queue, 'rs--', label='Queue')
    ax.plot(sizes, delete_time_tree, 'g^-.', label='Tree')
    ax.set_title('Eliminación')
    ax.set_xlabel('Tamaño (N)')
    ax.set_ylabel('Tiempo (µs)')
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    
    # Ventana 2: Memoria
    fig_mem, axes_mem = plt.subplots(3, 1, figsize=(10, 12))
    fig_mem.suptitle("Comparación de Memoria (bytes)", fontsize=14)
    
    # Inserción (Memoria)
    ax = axes_mem[0]
    ax.plot(sizes, insert_mem_stack, 'bo-', label='Stack')
    ax.plot(sizes, insert_mem_queue, 'rs--', label='Queue')
    ax.plot(sizes, insert_mem_tree, 'g^-.', label='Tree')
    ax.set_title('Inserción')
    ax.set_ylabel('Memoria (bytes)')
    ax.legend()
    ax.grid(True)
    
    # Búsqueda (Memoria)
    ax = axes_mem[1]
    ax.plot(sizes, search_mem_stack, 'bo-', label='Stack')
    ax.plot(sizes, search_mem_queue, 'rs--', label='Queue')
    ax.plot(sizes, search_mem_tree, 'g^-.', label='Tree')
    ax.set_title('Búsqueda')
    ax.set_ylabel('Memoria (bytes)')
    ax.legend()
    ax.grid(True)
    
    # Eliminación (Memoria)
    ax = axes_mem[2]
    ax.plot(sizes, delete_mem_stack, 'bo-', label='Stack')
    ax.plot(sizes, delete_mem_queue, 'rs--', label='Queue')
    ax.plot(sizes, delete_mem_tree, 'g^-.', label='Tree')
    ax.set_title('Eliminación')
    ax.set_xlabel('Tamaño (N)')
    ax.set_ylabel('Memoria (bytes)')
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Configuración
    config = {
        "min_size": 1_000,      # Tamaño inicial relevante para observar patrones
        "max_size": 50_000,     # Tamaño máximo ampliado para validar escalabilidad
        "step": 1_000,          # Granularidad balanceada entre detalle y eficiencia
        "samples": 15           # Más muestras para reducir variabilidad estadística
    }
    
    # Ejecutar mediciones
    results = etg.measure_performance(**config)
    
    # Mostrar resultados
    print_results(results)
    plot_comparison(results)