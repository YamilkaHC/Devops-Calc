Feature: Dividir dos numeros

    Scenario Outline: Dividir
    Given que deseo Dividir dos numeros
    When yo ingrese <dividendo> y <divisor> para dividir
    Then El resultado <result> debe ser la division de ambos

    Examples: Division de Numeros
    | dividendo  | divisor  | result |
    | 2          | 2     | 1      |
    | 12         | 3     | 4      |
    | 1000       | 100   | 10     |
    | 10         | 2     | 5      |
    | 15         | 0     | Invalid  |