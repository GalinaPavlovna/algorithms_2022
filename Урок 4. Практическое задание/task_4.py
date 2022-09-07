"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from random import randrange
import timeit

array = [randrange(10) for _ in range(100)]


def timer(n):
    def deco(func):
        def wrapper():
            result = 0
            for _ in range(n):
                start = timeit.default_timer()
                ret = func()
                result += timeit.default_timer() - start
            print(f"Время выполнения {result:.5f}")
            return ret

        return wrapper

    return deco


@timer(1000)
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@timer(1000)
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@timer(1000)
def func_3():
    my_dict = {i: array.count(i) for i in set(array)}
    elem = max(my_dict, key=lambda x: my_dict[x])
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {my_dict[elem]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

"""
Получилось ускорить задачу.
Я думаю, что за счет того, что массив превратился во множество, и не надо было вычислять
для одного и того же элемента количество его включений столько раз, сколько он встречается.
Интересно было бы проверить, ускоряет ли работу применение функции max и словаря по-отдельности;
можно было запихнуть результаты в список кортежей, а не словарь и посмотреть, как поменяются результаты.
Но не проверила.
"""