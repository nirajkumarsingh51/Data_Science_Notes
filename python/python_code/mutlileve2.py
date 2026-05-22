class A:
    def Adisp():
        print("Adisp called")

class B:
    def Bdisp():
        print("Bdisp called")

class C(A,B):
    def Cdisp():
        print("Cdisp Called")

x=C
x.Cdisp()
x.()