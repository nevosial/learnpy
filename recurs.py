
#Below function will print fibonacci numbers in recursive fashion
# This method is inefficient as takes longer time for producing an outpur for largers inputs.
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

#print(fib(34))

#Using a technique called memoization.
#A memoized function stores in a cache the results corresponding to some set of specific inputs.
#Later calls, with previously computed inputs, return the results stored in the cache, thus avoiding their recalculation.

def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper

fib = memoize(fib)

#The diferrence in execution time is noticeable.
print(fib(34))
