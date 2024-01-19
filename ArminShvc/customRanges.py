# determine how many decimal points we have
def max_decimal_places(*args):
    max_places = 0
    for number in args:
        decimal_str = str(number).split(".")
        if len(decimal_str) == 2:
            max_places = max(max_places, len(decimal_str[1]))
    return max_places


# create float range by 3 parameters: start, stop, step
def float_range(start, stop, step):
    max_point = max_decimal_places(start, stop, step)
    current = start
    for _ in range(int((stop - start) / step) + 1):
        yield "{:.{}f}".format(current, max_point)
        current += float(step)


# create string range for abcd...wxyz by 3 parameters: start, stop, step
def string_range(start, stop, step):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    stop_index = alphabet.find(stop.lower())
    next_char = 'a'
    end_index = True
    current = start.lower()
    while end_index:
        if stop_index >= alphabet.find(next_char):
            yield current
            current_index = alphabet.find(current)
            next_char = alphabet[current_index + int(step)]
            current = next_char
        else:
            # yield stop
            end_index = False


if __name__ == "__main__":

    for flo in float_range(2.345, 3.7844, 0.0001):
        print(flo)

    for char in string_range("c", "x", 2):
        print(char)







