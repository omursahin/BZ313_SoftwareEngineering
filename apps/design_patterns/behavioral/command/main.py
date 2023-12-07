"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

"""Class Dedicated to Command"""


class Command(ABC):
    """constructor method"""

    def __init__(self, receiver):
        self.receiver = receiver

    """process method"""

    def process(self):
        pass


"""Class dedicated to Command Implementation"""


class CommandImplementation(Command):
    """constructor method"""

    def __init__(self, receiver):
        self.receiver = receiver

    """process method"""

    def process(self):
        self.receiver.perform_action()


"""Class dedicated to Receiver"""


class Receiver:
    """perform-action method"""

    def perform_action(self):
        print('Action performed in receiver.')


"""Class dedicated to Invoker"""


class Invoker:
    """command method"""

    def command(self, cmd):
        self.cmd = cmd

    """execute method"""

    def execute(self):
        self.cmd.process()


"""main method"""
if __name__ == "__main__":
    """create Receiver object"""
    receiver = Receiver()
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
