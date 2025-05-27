#Singleton

class Singleton:
    _instance = None

    def __new__(class_obj_itself):
        if class_obj_itself._instance is None:
            class_obj_itself._instance = super().__new__(class_obj_itself)
            print("Creating new instance")

        return class_obj_itself._instance
    

ob1 = Singleton()
ob2 = Singleton()

check = ob1 is ob2
print(check)

if (check == True):
    print("Both are the same instance")
else:
    print("Different instances")



        