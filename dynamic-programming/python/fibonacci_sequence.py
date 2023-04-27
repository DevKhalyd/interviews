# Important:  In larger examples, many more values of fib, or subproblems, are recalculated, leading to an exponential time algorithm.
def fib(n):
    """Print a Fibonacci number closest to n."""
    # Always return 0 or 1 and then makes the sum of all the previous numbers
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

n = fib(5)

print(f"Finobacci number: {n}")


# output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 


# def fib(n):
#    """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# fib(2000)