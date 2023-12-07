"""Memento class for saving the data"""


class Memento:
    """Constructor function"""

    def __init__(self, file, content):
        """put all your file content here"""

        self.file = file
        self.content = content


"""It's a File Writing Utility"""


class FileWriterUtility:
    """Constructor Function"""

    def __init__(self, file):
        """store the input file data"""
        self.file = file
        self.content = ""

    """Write the data into the file"""

    def write(self, string):
        self.content += string

    """save the data into the Memento"""

    def save(self):
        return Memento(self.file, self.content)

    """UNDO feature provided"""

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


"""CareTaker for FileWriter"""


class FileWriterCaretaker:
    """saves the data"""

    def save(self, writer):
        self.obj = writer.save()

    """undo the content"""

    def undo(self, writer):
        writer.undo(self.obj)


if __name__ == '__main__':
    """create the caretaker object"""
    caretaker = FileWriterCaretaker()

    """create the writer object"""
    writer = FileWriterUtility("GFG.txt")

    """write data into file using writer object"""
    writer.write("First vision of GeeksforGeeks\n")
    print(writer.content + "\n\n")

    """save the file"""
    caretaker.save(writer)

    """again write using the writer """
    writer.write("Second vision of GeeksforGeeks\n")

    print(writer.content + "\n\n")

    """undo the file"""
    caretaker.undo(writer)

    print(writer.content + "\n\n")
