class A:
    def disp(self):
        print("Adisp called")
        
    def __init__(self):
        print("A default constructor A")



class B(A):
    def __init__(self):
        print("A default constructor B ")
        super().__init__()
    def disp(self):
        print("Bdisp called")
        
        # super() .disp()
        # A.disp()

x=B()
x.disp()
