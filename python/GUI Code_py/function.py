def disp():
    print("disp call")

def check(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("odd")

def high(a,b):
    if a>b:
        return a
    else:
        return b

def product(a):
    b=float(input("Enter a No. : "))
    return(a*b)

check(5)
disp()
h=high(10,4)
print("higest no :",h)
print("Product = ", product(3))
disp()