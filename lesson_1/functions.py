def greet(name=None):
    if name is None:
        name = input()
    print("Hello " + name + ", how are you doing today?")

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5))
