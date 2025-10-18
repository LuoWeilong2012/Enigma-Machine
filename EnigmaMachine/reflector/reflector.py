def out(a,b):
    result = ''.join([char for char in a if char not in b])        
    return result
def reflector():
    word="qwertyuiopasdfghjklzxcvbnm"
    one="mnbvcxzlkjhgf"
    outto=out(word,one)

