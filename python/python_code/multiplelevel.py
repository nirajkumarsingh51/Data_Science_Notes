class A:
    def Adisp():
        print("Adisp called")

class B(A):
    def Bdisp():
        print("Bdisp called")

class C(B):
    def Cdisp():
        print("Cdisp Called")

x=C
x.Adisp()
x.Bdisp()
x.Cdisp()
