# Range is also a sequence
# range memory nadarad, az inke ghabli ya badish chi bude khabar nadare

# Generator: be inhayi ke mesl range memory nadaran gofte mishe

import sys

smallRange = range(10)
print(smallRange)

smallList = list(range(10))
print(smallList)

print('=' * 40)
# ======================================

bigRange = range(100)
bigList = list(range(100))

print('size of smallRange in memory: {}'.format(sys.getsizeof(smallRange)))
print('size of bigRange in memory: {}'.format(sys.getsizeof(bigRange)))
print('size of smallList in memory: {}'.format(sys.getsizeof(smallList)))
print('size of bigList in memory: {}'.format(sys.getsizeof(bigList)))

# size range faregh az andaze range sabet hast, 10 va 100 barash farghi nadare

# Range(start, stop, step) hamanand slicing dar string ha hast

print('=' * 40)
# ======================================

a = 928374203948023948701234598702349872938032
# mikhahim bebinim in adad bar 1402 bakshpazir hast ya na?

print(a in range(0, 999999999999999999999999999999999999999999, 1402))

# zarb va taghsim kheili memory intensive hastan, va estefade az range bejaye una herfei tare
