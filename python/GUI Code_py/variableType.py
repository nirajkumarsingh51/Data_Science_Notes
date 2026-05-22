print("Welcome in world of variable")

# print("a =", a)  ## Error: global variable 'a' ko define karne se pehle access kar rahe hain

a = 20

def show():
    b = 10
    print("a =", a, ", b =", b)

def disp():
    print("Value of a =", a)

show()
disp()

print("a is :", a)

# print("b is :", b)  ## Error: local variable 'b' ko function ke bahar access nahi kar sakte ku ke wo local hai 
