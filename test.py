import random

from algorithms.binary_search import Algo
from algorithms.selection_sort import SelectionSort

def test_binary_search():
    numbers = [random.randint(1, 10) for _ in range(20)]
    numbers.sort()
    algo = Algo(numbers, 3)
    index = algo.binary_search()
    print(f'{index}')

def test_selection_sort():
    numbers = [random.randint(1, 30) for _ in range(10)]
    print(f'unsorted array {numbers}')
    selection_sort = SelectionSort(numbers)
    sorted_array = selection_sort.sort()
    print(f'sortee array: {sorted_array}')


if __name__ == '__main__':
    test_selection_sort()
