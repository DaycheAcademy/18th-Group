# unordered data type, na insertion va na memory order nadaran

# you 'CAN NOT' define empty set using literals
# emptySet = {} in set e khali nist, dictionary hast

emptySet = set()

sampleSet = {1, 'A', 'g', 3.86, 'Dayche'}
print(sampleSet)

# harbar barname ro ejra konim ye khoruji mide

print('=' * 40)
# ======================================

for _ in range(10):
    print(sampleSet)
# khoruji ha hame yeksan hast, chera ke ba hamun tartibi ke ruye memory gharar dade dare chap mikone 10 martabe

print('=' * 40)
# ======================================

odd = set(range(1, 50, 2))  # members: 25
power = {1, 4, 9, 16, 25, 36, 49}  # members: 7

print(odd.intersection(power))
print(len(odd.union(power)))
# set ha ozv tekrari nemipazirand

sameSampleSet = {1, 'A', 'g', 3.86, 'Dayche', 'A', 'A'}

print('=' * 40)
# ======================================
