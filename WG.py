"""Первое, что пришло на ум - тернарный оператор
(в С++ имеет очень большую скорость по сравнению с условиями)"""
value = int(input("Enter value: "))
print(value) if (value % 2 == 0) else 1

"""т.к в Python каждый тип это класс, в котором уже реализованы методы как FIFO, поэто я посчитал, 
что правильней всего использовать и реализовать классы таким образом
"""
cls = str()  # методы rjust -добавляет слева элементы,
# r/lstrip - удаление элементов слева/ справа removeprefix/removesuffix
# и конечно в str это срез 

cls1 = list()  # методы: pop insert remove append

cls2 = dict()  # setdefault pop

cls3 = set() # add remove pop


def q_sort(mass: list) -> list:
    """сортировка Хоара, выбрал её - проста реализация, подходит для любых массивов,
    на сколько я знаю - не использует доп память """
    from random import randint as rand

    if len(mass) > 1:
        elem = mass[rand(0, len(mass) - 1)]
        low = [f for f in mass if f < elem]
        sr = [f for f in mass if f == elem]
        hight = [f for f in mass if f > elem]

        mass = q_sort(low) + sr + q_sort(hight)
    return mass
