sampleParagraph = "Atoms of radioactive elements can split. According to Albert Einstein, mass and energy are interchangeable under certain circumstances. When atoms split, the process is called nuclear fission. In this case, a small amount of mass is converted into energy. Thus the energy released cannot do much damage. However, several subatomic particles called neutrons are also emitted during this process. Each neutron will hit a radioactive element releasing more neutrons in the process. This causes a chain reaction and creates a large amount of energy. This energy is converted into heat which expands uncontrollably causing an explosion. Hence, atoms do not literally explode. They generate energy that can cause explosions."
sampleParagraph = sampleParagraph.replace(',', '')
sampleParagraph = sampleParagraph.replace('.', '')
words = sampleParagraph.split(' ')
print(words)
# total number of words in sample paragraph
print('total words in sample paragraph is:\t', len(words))

# total number of Unique words in sample paragraph

setOfwords = set(words)
print('number of unique words is :\t', len(setOfwords))       #  78 word are unique

# total number of to-be verb
toBeverbs = ['am', 'is', 'are', 'be', 'being', 'been', 'was', 'were']
totalTobe = 0
for word in words:
    for tobe in toBeverbs:
        if word == tobe:
            totalTobe += 1
print('total to be verbs using is :\t ', totalTobe)
# ---------------------------------
# calculate sum each to-be verbs in paragraph, and mapping result into dict
accurences = []
for tb in toBeverbs:
    totalAccurence = words.count(tb)
    accurences.append(totalAccurence)
print('for each to be verb so we have here :\n', dict(zip(toBeverbs, accurences)))

