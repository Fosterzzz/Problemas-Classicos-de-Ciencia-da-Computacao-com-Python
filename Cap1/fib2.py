def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)



if __name__ == "__main__":
    print(fib5(10))