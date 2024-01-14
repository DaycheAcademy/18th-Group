# String is a sequence

# Sequence:
# 1 - Ordered
# 2 - Indexable ---> Default : start from Zero

alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Indexing
print(alphabet_string[0])
print(alphabet_string[12])

# Slicing
print(alphabet_string[0: 13])
print(alphabet_string[0: 13: 2])
# print(alphabet_string[start: stop: step])

print('=' * 40)
print(alphabet_string[:13])  # az ebteda ke lozuman avale index nist
print(alphabet_string[2:])  # ta enteha ke lozuman akhare index nist

print('=' * 40)
print(alphabet_string[-1])
print(alphabet_string[-13])
print(alphabet_string[13])

print('=' * 40)
print(alphabet_string[-1: -13])  # Step default +1 hast , inja chizi chap nemishavad
print(alphabet_string[-3: 5])  # inja chizi chap nemishavad

print('=' * 40)
print(alphabet_string[3: -5])
print(alphabet_string[-2: 3: -1])

print('=' * 40)
print(alphabet_string[::-1])  # ways to reverse strings
print(alphabet_string[-1::-1])
print(alphabet_string[len(alphabet_string)-1::-1])
print(alphabet_string[:-len(alphabet_string)-1:-1])
