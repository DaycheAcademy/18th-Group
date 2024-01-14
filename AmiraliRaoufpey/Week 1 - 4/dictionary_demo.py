# Mapping

emptyDict = {}
anotherEmptyDict = dict()

# each dictionary element is a pair of "key" & "value"

sampleDict = {'name': 'Amirali',
              'surname': 'Raoufpey',
              'age': 31,
              'city': 'Tehran'}

print(sampleDict['name'])
print(hex(id(sampleDict)))
sampleDict['education'] = 'MBA'
print(hex(id(sampleDict)))  # it's mutable and will not change address
# Accessing values can ONLY be through 'keys'

print('=' * 40)
# ======================================

print(sampleDict.keys())  # prints "view object" . view object is like a list, and it's iterable

keyList = list(sampleDict.keys())
print(keyList)

print('=' * 40)

print(sampleDict.values())
valueList = list(sampleDict.values())
print(valueList)

print('=' * 40)

print(sampleDict.items())  # har eleman list yek tuple 2 ozvi hast
itemTuple = tuple(sampleDict.items())
print(itemTuple)

print('=' * 40)

newDict = dict(itemTuple)  # har tuple ke aza an khod tuple haye 2 ozvi bashad mitavan be dictionaty tabdil kard
print(newDict)

print('=' * 40)
# ======================================

# insertion order
# memory order

# from python 3.6 dictionary has order, but doesn't work in jupiter notebook and pandas, and we need to import
# "ordered dictionary" from "collections"

# ======================================

# dictionary data type restrictions:
# 1 - keys should be immutable, should be hashable (can be: number, string, tuple | can't be: list, set, dictionary)
# 2 - values can be of any data type

# ======================================

# algorithm hashing: jabeye siahi hast ke vorudi migirad va khoruji (digest) midahad ba 4 vizhegi zir:
# 1- be ezaye har vorudi yekta, khoruji yekta khahad bud (hich 2 vorudi khoruji yeki nadarad
# 2- be ezaye har vorudi, tool khoruji sabet hast
# 3- algorithm yektarafe hast, az khoruji nemishe be vorudi resid
# 4- khoruji baraye ensan mafhoum khasi nadarad

# key ha immutable hastan, chera ke ma anha ra hash mikonam va hash ha sabet hast o taghir nemikonad

# ======================================

print(hash('name'))
print(hash('surname'))

print('=' * 40)
# ======================================

for k in sampleDict:
    print(k)

print('=' * 40)
for k in sampleDict:  # complexity ejra: O(N)
    print(sampleDict[k])

print('=' * 40)
for v in sampleDict.values():  # complexity ejra: O(N^2)
    print(v)

# estefade az halghe dovom baraye gereftan value haye dictionary kheili sari tar hast nesbat be halgheye sevom