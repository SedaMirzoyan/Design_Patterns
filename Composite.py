#Composite
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name =  name

    @abstractmethod
    def component_size(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name, size):
        super().__init__(name)
        self.size =  size

    def component_size(self):
        return self.size
    

class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.files_list =  []

    def add(self, file):
        self.files_list.append(file)

    def component_size(self):
        total = 0
        for component in self.files_list:
            total += component.component_size()
        return total

    

root = Directory("root")
file1 = File("file1", 15)
file2 = File("file2", 20)
file3 = File("file3", 25)
folder1 = Directory("folder1")

root.add(file1)
root.add(file2)
folder1.add(file3)

root.add(folder1)
print(root.component_size())



