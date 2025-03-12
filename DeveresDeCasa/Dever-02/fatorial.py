import time

# Complexidade linear O(n) pois o laço 'while' executa n - 1 iterações (onde n é o valor inicial passado como argumento da função).
def fatorial(n: int) -> int:
    # Inicializamos a variável 'fatorial' com o valor 1
    fatorial = 1
    
    # Em cada iteração, o valor de 'fatorial' será multiplicado por 'n' e depois n será decrementado.
    while n > 1:
        fatorial *= n
        n -= 1
    
    # Após o loop terminar, 'fatorial' terá o valor do fatorial de n.
    return fatorial


# Exemplo de uso
if __name__ == "__main__":
    # Dicionário com arrays de diferentes valores para n
    dict = {
        "n = 10": 10,
        "n = 100": 100,
        "n = 500": 500,
        "n = 1000": 1000
    }
    
    # Calcula o tempo de execução do fatorial para cada um dos arrays
    for description, n in dict.items():
        start_time = time.time()
        fatorial(n)
        end_time = time.time()
        print(f"Tempo de execução com {description}: {end_time - start_time} segundos\n")