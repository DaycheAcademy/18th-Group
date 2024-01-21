
sum = 0
counter = 0

while True:
    inp = input('Enter an Integer: ')
    # print(type(inp))
    # print(inp.isdigit())
    if inp.lower() == 'q' or inp.lower() == 'quit':
        break
    if not inp.isdigit():
        continue
    else:
        sum = sum + int(inp)
        counter = counter + 1
if counter - 0:
    print('The mean is: {}'.format(sum / counter))
if not counter - 0:
    print("There is no number to calculate mean value")

# meanValue = sum / counter
# print(meanValue)
