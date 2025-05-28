"""
Command design pattern:
It treat actions like an objects for controling when and how they run.
"""

from abc import ABC, abstractmethod

class Light:
    """
    Receiver, Light that can be turned on or off,
    with corresponding methods
    """
    def turn_on(self):
        print("Light is on")


    def turn_off(self):
        print("Light is off")


class Command(ABC):
    """
    Abstract base class for commands.
    """
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    """
    Implement command for turn the light on.

    Attributes:
        light: Light (Receiver) object   
    """
    def __init__(self, light):
        """
        Initialize with the receiver (light)

        Args: 
            light: Light (Receiver) object     
        """
        self.light = light


    def execute(self):
        "execute the command to turn on the light"
        self.light.turn_on()

    

class TurnOffCommand(Command):
    """
    Implement command for turn the light off.

    Attributes:
        light: Light (Receiver) object   
    """
    def __init__(self, light):
        """
        Initialize with the receiver (light)

        Args: 
            light: Light (Receiver) object     
        """
        self.light = light


    def execute(self):
        "execute the command to turn off the light"
        self.light.turn_off()



class RemoteControl:
    """
    Class that calls the command

    Attribute:
        command (Command object): command object
    """
    def __init__(self):
        """
        Initialize command to None
        """
        self.command = None
    

    def set_command(self, command):
        """
        Initialize remote control to a command

        Args:
            command (Command object): command object
        """
        self.command = command


    def press_button(self):
        """
        Calls command execute method
        """
        if(self.command):
            self.command.execute()




#create the receiver object
light = Light()

#create command objects with the receiver
on_command = TurnOnCommand(light)
off_command = TurnOffCommand(light)

#create remote control object and exceute commands
remote_control = RemoteControl()
remote_control.set_command(on_command)
remote_control.press_button()
remote_control.set_command(off_command)
remote_control.press_button()