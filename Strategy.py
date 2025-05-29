"""
Strategy Design pattern:
It lets you change how something is done without changing the thing that does it.
If we want to sort a list, instead of hardcoding bubble sort, quick sort,
we can choose the sorting method at runtime.
"""

from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    """
    Abstract base class with sorting strategies
    """
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortingStrategy):
    """
    Strategy for sorting using bubble sort algorithm
    """
    def sort(self, data):
        """
        Sorts the list using bubble sort

        Args:
            data (list): list to sort

        Return:
            list:
                The sorted list using bubble sort
        """
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
    """
    Class which uses sorting strategy

    Attributes:
        strategy (BubbleSortStrategy instance): The sorting strategy
    """
    def __init__(self, strategy):
        """
        Initialize with a sorting strategy

        Args:
            strategy (BubbleSortStrategy instance): New sorting strategy
        """
        self.strategy = strategy


    def sort_data(self, data):
        """
        Sort the data using the current strategy

        Args:
            data (list): list to sort

        Return:
            list: Sorted list
        """
        return self.strategy.sort(data)
    


#original unsorted list
input = [1, -2, 0, 4, 8, -5]

#create sorter with Bubble sort strategy
bubble_sort_strategy = BubbleSortStrategy()
sorter = Sorter(bubble_sort_strategy)

#sort data using the current strategy (Bubble sort)
sorted_data = sorter.sort_data(input)
print(sorted_data)

