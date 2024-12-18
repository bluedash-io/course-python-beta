""" 
    Dado un arreglo de cadenas words, devuelve la primera cadena palindrómica en el arreglo. Si no existe tal cadena, devuelve una cadena vacía "".

    Una cadena es palindrómica si se lee igual hacia adelante y hacia atrás.

    Ejemplo 1:
    Entrada:
    words = ["abc", "car", "ada", "racecar", "cool"]
    Salida:
    "ada"
    Explicación:
    La primera cadena que es palindrómica es "ada".
    Nota: "racecar" también es palindrómica, pero no es la primera.

    Ejemplo 2:
    Entrada:
    words = ["notapalindrome", "racecar"]
    Salida:
    "racecar"
    Explicación:
    La única cadena palindrómica es "racecar".

    Ejemplo 3:
    Entrada:
    words = ["def", "ghi"]
    Salida:
    ""
    Explicación:
    No hay cadenas palindrómicas, por lo que se devuelve una cadena vacía.

    Restricciones:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] contiene solo letras minúsculas del alfabeto inglés.
"""