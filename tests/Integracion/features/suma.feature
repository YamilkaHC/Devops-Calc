Feature: Sumar dos numeros

    Scenario Outline: Sumar
    Given que deseo Sumar dos numeros
    When yo ingrese los numeros <num1> y <num2>
    Then El resultado <result> debe ser la suma de ambos

    Examples: Suma de Numeros
    | num1  | num2  | result |
    | 2     | 2     | 4      |
    | 1     | 12    | 13     |
    | 100   | 1000  | 1100   |
    | 0     | 0     | 0      |
    | 1     | -1    | Invalid|