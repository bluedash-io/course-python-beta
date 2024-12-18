""" 
    Dada una cadena s y un carácter c que aparece en s, devuelve un arreglo de enteros answer donde answer.length == s.length y answer[i] es la distancia desde el índice i hasta la aparición más cercana del carácter c en s.

    La distancia entre dos índices i y j se calcula como abs(i - j), donde abs es el valor absoluto.

    Ejemplo 1:
    Entrada:
    s = "loveleetcode", c = "e"
    Salida:
    [3,2,1,0,1,0,0,1,2,2,1,0]
    Explicación:
    El carácter 'e' aparece en los índices 3, 5, 6 y 11 (indexado desde 0).

    La aparición más cercana de 'e' para el índice 0 está en el índice 3, por lo que la distancia es abs(0 - 3) = 3.
    Para el índice 1, la distancia más cercana es abs(1 - 3) = 2.
    Para el índice 4, hay un empate entre 'e' en los índices 3 y 5, pero la distancia sigue siendo abs(4 - 3) == abs(4 - 5) = 1.
    Para el índice 8, la aparición más cercana está en el índice 6, por lo que la distancia es abs(8 - 6) = 2.
    Ejemplo 2:
    Entrada:
    s = "aaab", c = "b"
    Salida:
    [3,2,1,0]

    Restricciones:
    1 <= s.length <= 10^4
    c es un único carácter que aparece al menos una vez en s.
    s y c consisten solo en letras minúsculas del alfabeto inglés.
"""