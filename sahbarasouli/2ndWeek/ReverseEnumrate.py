alpha="abcdefghijklmno"
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i , j in zip(alpha[::-1],numbers[::-1]):
    print(f"the char is {i} and the num is {j}")