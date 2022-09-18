"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""
from memory_profiler import memory_usage


# Исходный  код
def memoriser(func, *args):
    def wrapper(*args):
        start = memory_usage()[0]
        res = func(*args)
        mem = memory_usage()[0] - start
        print("memoriser -", mem)
        return res

    return wrapper


@memoriser
def recursion_wrapper(func, *args):
    a = func(*args)
    return a


def rate_summ(n, q, b):
    return b + rate_summ(n - 1, q, b * q) if n != 1 else b


# Оптимизированный код
def generator(q, b):
    summ = 0
    while True:
        summ += b
        yield summ
        b *= q


@memoriser
def summator(n, q, b):
    counter = 1
    for i in generator(q, b):
        if counter == n:
            return i
        else:
            counter += 1


print("Рекурсия")
print(recursion_wrapper(rate_summ, 500, 2, 3))
print("Yield")
print(summator(500, 2, 3))

"""
Рекурсия заменена на yield, что ожидаемо уменьшило расход памяти.
Сложно было придумать-таки вариант использования yield - на мой взгляд, память-то экономит, но код усложняет.
"""
