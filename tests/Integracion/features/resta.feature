Feature: Restar dos numeros

    Scenario Outline: Restar
    Given que deseo Restar dos numeros
    When yo ingrese los numeros <num1> y <num2>
    Then El resultado <result> debe ser la resta de ambos

    Examples: Resta de Numeros
    | num1  | num2  | result |
    | 2     | 2     | 0      |
    | 1     | 12    | -11    |
    | 1000  | 100   | 900    |
    | 0     | 0     | 0      |
    | 10    | 1     | 9      |