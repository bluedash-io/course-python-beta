""" 
    Dadas dos listas de cadenas words1 y words2, devuelve el número de cadenas que aparecen exactamente una vez en cada una de las dos listas.

    Ejemplo 1:
    Entrada:
    words1 = ["leetcode","is","amazing","as","is"]
    words2 = ["amazing","leetcode","is"]
    Salida:
    2
    Explicación:

    "leetcode" aparece exactamente una vez en cada una de las dos listas. Se cuenta esta cadena.
    "amazing" aparece exactamente una vez en cada una de las dos listas. Se cuenta esta cadena.
    "is" aparece en ambas listas, pero hay 2 ocurrencias en words1. No se cuenta esta cadena.
    "as" aparece una vez en words1, pero no aparece en words2. No se cuenta esta cadena.
    Por lo tanto, hay 2 cadenas que cumplen con la condición.
    Ejemplo 2:
    Entrada:
    words1 = ["b","bb","bbb"]
    words2 = ["a","aa","aaa"]
    Salida:
    0
    Explicación:
    No hay cadenas que aparezcan exactamente una vez en ambas listas.

    Ejemplo 3:
    Entrada:
    words1 = ["a","ab"]
    words2 = ["a","a","a","ab"]
    Salida:
    1
    Explicación:
    La única cadena que aparece exactamente una vez en ambas listas es "ab".

    Restricciones:
    1 <= words1.length, words2.length <= 1000
    1 <= words1[i].length, words2[j].length <= 30
    words1[i] y words2[j] consisten en letras minúsculas del alfabeto inglés.
"""