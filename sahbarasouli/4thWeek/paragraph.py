mainparagraph='So perhaps, you\'ve generated some fancy text, and you\'re content that you can now copy and paste your fancy text in the comments section of funny cat videos, but perhaps you \'re wondering how it is even possible to change the font of your text? Is it some sort of hack? Are you copying and pasting an actual font?'
numberOfeachTobe={}
numberOfTobe=0
totalWord=mainparagraph.replace("\'"," ")
totalWord=(totalWord.split(' '))

myWord=mainparagraph.replace("\'"," ")
myWord=set(myWord.split(' '))

print ("number of all words in paragraph is: " , len(totalWord))
newWord=set(mainparagraph.split(' '))
print ('the number of the new word are: ' , len(newWord))

tobeSet={'am','is','are','re','m','be','was','were','Are','Is','Am'}
dict={'am':0,'is':0,'are':0,'re':0,'m':0 ,'be':0 ,'was':0,'were':0,'Are':0,'Is':0,'Am':0}

for i in ((totalWord)):
    if tobeSet.__contains__(i):
        numberOfTobe+=1
        if(dict.get(i) != None):
            dict.update({i:dict.get(i)+1})
        
print("the number of total tobe verb is: ",numberOfTobe)
newdic={'Is':dict.get('is')+dict.get('Is'),'Are':dict.get('are')+dict.get('Are')+dict.get('re'),'Am':dict.get('Am')+dict.get('am')+dict.get('m')}
print("each tobe: ",newdic)