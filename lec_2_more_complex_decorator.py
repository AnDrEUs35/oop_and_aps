def decorator(func):
    def new_func():
        print('kill him')
    return new_func

@decorator
def decorate_example():
    print('Not kill him')

decorate_example()

print(decorate_example.__class__)
print(decorate_example.__name__)