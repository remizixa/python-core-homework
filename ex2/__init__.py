import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            # put your code here
            count = 1
            sum = 0
            while count <= num:
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print(f'Время выполнения: {end - start}')
                sum += end - start
                count += 1
            print(f'Среднее время выполнения: {sum / num}')
        return wrapper2
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
