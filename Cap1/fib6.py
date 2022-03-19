from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0 # Caso especial
    if n > 0: yield 1 #Caso Especial
    num1: int = 0
    num2: int = 1
    for i in range(1, n):
        num1, num2 = num2, num1 + num2
        yield num2 #passo principal da geração


if __name__ == "__main__":
    for j in fib6(50):
        print(j)