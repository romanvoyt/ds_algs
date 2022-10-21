import random

from algorithms.binary_search import BinarySearch
from algorithms.selection_sort import SelectionSort
from algorithms.quick_sort import QuickSort


def test_binary_search():
    numbers = [random.randint(1, 10) for _ in range(20)]
    numbers.sort()
    algo = BinarySearch(numbers, 3)
    index = algo.search()
    print(f'{index}')


def test_selection_sort():
    numbers = [random.randint(1, 30) for _ in range(10)]
    print(f'unsorted array {numbers}')
    selection_sort = SelectionSort(numbers)
    sorted_array = selection_sort.sort()
    print(f'sortee array: {sorted_array}')

# The sorting is deleting duplicates, to fix
def test_quick_sort():
    numbers = [random.randint(1, 33) for _ in range(100)]
    print(f'unsorted array {numbers}')
    quickie = QuickSort()
    quickie.array = numbers
    sorted_array = quickie.sort(quickie.array)
    print(f'sorted array: {sorted_array}')


if __name__ == '__main__':
    test_quick_sort()
