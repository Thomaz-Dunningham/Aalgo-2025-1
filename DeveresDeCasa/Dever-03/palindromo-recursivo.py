# Definição da função recursiva de palíndromo
def is_palindrome(array, i, j):
    if array[i] != array[j]:
        return False
    if i >= j:
        return True
    return is_palindrome(array, i + 1, j - 1)

# Exemplo de uso
if __name__ == "__main__":
    # Dicionário com arrays de exemplo
    arrays = {
        "array1": [0, 1, 2, 3, 2, 1, 0],
        "array2": ["a", "b", "b", "a"],
        "array3": ["a", "b", "c", "b", "a"],
        "array4": ["a", "b", "c", "f", "b", "a"]
    }

    # Imprime o resultado da função is_palindrome para cada um dos arrays
    for nome, array in arrays.items():
        resultado = is_palindrome(array, 0, len(array) - 1)
        print(f"{nome}: {resultado}\n")