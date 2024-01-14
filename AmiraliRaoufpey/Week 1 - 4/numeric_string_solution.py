numericString = '34,0.86457,-23,0,876587,2,8'

# 1- bedune abzar haye python:

if numericString[-1] != ',':
    numericString += ','

number = ''
sumOfNumbers = 0
for char in numericString:
    if char in '0123456789.-':
        number += char
    else:
        sumOfNumbers += float(number)
        number = ''
# sumOfNumbers += float(number) -> agar dar enteha ',' ezafe nemikardim in rah javab dorost midad
print(sumOfNumbers)

print('=' * 40)
# ======================================
numericString = '34,0.86457,-23,0,876587,2,8'

# 2- be vasileye method ha, mikhahim beshkunim az comma ha

mySum = 0
numericList = numericString.split(',')
print(numericList)
for num in numericList:
    mySum += float(num)
print(mySum)

print('=' * 40)
# ======================================

# 3- ravaeshe pythonic (list comprehension)

print(sum([float(num) for num in numericString.split(',')]))