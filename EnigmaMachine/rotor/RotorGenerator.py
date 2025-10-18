#This function is used to generate a rotor.
def RG(strs,*,types=False):#"key"must be a string!Must be a 26-character string
    rotor={}
    if types==True:
        for i in range(26):
            rotor[chr(i+97)]=strs[i]
    else:
        for i in range(26):
            rotor[chr(i+65)]=strs[i]
    return rotor

