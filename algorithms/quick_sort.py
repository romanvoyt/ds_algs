from typing import List
class QuickSort:
    def __int__(self, array: List[list]):
        self.array = array

    def swap(self, a, b):
        temp = a
        a = b
        b = temp
        return a, b

    def sort(self) -> List[list]:
        if len(self.array) < 2:
            return self.array

        base_value_id = int(len(self.array)/2)
        if self.array[0] > self.array[base_value_id]:
            self.array[0], self.array[base_value_id] = self.swap(self.array[0], self.array[base_value_id])
