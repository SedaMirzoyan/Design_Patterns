#Adapter

'''
OldSystem has a method "specific_request", Target and Adapter have "request" method. 
The Adapter adapts OldSystem to work with the Target interface, 
allowing the client to interact with OldSystem through the Adapter using the request method.
'''

class OldSystem:
    def specific_request(slef):
        return "Specific request"
    
class Target:
    def request(slef):
        return "Target request"
    

class Adapter(Target):
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.specific_request()
    

old_system = OldSystem()
adapter = Adapter(old_system)

print(adapter.request())    #prints Specific request