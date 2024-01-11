# List is a sequence

# Sequence:
# 1 - Ordered
# 2 - Index-able

import copy

emptyList = []  # literal
anotherEmptyList = list()  # constructor (iterable behesh pass midahim)

sampleList = [1, 3.6, 'A', 9]
sampleList2 = [1, 3.6, 4, 9, 2, 4.907]

sampleList.append(4.907)
print(sampleList)

sampleString = 'ABCD'
alphabetList = list(sampleString)  # be constructor tanha iterable mitavan pass dad
print(alphabetList)

print('=' * 40)
# ======================================

# sampleList.sort()  --> khata midahad chera ke data type str darim, tarjihan type hame aza list bayad yeki bashad

# ======================================

print(sampleList2.sort())  # why None?
# 1- all variables in python have pointer behaviour
# 2- list is mutable object (mutable = when changed they will change in current location and their id won't change)

print(sampleList2)

print('=' * 40)
# ======================================
# 1:
# a = 5 , a -> variable(object), 5 -> value(id - identity)
# the word in memory block which 'a' is stored, is filled with address of another word in block which '5' is there
# this is pointer concept - "a" points to the address (id) where value is stored

a = 5
print(hex(id(a)))
b = 5
print(hex(id(b)))  # python tries to assign same id while we have same value

print('=' * 40)
# ======================================
# 2:
# list is mutable, so when we use any method on it, the result is in the same id and there is no "output" value
# having no output is the reason we saw "None"

a = a + 1
print(a, b)
print(hex(id(a)))  # numerics are immutable, when changed the address will change

print('=' * 40)
# ======================================

odd = list(range(1, 20, 2))
# print(odd)

backUp = odd
odd.append(101)
print(backUp)  # mibinim meghdar 101 ra darad, chon mutable hast va har do be yek ja eshare mikonad

print('=' * 40)
# ======================================

print(odd.index(11))

print('=' * 40)
# ======================================

odd = list(range(1, 20, 2))
backUp = odd.copy()
odd.append(101)
print(backUp)
print(odd)
print(hex(id(backUp)))
print(hex(id(odd)))

print('=' * 40)
# ======================================

odd = list(range(1, 20, 2))
backUp = list(odd)
odd.append(101)
print(backUp)
print(hex(id(backUp)))
print(hex(id(odd)))

print('=' * 40)
# ======================================

odd = list(range(1, 20, 2))
backUp = copy.copy(odd)
odd.append(101)
print(backUp)
print(hex(id(backUp)))
print(hex(id(odd)))

print('=' * 40)
# ======================================
# shallow vs deep copy

odd = [1, 3, 11, 5, 91, 9, [7, 13]]
backUp = odd.copy()
backUp2 = list(odd)
backUp3 = copy.copy(odd)  # in behtarin ravesh hast

fullBackUp = copy.deepcopy(odd)

odd[-1].append(15)
odd.append(101)
print('odd:', odd)
print('backUp:', backUp)
print('backUp2:', backUp2)
print('backUp3:', backUp3)  # list dakhel list avaz shod chera ke doroste ma dar ye address dg copy kardim vali
# dakhele un -> address list dovom bud ke taghir nakard
print('fullBackUp:', fullBackUp)  # be dakhel tarin ja miravad va hame ra be address jadid copy mikonad

print('=' * 40)
# ======================================

odd = [1, 3, 11, 5, 91, 9, [7, 13]]

backUp = odd
odd = odd + [101]  # assignment
print('normal assignment:', backUp)  # the assignment was in a new address

print('=' * 40)
# ======================================

odd = [1, 3, 11, 5, 91, 9, [7, 13]]

backUp = odd
odd += [101]  # augmented assignment
print('augmented assignment:', backUp)  # using augmented method made the assignment in the same address
# augmented method keeps the address if variable is mutable
