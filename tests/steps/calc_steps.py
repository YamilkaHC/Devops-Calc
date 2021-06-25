from behave import *
from behave import given, when, then, step
import api
from fastapi.testclient import TestClient


@given ("que deseo Sumar dos numeros")
def step (context):
    context.app = TestClient(api.app)
@when ("yo ingrese los numeros {num1} y {num2}")
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/sumar?num1={num1}&num2={num2}')
    assert 200 == context.api_response.status_code

@then ("El resultado {result} debe ser la suma de ambos")
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))
