class Algo:
    def __init__(self, array: list, item: int):
        self.array = array
        self.item = item

    def binary_search(self):
        low = 0
        high = len(self.array)

        while low <= high:
            mid = int((low + high)/2)
            guess = self.array[mid]
            if guess == self.item:
                return mid
            if guess > self.item:
                high = mid - 1
            else:
                low = mid + 1
        return None
