def out(a,b):
    result = ''.join([char for char in a if char not in b])        
    return result
def PlugboardGenerator(types=False):
    plugboard_dict={}
    words="plmokijnuhbygvtfcrdxeszwaq"
    NotIn="qwertyuiopasdf"
    Yes=out(words,NotIn)
    First='lmkjnh'
    Second=out(Yes,First)
    if types==True:
        words.upper()
        NotIn.upper()
        Yes.upper()
        First.upper()
        Second.upper()
    for i in range(14):
        plugboard_dict[NotIn[i]]=NotIn[i]
    for j in range(6):
        plugboard_dict[First[j]]=Second[j]
        plugboard_dict[Second[j]]=First[j]
    return plugboard_dict