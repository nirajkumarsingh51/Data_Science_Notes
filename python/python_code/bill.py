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
print("================================================")
print("Item Code             ::",icode)
print("================================================")
print("Unit Price in Rs      ::",uprice)
print("Quantity Taken        ::",qty)
print("================================================")
print("Total Amount in Rs    ::",tot)
print("Discount Amount in Rs ::",disc)
print("================================================")
print("Net Payable Amount in Rs::",pamt)