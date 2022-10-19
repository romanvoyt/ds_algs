class SelectionSort:
    def __init__(self, array):
        self.array = array

    def find_smallest_id(self):
        smallest = self.array[0]
        smallest_id = 0
        for i in range(1, len(self.array)):
            if smallest > self.array[i]:
                smallest = self.array[i]
                smallest_id = i
        return smallest_id

    def sort(self):
        sorted_array = []
        for i in range(len(self.array)):
            smallest_n = self.find_smallest_id()
            sorted_array.append(self.array.pop(smallest_n))
        return sorted_array

