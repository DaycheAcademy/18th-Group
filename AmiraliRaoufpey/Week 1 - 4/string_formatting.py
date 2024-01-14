import math
alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

name = 'Amirali'
age = 31

print('My name is Amirali, I am 31')

print('My name is', name, ', I am', age)

print('=' * 40)
print('My name is %s, I am %s' % (name, age))

# String Formating
print('My name is {}, I am {}'.format(name, age))
print('My name is {1}, I am {0}'.format(age, name))

print(
"""Farvarrdin: {2}
Ordibehesht:{2}
Khordad: {2}
Tir: {2}
Mordad: {2}
Shahrivar: {2}
Mehr: {1}
Aban: {1}
Azar: {1}
Dey: {1}
Bahman: {1}
Esfand: {0}""".format(29, 30, 31))

# =================================
print('=' * 40)
for number in range(16):
    print('{} to the power of 2 is: {}'.format(number, number ** 2))

print('=' * 40)
for number in range(16):
    print('{0:<3} to the power of 2 divided be 3 is: {1:>6.2f}'.format(number, number ** 2 / 3))  # chap chin <, rast chin >, tedad jaygah argham 3 va 6 masalan, arghame ashar ".2f"

# =================================
print('=' * 40)
print(math.pi)

# Casting: Converting one Data Type to Another
print(float('{:.3f}'.format(math.pi)))

# Casting: Implicit, Explicit -> tarjihan be python mohaval nakon, khodesh anjam mide vali ma ghablesh khodemun bokonim

print(f'My name is {name}, I am {age}')
print('hello, my name is Amirali \nI am 31') # \ is escape character
print('hello \\this is fun!')

# =================================

# print('my binary age is {:b}'.format(age)) --> binary
# print('my binary age is {:u}'.format(age)) --> unicode
# print('my binary age is {:r}'.format(age)) --> raw string (no scape character)
