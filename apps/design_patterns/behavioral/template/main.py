""" method to get the text of file"""


def get_text():
    return "plain_text"


""" method to get the xml version of file"""


def get_xml():
    return "xml"


""" method to get the pdf version of file"""


def get_pdf():
    return "pdf"


"""method to get the csv version of file"""


def get_csv():
    return "csv"


"""method used to convert the data into text format"""


def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)


"""method used to save the data"""


def saver():
    print("[SAVE]")


"""helper function named as template_function"""


def template_function(getter, converter=False, to_save=False):
    """input data from getter"""
    data = getter()
    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    """saves the data only if user want to save it"""
    if to_save:
        saver()

    print("`{}` was processed".format(data))


"""main method"""
if __name__ == "__main__":
    template_function(get_text, to_save=True)

    template_function(get_pdf, converter=convert_to_text)

    template_function(get_csv, to_save=True)

    template_function(get_xml, to_save=True)
