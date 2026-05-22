class number:
    a=10
    def accept(p):
        number.a=p
        print("accept called!")
    def disp():
        print("value of a=",number.a)
x=number
# x=number()
x.disp()
x.accept(50)
x.disp()