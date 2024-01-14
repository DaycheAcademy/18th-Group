def factor(x):
    a = 1
    Answer = 0
    while (a + 1) <= x:
        Answer = a * (a + 1)
        a += 1
    return Answer


if __name__ == '__main__':
    print('factorial:', factor(8))