# Calculadora API

La aplicacion consiste en una calculadora que realiza las operaciones de suma, resta, multiplicación y division de dos numeros en Python haciendo uso de una api y con sus respectivos unit test. 

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

##  Run App

```
uvicorn --host 0.0.0.0 --port 8000 api:app
```
  




# Urls de los repositorios de los ejercicios que hemos realizado hasta ahora

### Practica: hello word
https://github.com/YamilkaHC/HelloWordPractice

### Practica: Docker ejercicio #6
https://github.com/YamilkaHC/HelloWordPractice/tree/PracticeDocker-Exercise%236

### Practica: Docker ejercicio #7
https://github.com/YamilkaHC/HelloWordPractice/tree/PracticeDocker-Exercise%237

### Practica: DockerWordpress
https://github.com/YamilkaHC/HelloWordPractice/tree/PracticeDocker-Wordpress