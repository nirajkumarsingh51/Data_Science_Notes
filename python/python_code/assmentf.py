# 6. Write an application in „Python‟ to accept values for product number, unit price, and quantity 
# taken from the standard input device. Also display the same on the standard output device in the 
# following sequence and format: - 
# Product No 
# Unit price in rupees 
# Quantity taken in pieces 
# ::   ?
# ::   ?
# ::   ?

productNo = input("Enter Product No: ")
unitPrice = float(input("Enter Unit price in rupees: "))
quantity = int(input("Enter Quantity taken in pieces: "))

print("\nProduct No")
print("::", productNo)

print("Unit price in rupees")
print("::", unitPrice)

print("Quantity taken in pieces")
print("::", quantity)