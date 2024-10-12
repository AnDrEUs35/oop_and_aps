def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            f = open(filename, "w")
            f.write(str(result))
            f.close()
            return result
        return wrapped
    return decorator
  
@logger('file_log.txt')
def summator(list_of_num):
    return sum(list_of_num)

summator([1,2,3,4])
