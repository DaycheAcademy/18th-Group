
sampleString = 'ABCDE'
sampleList = [1, 2, 3]

for char in sampleList:
    print(char)

# char is iterator
# sampleString is iterable object

char = iter(sampleString)  # amalan in function dar "for" penhan ast
elem = iter(sampleList)
print(type(char))
print(type(elem))

# ieterator ha az khodeshun hafezei nadaran va typeshun ro ham az iterable object migiran

print('=' * 40)
# ======================================

print(next(char))  # A
print(next(char))  # B
print(next(char))  # C
print(next(char))  # D
print(next(char))  # E

print(next(char))  # Error StopIteration migirim, khode "for" in ro handel mikone, "break" moaadele inject kardan dasti
# StopIterable be halghe hast
