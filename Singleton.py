"""
Singleton design pattern:
Pattern makes sure only one object of a class is created, 
and everyone uses the same instance.
"""

class Singleton:
    """
    Makes sure only one instance is created
    """

    #class variable, for holding one instance
    _instance = None

    def __new__(class_obj_itself):
        """
        Creates new instance or returns an existing one

        Return:
            the single instance of class
        """
        if class_obj_itself._instance is None:
            #if no instance exists cretae and store it
            class_obj_itself._instance = super().__new__(class_obj_itself)
            print("Creating new instance")
        
        #returns instance of the class
        return class_obj_itself._instance
    

    def __init__(self):
        """
        Returned instance is passed for initialization

        Attribute:
            value (int): just to show singleton instance can hold data
        """
        self.value = None
    


#check if 2 objects are the same instance or not
ob1 = Singleton()
ob2 = Singleton()

check = ob1 is ob2
print(check)

if (check == True):
    print("Both are the same instance")
else:
    print("Different instances")



        