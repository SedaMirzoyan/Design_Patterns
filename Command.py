#Command

from abc import ABC, abstractmethod

class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    
class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command

    def press_button(self):
        if(self.command):
            self.command.execute()



light = Light()
on_command = TurnOnCommand(light)
off_command = TurnOffCommand(light)

remote_control = RemoteControl()
remote_control.set_command(on_command)
remote_control.press_button()
remote_control.set_command(off_command)
remote_control.press_button()
