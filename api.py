from fastapi import FastAPI
from Calc import Calc

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sumar")
def read_sumar(num1: int = 0, num2:int = 0):
    return {
        "resultado": calc.sumar(num1, num2) 
    }
 