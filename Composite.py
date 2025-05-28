"""
Composite design pattern:
Treats groups of items (like directory) and individual items (like a file) the same way.
Even if directory is made of files and subdirectories it treats it like one object.
"""
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    """
    Abstract base interface

    Attributes:
        name (string): file/directory name
    """
    def __init__(self, name):
        """
        Initialize component with a name
        
        Args:
            name (string): file/directory name
        """
        self.name =  name

    @abstractmethod
    def component_size(self):
        pass



class File(FileSystemComponent):
    """
    Represents a file

    Attributes:
        size (int): size of the file
    """
    def __init__(self, name, size):
        """
        Initialize file with a name and size

        Args:
            name (string): file name
            size (int): size of the file
        """
        super().__init__(name)
        self.size =  size


    def component_size(self):
        """
        Returns the size of a file

        Return:
            int: File size
        """
        return self.size
    


class Directory(FileSystemComponent):
    """
    Represents a directory, which can contain files and subdirectories

    Attributes:
        files_list (list): list of files and directories
    """
    def __init__(self, name):
        """
        Initialize the directory with a name and empty list

        Args:
            name (string): directory name
        """
        super().__init__(name)
        self.files_list =  []


    def add(self, file_subdir):
        """
        Add file or subdirectory to directory

        Args:
            file_subdir: file or subdirectory to be added
        """
        self.files_list.append(file_subdir)


    def component_size(self):
        """
        calculate the size of the directory.
        including files and subdirectories it has

        Return: 
            total (int): size of all directory components
        """
        total = 0
        for component in self.files_list:
            total += component.component_size()
        return total

    

#create files and directory
root = Directory("root")
file1 = File("file1", 15)
file2 = File("file2", 20)
file3 = File("file3", 25)
folder1 = Directory("folder1")

#add files into directory and print size
root.add(file1)
root.add(file2)
folder1.add(file3)

root.add(folder1)
print(root.component_size())



