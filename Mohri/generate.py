def float_range(start, stop):
    while start < stop:
        yield start
        start += 0.01


def letter_range(start, stop, step=2):
    """Yield a range of lowercase letters."""
    for ord_ in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(ord_)


if __name__ == "__main__":

    for i in float_range(2.3, 3.78):
        print("{:.2f}".format(i))

    print("*" * 40)

    for char in letter_range("c", "y", 2):
        print(char)