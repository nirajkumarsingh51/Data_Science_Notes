# Write an application in „Python‟ to display the given strings on the standard output device in the 
#given sequence and format: -
    #(1.)    “Welcome to c\turboc” 
print("\"Welcome to C\\turboc\"")

    #(2.) “Welcome To C\Python” 
print("\"Welcome To C\\Python\"")

    #(3.) “Python” is not a difficult language”
print("\"Python” is not a difficult language\"")

    #(4.) “Python‟ is very interesting language”
print("\"Python‟ is very interesting language\"")

    #(5.) “I like „Python‟ very much!”  
print("\"I like „Python‟ very much!\"")

#2. Write an application in „Python‟  to print the following string in a specific format  
#Twinkle, twinkle, little star, 
#How I wonder „what you are‟!  
#Up above the world so high,      
#Like a diamond in the “sky”.  
#Twinkle, twinkle, little star,  
#How I wonder what you are 

# Python program to print the poem in a specific format

print("Twinkle, twinkle, little star,")
print("       How I wonder 'what you are'!")
print("       Up above the world so high,")
print("Like a diamond in the \"sky\".")
print("      Twinkle, twinkle, little star,")
print("      How I wonder what you are")

# a = int(input("enter a number 1"))
# b = int(input("enter a no 2"))

# print("valu 1 ans 2 is " , a+b)


#3. Write an application in „Python‟ to accept one integer and one fractional value from keyboard, 
#calculate and display product.
a = int(input("Enter an intereger Values:"))
b = float(input("Enter a fractional Values:"))
product = a*b
print(a,type(a))
print(b,type(b))
print("The Product Of Interager and Fractional Values is : ", product, type(product))

#4. Write an application in „Python‟ to print series 1 to 5 as a following format:
print("1")
print("   2")
print("      3")
print("         4")
print("            5")

# 5. Write an application program in „Python‟ to reserve three memory locations named empno, salary 
# and itax having values 8801, 12000.00, and 347.82 respectively. Also display the same on the 
# standard output device in the following sequence and format: - 
# EmpNo 
# :: 
# Salary in rupees 
# Income tax in rupees 
# :: 
# :: 
# 8801 
# 12000.00 
# 347.82

empno = 8801
salary = 12000.00
itax = 347.82
 
print("EmpNo")
print("::")
print("Salary in rupees")
print("::")
print("::")
print(empno)
print(salary)
print(itax)

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