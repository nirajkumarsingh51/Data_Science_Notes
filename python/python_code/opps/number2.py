class number:
    a=10
    def accept(self,p):
        number.a=p
        print("accept called!")
    def disp(self):
        print("value of a=",number.a)

x=number
# x=number()
x.disp()
x.accept(50)
x.disp()
