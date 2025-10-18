import RotorGenerator as RG
class Rotor:
    def __init__(self,key):
        self.key=key
        self.rotor_a=RG.RG(key,)
        self.rotor_A=RG.RG(key,types=True)
    def Advance_A(self,number=1):
        for _ in range(number):
            rotor=dict(self.rotor_A)
            for i in range(26):
                if i+65==90:
                    self.rotor_A[chr(i+65)]=rotor["A"]
                else:
                    self.rotor_A[chr(i+65)]=rotor[chr(i+66)]
    def Advance_a(self,number=1):
        for _ in range(number):
            rotor=dict(self.rotor_a)
            for i in range(26):
                if i+97==122:
                    self.rotor_a[chr(i+97)]=rotor["a"]
                else:
                    self.rotor_a[chr(i+97)]=rotor[chr(i+98)]
    def Retract_A(self,number=1):
        for _ in range(number):
            rotor=dict(self.rotor_A)
            for i in range(26):
                if i+65==65:
                    self.rotor_A[chr(i+65)]=rotor["Z"]
                else:
                    self.rotor_A[chr(i+65)]=rotor[chr(i+64)]
    def Retract_a(self,number=1):
        for _ in range(number):
            rotor=dict(self.rotor_a)
            for i in range(26):
                if i+97==97:
                    self.rotor_a[chr(i+97)]=rotor["z"]
                else:
                    self.rotor_a[chr(i+97)]=rotor[chr(i+96)]