"""
Adapter design pattern:
It provides a way for two incompatible interfaces work together.
In the following example they are OldSystem and Target.
"""

class OldSystem:
    """
    Old system interface
    """
    def specific_request(slef):
        """
        Old method

        Return:
            string: response from the old system
        """
        return "Specific request"
    

class Target:
    """
    The new system interface
    """
    def request(slef):
        """
        New method

        Return:
            string: response from the new system
        """
        return "Target request"
    

class Adapter(Target):
    """
    With the help of Adapter OldSystem and Target can work together
    """
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        """
        Translates old request to the new request
        """
        return self.old_system.specific_request()
    


#using Target interface, but gets old system's response
old_system = OldSystem()
adapter = Adapter(old_system)

print(adapter.request())    #prints Specific request