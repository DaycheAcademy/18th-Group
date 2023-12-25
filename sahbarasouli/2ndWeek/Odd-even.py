myFnumber=[1,2,3,4,5,6,7,8,9,10]
mySnumber=[10,11,21,13,14,15,16,17,18,19,20]

for odd , even in zip(myFnumber[1::+2],myFnumber[::+2]):
    print(f"the odd numbers are : {odd}  and the even numbers are :{even}")

print (mySnumber[mySnumber.__len__():0:-1])
