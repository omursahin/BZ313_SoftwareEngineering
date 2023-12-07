"""State class: Base State class"""


class State:
    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1

        """check for the last station"""
        if self.pos == len(self.stations):
            self.pos = 0
        print("Visiting... Station is {} {}".format(self.stations[self.pos], self.name))


"""Separate Class for AM state of the radio"""


class AmState(State):
    """constructor for AM state class"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    """method for toggling the state"""

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


"""Separate class for FM state"""


class FmState(State):
    """Constriuctor for FM state"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    """method for toggling the state"""

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


"""Dedicated class Radio"""


class Radio:
    """A radio. It has a scan button, and an AM / FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    """method to toggle the switch"""

    def toggle_amfm(self):
        self.state.toggle_amfm()

    """method to scan """

    def scan(self):
        self.state.scan()


""" main method """
if __name__ == "__main__":

    """ create radio object"""
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    for action in actions:
        action()
