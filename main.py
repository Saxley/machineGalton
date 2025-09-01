import os # Uso esta biblioteca para obtener el numero de elementos en un directorio
import numpy as np # Uso la biblioteca numpy para generar numeros aleatorios de forma binomial.
import matplotlib.pyplot as plt # Uso la biblioteca matplotlib.pyplot para generar el grafico
from collections import Counter # Counter nos servira para contar los numeros repetidos del arreglo adquirido
from typing import Dict # typing nos ayuda a determinar lo que devuelve y lo que recibe una funcion.

def count_files_in_directory(path:str) -> int:
    """
    Cuenta el número de archivos en la carpeta.
    
    Recibe los argumentos:
        path (str): La ruta de la carpeta.

    Retorna:
        int: El número de elementos en la carpeta.
    """
    try:
        # Genera una lista de todos los elementos, dentro de la carpeta especificada.
        elements = os.listdir(path)
        
        # Devuelve la longitud de la lista, que es el número total de elementos.
        return len(elements)
    except FileNotFoundError:
        # Maneja el caso en el que la ruta no existe.
        print(f"Error: La carpeta '{path}' no fue encontrada.")
        return -1  # Retorna -1 para indicar un error



def simulate_galton_machine(num_balls: int, num_levels: int) -> Dict[int, int]:
    """
    Simula la caída de canicas en una máquina de Galton.
    
    Recibe los argumentos:
        num_balls (int): Número total de canicas.
        num_levels (int): Número de niveles de la máquina de Galton.

    Retorna:
        dict: Claves = contenedores, Valores = número de canicas en cada uno.
    """
    # Genera 3000 números, donde cada número es el conteo de veces que una canica 
    # se desvió en los 12 niveles de la maquina de Galton.
    # Cada bola tiene probabilidad 0.5 de desviarse a la derecha en cada nivel
    results = np.random.binomial(num_levels, 0.5, size=num_balls)

    # Contamos los valores repetidos de los 3000 elementos, la funcion ´Counter´ nos devuelve un objeto Counter.
    # Este objeto es muy similar a un diccionario se basa en el numero como key y como value el conteo de dicho numero
    counts = Counter(results)
    # Nos aseguramos de que retornaremos un tipo de dato ´dictionary´ transformando el objeto Counter en un dict
    return dict(counts)


def plot_histogram(data: Dict[int, int], filename: str) -> None:
    """
    Grafica un histograma a partir de los resultados de la simulación.
    Genera un grafico en la carpeta images.
    
    Recibe los argumentos:
        data(Dict[int:int]) : un diccionario con clave valor de tipo enteros
        filename(str) : una cadena de texto que sirve como path para almacenar el histograma
    
    Retorna:
        No retorna nada
    """
    container_indices = sorted(data.keys()) # adquirimos los indices y los ordenamos con la funcion ´sorted´ 
    ball_counts = [data[i] for i in container_indices] # creamos una nueva lista con los valores ordenados conforme a los indices

    plt.figure(figsize=(10, 6)) # Creamos nuestro plano
    ''' 
    Indicamos que en el plano se creara un grafico de barras.
    Le pasamos 2 valores que actuaran como X,Y.
    Asignamos el color a las barras y a los bordes.
    '''
    plt.bar(container_indices, ball_counts, color="orange", edgecolor="green") 

    plt.title("Simulación de la Máquina de Galton") # Asignamos un titulo al gráfico
    plt.xlabel("Contenedores") # Asignamos nombre al eje X
    plt.ylabel("Cantidad de Canicas") # Asignamos nombre al eje Y
    plt.xticks(container_indices) # Indicamos el numero de barras que seran visibles
    plt.grid(axis="y", linestyle="dotted", alpha=0.7) # Dibujamos una cuadricula para que se vea similar a la maquina de Galton

    plt.savefig(filename, dpi=150) # Almacenamos la imagen con una resolucion de 150
    plt.close() # cerramos el plano
    print(f"El histograma ha sido guardado como '{filename}'") # Notificamos la creación y el nombre


if __name__ == "__main__":
    #CONSTANTES
    NUM_BALLS = 3000 # numero de pelotas
    NUM_LEVELS = 12 # numero de niveles
    FOLDER_PATH = './images' # Ruta de almacenamiento

    # VARIABLES
    # Llama a la función que contara los elementos de mi carpeta images
    num_elements = count_files_in_directory(FOLDER_PATH) # numero de archivos en la carpeta
    name_histogram = f"{FOLDER_PATH}/galton_histogram_{num_elements+1}.png" # ruta con el nuevo nombre para el archivo nuevo

    results = simulate_galton_machine(NUM_BALLS, NUM_LEVELS) # Ejecutamos el simulador
    plot_histogram(results, name_histogram) # Creamos el gráfico
