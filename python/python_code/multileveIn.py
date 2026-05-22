class A:
    def Adisp():
        print("Adisp called")

class B(A):
    def Bdisp():
        print("Bdisp called")

class C(B):
    def Cdisp():
        print("Cdisp Called")

x=A
x.Adisp()
# x.Bdisp()

y=B
y.Adisp()
y.Bdisp()

z=C
z.Adisp()
z.Bdisp()
z.Cdisp
