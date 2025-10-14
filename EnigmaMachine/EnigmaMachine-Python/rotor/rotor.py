import RotorGenerator as RG
class Rotor:
    def __init__(self,key):
        self.key=key
        self.rotor_a=RG.rg(key)
        self.rotor_A=RG.RG(key)
    def Advance_A(self.rotor_A):
        rotor=dict(self.rotor_A)
        for i in range(26):
            