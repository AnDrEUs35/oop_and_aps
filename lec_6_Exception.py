try:
    # Некоторый код, генерирующий исключение
    raise Exception("Описание ошибки")
    
except Exception as e:
    print("Произошла ошибка:", str(e))


class MyError(Exception):
    def __str__(self):
        return 'Натворил делов'

raise MyError()
