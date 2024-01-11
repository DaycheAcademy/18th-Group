
# for <iterator> in <iterable object>:
#    1 -
#    2 -
#    3 -

for i in range(10):
    print(i)

print('=' * 40)
alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in alphabet_string:
    print(char)

# ======================================

print('=' * 40)
for char in alphabet_string[::-1]:
    print(char)

# ======================================
# backward iteration
print('=' * 40)
N = 5
for num in range(N, 0, -1):  # bejaye 0 agar -1 bezarim khod 0 ro ham shamel mishe
    print(num)

# ======================================

print('=' * 40)
for i in range(len(alphabet_string)):
    print(alphabet_string[i])

print('=' * 40)

# ======================================

for char in alphabet_string:
    if char in 'cQmnr':
        break  # az halghe birun miad
    if char in 'CFGJK':
        continue  # be dor badi halghe mire
    print(char)
else:
    print('agar halghe break nashavad in else ejra mishe !')

print('=' * 40)
# ======================================

for num in range(2, 50):
    for i in range(2, num // 2 + 1):
        if not num % i:
            break
    else:
        print(num)

print('=' * 40)
# ======================================

for ind, char in enumerate(alphabet_string, 1):  # shomarande hast va az adad entekhabi shorou mikone
    print('character #{}: {}'.format(ind, char))

print('=' * 40)
# ======================================

sampleAlphabet = 'ABCDEF'
sampleNumbers = '123456'

for num, char in zip(sampleNumbers, sampleAlphabet):
    print(f'{num}: is {char}')

print('=' * 40)
# ======================================

for even, odd in zip(alphabet_string[::2], alphabet_string[1::2]):
    print(even, odd)

print('=' * 40)
# ======================================
