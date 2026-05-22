#accept a number form keyboard , calculate and disply its hexadecimal
n=int(input("Enter a number: "))
# hex= ""
# while n>0:
#     d=n%16
#     n=n//16
#     if(d==10):
#         hex="A"+hex
#     elif d==11:
#         hex="B"+hex
#     elif d==12:
#         hex="C"+hex
#     elif d==13:
#         hex="D"+hex
#     elif d==14:
#         hex="E"+hex
#     elif d==15:
#         hex="F"+hex;
#     else:
#         hex=str(d)+hex
#     n=n//16
# print("Hexadecimal is : ",hex)

print("Hexadecimal is : ",hex(n))