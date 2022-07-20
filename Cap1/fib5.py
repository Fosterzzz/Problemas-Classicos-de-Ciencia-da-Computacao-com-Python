def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    print(f'{last} \n{next}')
    for _ in range(1, n):
        last, next = next, last + next
        print(f'{next}')
    return next


if __name__ == "__main__":
    fib5(10)