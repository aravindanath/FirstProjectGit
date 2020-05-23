def fib(n):
    a, b = 0, 1
    for i in range(n):
        # if a function contains 'yield'statement, then it becomes Generator
        yield a
        a, b = b, a + b


a = int(input('Enter the amount of Fibonacci numbers to be printed: '))
print(list(fib(a)))