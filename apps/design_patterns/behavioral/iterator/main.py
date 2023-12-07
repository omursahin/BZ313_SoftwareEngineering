"""utility function"""


def inBuilt_Iterator1():
    alphabets = [chr(i) for i in range(65, 91)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


"""utility function"""


def inBuilt_Iterator2():
    alphabets = [chr(i) for i in range(97, 123)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


"""main method"""
if __name__ == "__main__":
    """call the inbuiltIterators"""
    inBuilt_Iterator1()
    inBuilt_Iterator2()
