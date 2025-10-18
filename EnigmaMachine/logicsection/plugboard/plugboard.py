import PlugboardGenerator as PG
Plugboard_A=PG.PlugboardGenerator(True)
Plugboard_a=PG.PlugboardGenerator()
def reflector(words):
    words_p=""
    for i in words:
        if i.isupper():
           I=Plugboard_A[i]
        else:
           I=Plugboard_a[i]
        words_p+=I
    return words_p