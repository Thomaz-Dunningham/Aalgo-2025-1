import time
import random

def quick_sort(arr):
    # Função auxiliar para particionar o array
    def partition(low, high):
        # Escolhe o último elemento como pivô
        pivot = arr[high]

        i = low - 1  # Índice do menor elemento
        for j in range(low, high):
            # Se o elemento atual é menor ou igual ao pivô
            if arr[j] <= pivot:
                i += 1  # Incrementa o índice do menor elemento
                arr[i], arr[j] = arr[j], arr[i]  # Troca os elementos
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Coloca o pivô na posição correta
        return i + 1

    # Função principal do Quick Sort
    def quick_sort_recursive(low, high):
        if low < high:
            # Particiona o array e obtém o índice do pivô
            pivot_index = partition(low, high)
            # Ordena os elementos antes e depois da partição
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    # Chama a função recursiva com os índices iniciais
    quick_sort_recursive(0, len(arr) - 1)

# Exemplo de uso
if __name__ == "__main__":
    # Dicionário com arrays de diferentes tamanhos
    arrays = {
        "100 elementos": [random.randint(1, 1000) for _ in range(100)],
        "1000 elementos": [random.randint(1, 1000) for _ in range(1000)],
        "10000 elementos": [random.randint(1, 1000) for _ in range(10000)],
        "100000 elementos": [random.randint(1, 1000) for _ in range(100000)]
    }
    
    # Calcula o tempo de execução do Quick Sort para cada um dos arrays
    for description, array in arrays.items():
        start_time = time.time()
        quick_sort(array)
        end_time = time.time()
        print(f"Tempo de execução com {description}: {end_time - start_time} segundos\n")