import ReflectorGenerator as ReG
Reflector_a=ReG.ReflectorGenerator()
Reflector_A=ReG.ReflectorGenerator(True)
def reflector(words):
    words_p=""
    for i in words:
        if i.isupper():
           I=Reflector_A[i]
        else:
           I=Reflector_a[i]
        words_p+=I
    return words_p