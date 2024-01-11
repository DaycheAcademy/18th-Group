
# Flow Control
# if, elif, else ---> conditional
# for, else ---> loops
# while

# Chained & Unchained Conditioning

# False:
# int: 0
# float: 0.0
# string: ''    ""  """"""
# list: []
# tuple: ()
# dictionary: {}
# set: set()
# False

age = 18

if age:
    print('we are inside condition block')

# =================================
print('=' * 40)
if not age - 18:
    print('sen 18 sal hast')

# =================================
print('=' * 40)

# ternary operator:

vote = True if age > 18 else False
print(vote)

temp = 'some string'
myString = 'ABC' if temp else 'XYZ'
print(myString)

# =================================
print('=' * 40)
for num in range(1, 100):
    decision = 'Hop-Wiz'if not num % 21 else 'Hop' if not num % 3 else 'Wiz' if not num % 7 else str(num)
    # first need to check 21 then 3 & 7, checking 3 before 7 is more efficient
    # when assigning values all should be same type so num cast to str
    print(decision)

# ======================================

