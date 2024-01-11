# tuple is a sequence

# tuples are immutable

import sys  # har anche marbut be machine mishavad
import os  # har anche marbut be system amel mishavad

emptyTuple = ()  # literal
anotherEmptyTuple = tuple()  # constructor (iterable behesh pass midahim)

# sampleTuple0 = (1, 2, 3)
sampleTuple = 1, 2, 3  # baraye tarif tuple niazi be gharar dadan parantez nist
print(type(sampleTuple))

print(1, 2, 3)
print((1, 2, 3))  # baraye jaii ke agar parantez nazarim eshtebahan nemifahmad ke manzoor ma tuple hast mizarim

# dar mored list ha tarjihman in bud ke tanha az yek noe data type ra gharar dahim, dar morede tuple tosie shode ke
# agar data type ha mokhtalef hastan az tuple estefade konim, mutable hast va taghir nemikonad va method hayi mesle
# sort o append nadarad, hata assign meghdar ham be aza nadarad chera ke gheyre ghabele taghir ast

# sampleTuple[0] = 10 -> in support nemishavad chon immutable ast
print(hex(id(sampleTuple)))

sampleTuple = sampleTuple[0], 10, sampleTuple[2]
print(sampleTuple)
print(hex(id(sampleTuple)))
# ba in ravesh ke maghadir dar yek samt hesab shavad va assign shavad be yek address jadid emkanpazir ast

print('=' * 40)
# ======================================

album = 'Homayoun Shajarian', 2003, ('nasim-e-vasl', 'sokoot', 'havay-e-gerye')

artist, year, tracks = album  # tuple unpacking

print(artist)
print(year)
print(tracks)

print('=' * 40)
# ======================================
# list vs tuple:
# 1 - ager gharar ast in moteghayer ta akhar sabet bemanad tuple tarif mikonim
# 2 - chera baraye sabet list na? chon tuple behine tar az fazaye memory estefade mikone
# 3 - etelaati ke az database khande mishan be sourate pishfarz Tuple hast, chon gharar nist rahat taghir bedim va
# jaye kamtari ham migire

oddList = list(range(1, 20, 2))
oddTuple = tuple(range(1, 20, 2))

print('size of oddList on memory: {} BYTES'.format(sys.getsizeof(oddList)))
print('size of oddTuple on memory: {} BYTES'.format(sys.getsizeof(oddTuple)))

print('=' * 40)
# ======================================
