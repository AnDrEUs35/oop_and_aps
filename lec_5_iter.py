a = range(3)
# next(a)

print(id(a))
print(type(a))

new_a = iter(a)
print(id(a))
print(type(a))

print(next(new_a))
print(next(new_a))
print(next(new_a))

print(new_a)