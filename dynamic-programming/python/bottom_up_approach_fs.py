# Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.
# This simple optimization reduces time complexities from exponential to polynomial.

def fib(n):
    if n == 0:
        return 0
    else:
        previousFib = 0
        currentFib = 1
        for i in range(n-1):
            newFib = previousFib + currentFib
            previousFib = currentFib
            currentFib = newFib
        return currentFib

print(fib(10)) # 55 

