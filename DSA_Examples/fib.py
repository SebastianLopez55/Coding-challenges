def fib(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


test = 8
testResult = 21
print(fib(test) == testResult)

