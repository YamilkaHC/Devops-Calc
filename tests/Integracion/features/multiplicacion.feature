Feature: Multiplicar dos numeros

    Scenario Outline: Multiplicar
    Given que deseo Multiplicar dos numeros
    When yo ingrese <num1> y <num2> para multiplicar
    Then El resultado <result> debe ser la multiplicacion de ambos

    Examples: Multiplicar de Numeros
    | num1  | num2  | result |
    | 2     | 2     | 4      |
    | 1     | 12    | 12     |
    | 1000  | 1     | 1000   |
    | 0     | 1     | 0      |
    | 10    | 5     | 50     |