# WAP in “Python” language to accept item code, unit price and quantity taken. Calculate and print
# the bill in the following sequence and format, as 20% discount available on all items.
# ========================================
# Item Code ::
# ========================================
# Unit Price in Rs. ::
# Quantity Taken ::
# ========================================
# Total Amount in ::
# Discount Amount ::
# ========================================
# Net Payable Amount ::

icode=input("Enter item code:")
uprice=float(input("Enter unit price:"))
qty=int(input("Enter total quantity:"))
tot=uprice*qty
disc=tot*20/100
pamt=tot-disc
r="\n================================================\nItem Code             ::"+str(icode)+"\n================================================\nUnit Price in Rs      ::"+str(uprice)+"\nQuantity Taken        ::"+str(qty)+"\n================================================\nTotal Amount in Rs    ::"+str(tot)+"\nDiscount Amount in Rs ::"+str(disc)+"\n================================================\nNet Payable Amount in Rs::"+str(pamt)
print(r)
f=open("data.txt","w")
f=open("data.txt","a")
f.write(r)
f=open("data.txt","r")
print(f.read())
# print(f.read(200))
# print(f.readline())
# print(f.readlines())
f.close()