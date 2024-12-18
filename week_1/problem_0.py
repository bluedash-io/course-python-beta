'''
    Dado un array de cadenas llamado wordsDict y dos cadenas diferentes word1 y word2 que ya existen en el array, devuelve la distancia más corta entre estas dos palabras en la lista.

    Ejemplo 1:
    Entrada:
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
    Salida:
    3

    Ejemplo 2:
    Entrada:
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
    Salida:
    1

    Restricciones:
    2 <= wordsDict.length <= 3 * 10^4
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consiste en letras minúsculas en inglés.
    word1 y word2 están en wordsDict.
    word1 ≠ word2.
'''

# Solution (best)
def shortestDistance(words, word1, word2):
    
