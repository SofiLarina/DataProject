"""
Из набора данных Titanic.csv выведите:
количество пассажиров,
средний возраст пассажира,
среднюю стоимость билета,
максимальную и минимальную цену билета,
пассажира с максимальной ценой билета,
средний возраст мужчин и женщин по отдельности,
средний процент выживаемости мужчин и женщин,
среднюю стоимость билета в зависимости от класса проживания,
количество билетов по классам проживания,
количество выживших пассажиров
"""

def eratosthenes(n):
    numbers = list(range(2, n + 1))
    p = 2
    while p <= n:
        for i in range(2 * p, n + 1, p):
            if i in numbers:
                numbers.remove(i)
        for j in numbers:
            if j > p:
                p = j
                break
    return numbers

print(eratosthenes(100))