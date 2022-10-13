from datetime import datetime
import os

def logging(function):
    def results(*args, **kwargs):
        result = function(*args, **kwargs)
        info = f'{datetime.now()};\nИмя функции: {function.name};\nАргументы: {args}, {kwargs};\nРезультат: {result}\n\n\n'
        with open('log.txt', 'a', encoding='utf-8') as text:
            text.write(info)
    print(f'Функция {function.name} закомментировака.')
    return results

def parammed_logging(direct):

    def local_logging(function):
        def results(*args, **kwargs):
            result = function(*args, **kwargs)
            info = f'{datetime.now()};\nИмя функции: {function.name};\nАргументы: {args}, {kwargs};\nРезультат: {result}\n\n\n'
            with open(direct, 'w', encoding='utf-8') as text:
                text.write(info)

        print(f'Функция {function.name} закомментировака.')
        return results
    return local_logging