""" 
    Se te da un arreglo de enteros deck donde deck[i] representa el número escrito en la i-ésima carta.

    El objetivo es dividir las cartas en uno o más grupos de modo que:

    Cada grupo tenga exactamente x cartas, donde x > 1.
    Todas las cartas de un grupo tengan el mismo número escrito.
    Devuelve true si tal partición es posible, o false en caso contrario.

    Ejemplo 1:
    Entrada:
    deck = [1,2,3,4,4,3,2,1]
    Salida:
    true
    Explicación:
    Es posible formar la partición [1,1], [2,2], [3,3], [4,4].

    Ejemplo 2:
    Entrada:
    deck = [1,1,1,2,2,2,3,3]
    Salida:
    false
    Explicación:
    No es posible formar una partición válida.

    Restricciones:
    1 <= deck.length <= 10^4
    0 <= deck[i] < 10^4
    Notas:
    Para resolver este problema, la clave es encontrar el Máximo Común Divisor (GCD) de las frecuencias de los números
     en deck. Si el GCD es mayor que 1, entonces es posible hacer una partición válida.
"""