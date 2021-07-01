# Calculadora API

## Funcionalidades
    * Suma de 2 numeros
    * Resta de 2 numeros
    * Multiplicacion de 2 numeros
    * Division de 2 numeros

# Requirements 
- Docker
- Python3

# Tests

## Run unittest + coverge
```
coverage run my unittest.py
coverage report -m --fail-under=80 #Falla sino llegamos al 80% de coverage
```

## Run Integration Test
```
behave tests/Integracion
```