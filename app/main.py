from fastapi import FastAPI
import math

app = FastAPI()

def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def next_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        a, b = b, a + b
    return a

@app.get("/fibonacci/{number}")
async def check_fibonacci(number: int):
    if is_fibonacci(number):
        return {"next_fibonacci": next_fibonacci(number)}
    else:
        return {"message": "Not a Fibonacci number"}
