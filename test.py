import random

from algorithms.binary_search import Algo


def main():
    numbers = [random.randint(1, 10) for _ in range(20)]
    numbers.sort()
    algo = Algo(numbers, 3)
    index = algo.binary_search()
    print(f'{index}')


if __name__ == '__main__':
    main()
