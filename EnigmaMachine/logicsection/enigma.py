import sys
import path
import rotor
import reflector
import plugboard
Rotor1=rotor.Rotor("qwertyuiopasdfghjklzxcvbnm")
Rotor2=rotor.Rotor("plokmijnuhbygvtfcrdxeszwaq")
Rotor3=rotor.Rotor("zxcvbnmasdfghjklqwertyuiop")
def enigma(words,key1,key2,key3):#key_x is in uppercase
    key1=chr(key1)-65
    key2=chr(key2)-65
    key3=chr(key3)-65
