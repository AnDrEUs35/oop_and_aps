def sum_arg(a, b):
    return a + b

print(sum_arg(12, 25))


sum_arg = lambda a, b: a + b  # Анонимная функция

print(sum_arg(7, 13))





a = [lambda a: a**2 for a in range(10)]
print(a)




list_1 = [1, 3, 4]
list_2 = [0, 1, 2]

a = list(map(lambda a, b: a+b, list_1, list_2))
print(a)


maximum = (lambda a, b: a if a > b else b)
print(maximum(23 , 25))






lambda_list = [lambda х: х + 1, lambda х: х * 2, lambda х: х ** 3]
for i in lambda_list:
	print(i(2)) #выполняются все lamda-функции

print(lambda_list[0](4)) #выполняется конкретная lamda-функция
