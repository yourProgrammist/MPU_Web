import time
from datetime import datetime


def function_logger(input_arg):

    def the_real_decorator(function):

        def wrapper(*args, **kwargs):
            file = open(input_arg, 'w')
            print(function.__name__, file=file)
            start = datetime.now()
            print(start.strftime("%Y-%m-%d %H:%M:%S.%f"), file=file)
            if args:
                print(args, file=file)
            if kwargs:
                print(kwargs, file=file)
            res = function(*args, **kwargs)
            if res:
                print(res, file=file)
            else:
                print('-', file=file)

            end = datetime.now()

            print(end.strftime("%Y-%m-%d %H:%M:%S.%f"), file=file)
            print(str(end - start), file=file)
            file.close()
            result = function(*args, **kwargs)
            return f'{input_arg}\n{result}\n{input_arg}'

        return wrapper

    return the_real_decorator

@function_logger("log.txt")
def greeting_format(name):
    return f'Hello, {name}!'

greeting_format('John')
