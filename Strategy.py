#Strategy

from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        sorted = False
        for i in range(0, len(data)):
            sorted = False
            for j in range(0, len(data) - i - 1):
                if (data[j] > data[j + 1]):
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
                    sorted = True
            if(sorted == False):
                break
        return data
    

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)
    


input = [1, -2, 0, 4, 8, -5]
bubble_sort_strategy = BubbleSortStrategy()
sorter = Sorter(bubble_sort_strategy)
sorted_data = sorter.sort_data(input)
print(sorted_data)

