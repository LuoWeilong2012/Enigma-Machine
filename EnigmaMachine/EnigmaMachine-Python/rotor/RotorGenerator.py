#This function is used to generate a rotor.
def rg(key):#"key"must be a string!Must be a 26-character string
    if len(key)!=26:
        raise ValueError("Input must be a string of length 26.")
    rotor={}
    for i in range(26):
        rotor[chr(i+97)]=key[i]
    return rotor

def RG(key):#"key"must be a string!Must be a 26-character string
    if len(key)!=26:
        raise ValueError("Input must be a string of length 26.")
    rotor={}
    for i in range(26):
        rotor[chr(i+65)]=key[i]
    return rotor