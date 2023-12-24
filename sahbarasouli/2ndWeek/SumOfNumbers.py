mystr='1,2.236,-5.4,443,433.4333,53,-3434,434343,4343.434'
numbers=mystr.split(',')
sum=0
for number in numbers:
    sum= ((float)(number))+sum

print('The result is:{:.2f}'.format(sum))