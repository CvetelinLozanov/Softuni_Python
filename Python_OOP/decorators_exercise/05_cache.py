def cache(func):
    def wrapper(*args, **kwargs):
        if not wrapper.log.get(args[0]):
            wrapper.log[args[0]] = func(args[0])
        return wrapper.log[args[0]]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)