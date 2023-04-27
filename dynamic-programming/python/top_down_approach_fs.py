# Create a dict to store the values of the fib sequence
map = {
    0: 0,
    1: 1
}
# This technique of saving values that have already been calculated is called memoization;
# this is the top-down approach, since we first break the problem into subproblems and then calculate and store values
def fib(n):
    if not n in map:
        map[n] = fib(n-1) + fib(n-2)
    return map[n]

print(fib(10)) # 55