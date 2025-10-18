def out(a,b):
    result = ''.join([char for char in a if char not in b])        
    return result
def ReflectorGenerator(types=False):
    reflector_dict={}
    word="qwertyuiopasdfghjklzxcvbnm"
    one="mnbvcxzlkjhgf"
    outto=out(word,one)
    if types==True:
        word.upper()
        one.upper()
        outto.upper()
    for i in range(13):
        reflector_dict[one[i]]=outto[i]
        reflector_dict[outto[i]]=one[i]
    return reflector_dict
