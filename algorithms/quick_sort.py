from typing import List
import random
class QuickSort:
    def __int__(self, array: List[list]):
        self.array = array

    def swap(self, a, b):
        temp = a
        a = b
        b = temp

    # To do: fix bug (during the sorting the repeatable elements of the list are deleted)

    def sort(self, array):
        if len(array) < 2:
            return array
        base = array[0]
        lower_subarray = [num for num in array[1:] if num < base]
        higher_subarray = [num for num in array[1:] if num > base]
        return self.sort(lower_subarray) + [base] + self.sort(higher_subarray)


if __name__ == '__main__':
    numbers = [random.randint(1, 20) for _ in range(10)]
    print(f'unsorted array : {numbers}')
    quickie = QuickSort()
    quickie.array = numbers
    array = quickie.sort(quickie.array)
    print(f'sorted array {array}')
