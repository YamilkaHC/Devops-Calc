from behave import *
import api
from fastapi.testclient import TestClient


@given ("que deseo Sumar dos numeros")
def step_implementation (context):
    context.app = TestClient(api.app)

@when ("yo ingrese los numeros {num1} y {num2}")
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/sumar?num1={num1}&num2={num2}')
    assert 200 == context.api_response.status_code

@then ("El resultado {result} debe ser la suma de ambos") 
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))





@given ("que deseo Restar dos numeros")
def step_implementation (context):
    context.app = TestClient(api.app)

@when ("yo ingrese {num1} y {num2} para restar")
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/restar?num1={num1}&num2={num2}')
    assert 200 == context.api_response.status_code

@then ("El resultado {result} debe ser la resta de ambos") 
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))




@given ("que deseo Dividir dos numeros")
def step_implementation (context):
    context.app = TestClient(api.app)

@when ("yo ingrese {num1} y {num2} para dividir")
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'dividir?num1={num1}&num2={num2}')
    assert 200 == context.api_response.status_code

@then ("El resultado {result} debe ser la division de ambos") 
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))






@given ("que deseo Multiplicar dos numeros")
def step_implementation (context):
    context.app = TestClient(api.app)

@when ("yo ingrese {num1} y {num2} para multiplicar")
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'multiplicar?num1={num1}&num2={num2}')
    assert 200 == context.api_response.status_code

@then ("El resultado {result} debe ser la multiplicacion de ambos") 
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))


 