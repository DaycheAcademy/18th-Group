while True:
    inp=input('enter the number')
    for char1 in inp:
        if(ord(char1)<48):
            print('thas not correct')
            inp=input('enter again')
            break
        if(ord(char1)>57):
        
            print('thas not correct')
            inp=input('enter again')
            break



# isnumeric
# isdigit
# isdecimal
