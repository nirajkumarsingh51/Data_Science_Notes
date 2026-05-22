class A:
    def Adisp():
        print("Adisp called")

class B(A):
    def Bdisp():
        print("Bdisp called")

x=A
x.Adisp()
# x.Bdisp()
y=B
y.Adisp()
y.Bdisp()