""" 
    Se te da un rango inclusivo [lower, upper] y un arreglo de enteros nums, ordenado y único, donde todos los elementos están dentro del rango inclusivo.

    Un número x se considera faltante si está en el rango [lower, upper] y no está en nums.

    Devuelve la lista ordenada más corta de rangos que cubre exactamente todos los números faltantes. Es decir:

    Ningún elemento de nums debe incluirse en los rangos devueltos.
    Cada número faltante debe estar cubierto por uno de los rangos.
    Ejemplo 1:
    Entrada:
    nums = [0,1,3,50,75], lower = 0, upper = 99
    Salida:
    [[2,2],[4,49],[51,74],[76,99]]
    Explicación:
    Los rangos faltantes son:

    [2,2]: El número 2 está faltando.
    [4,49]: Los números desde 4 hasta 49 están faltando.
    [51,74]: Los números desde 51 hasta 74 están faltando.
    [76,99]: Los números desde 76 hasta 99 están faltando.
    Ejemplo 2:
    Entrada:
    nums = [-1], lower = -1, upper = -1
    Salida:
    []
    Explicación:
    No hay números faltantes ya que nums cubre todo el rango [lower, upper].

    Restricciones:
    -10^9 <= lower <= upper <= 10^9
    0 <= nums.length <= 100
    lower <= nums[i] <= upper
    Todos los valores en nums son únicos.
"""