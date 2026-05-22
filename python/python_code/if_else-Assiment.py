# # 1. Wap in ‘Python’ language to accept two values and calculate highest value and lowest value.
# a=int(input("Enter a 1 no.: "))
# b=int(input("Enter a 2 no.: "))

# if a > b:
#     print("Highest value is:", a)
#     print("Lowest value is:", b)
# elif b > a:
#     print("Highest value is:", b)
#     print("Lowest value is:", a)
# else:
#     print("Both numbers are equal.")
    

# # # 2.  Wap in ‘Python’ language to accept a number, check and display the message whether it is positive 
# # # or negative number.

# a=int(input("Enter a 1 no.: "))
# if a>0:
#     print("positive Number")
# elif a<0:
#     print("Negative Number")
# else:
#     print("Number is Zero")

# 3.  Wap in ‘Python’ language to accept a number, check and display the message whether it is even or  
# odd number.
# a=int(input("Enter a 1 no.: "))
# if a%2==0:
#     print("even Number")
# else:
#     print("Odd Number")

# # 4. Wap in ‘Python’ language to accept a number, check and display the message whether it is positive 
# # even or positive odd or negative even or negative odd. 

# a=int(input("Enter a 1 no.: "))
# if  a>0:
#     if a%2==0:
#         print("No is positve even")
#     else:
#         print("Positve Odd")
# elif a<0:
#     if a%2==0:
#         print("Negatve even")
#     else:
#         print("Negative odd")
# else:
#     print("No is ZERO")

# # 5. Wap in ‘Python’ language to accept a character, check and display the message whether it is a digit 
# # or an alphabet or a special symbol. 

# ch=ord(input("Enter a character:"))
# if ch>=65 and ch<=90:
#     print("An Alphabet")
# elif ch>=97 and ch<=122:
#     print("An Alphabet")
# elif ch>=48 and ch<=57:
#     print("Digits")
# else:
#     print("Special Symbol")



# #6 Wap in ‘Python’ to accept a character, and determine whether the character is small case or capital case 
# # letter.

# ch=ord(input("Enter a character:"))
# if ch>=65 and ch<=90:
#     print("Capital letter")
# elif ch>=97 and ch<=122:
#     print("Small letter")
# elif ch>=48 and ch<=57:
#     print("Digits")
# else:
#     print("OtherWise")

# # 7. Wap in ‘Python’ language to accept a number, check and display the message whether it is positive or 
# # negative or neither +ve nor –ve.

# a=int(input("Enter a 1 no.: "))
# if a>0:
#     print("positive Number")
# elif a<0:
#     print("Negative Number")
# else:
#     print("neither +ve nor –ve")

# # 8. Wap in ‘Python’ to accept total no. in 500 and find out percentage and display remarks, where remarks 
# # will be given sequence and format:- 
# # per>=30 and per < 45 pass      
# # per>=45 and per <60 second 
# # per>=60 and per <=100 first 
# # otherwise fail.

# total = 500
# M = int(input("Enter total marks obtained (out of 500): "))
# per = M / total * 100
# print("Percentage =", per, "%")
# if per >= 30 and per < 45:
#     print("Remark: Pass")
# elif per >= 45 and per < 60:
#     print("Remark: Second Division")
# elif per >= 60 and per <= 100:
#     print("Remark: First Division")
# else:
#     print("Remark: Fail")

# # 9. Wap in ‘Python’ to accept year and display a message whether the year is a leap year or not. 
# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print("Given year", year, "is a leap year")
#     else:
#         print("Given year", year, "is not a leap year")
# elif year % 4 == 0:
#     print("Given year", year, "is a leap year")
# else:
#     print("Given year", year, "is not a leap year")


# # 10. Wap in ‘Python’ to accept six digit no. from keyboard, check and display a message whether given 
# # number is palindrome or not.
# n=int(input("Enter a 6-Digit no. : "))
# temp = n
# d1=n%10
# n=n//10
# d2=n%10
# n=n//10
# d3=n%10
# n=n//10
# d4=n%10
# n=n//10
# d5=n%10
# n=n//10
# rev=d1*100000+d2*10000+d3*1000+d4*100+d5*10+n
# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 11. Wap in ‘Python’ language to accept three numbers, check and display the highest value on the 
# standard output device, using nested if ..else. 

# a=int(input("Enter 1 no. : "))
# b=int(input("Enter a 2 no. : "))
# c=int(input("Enter a 3rd No. "))

# if a>b:
#     if a>c:
#         print("A is the higest",a)
#     else:
#         print("C is the higest ",c)
# elif b>c:
#     print("B is the Higest ",b)
# else:
#     print("C is the Higest ",c)


# # 12. Wap in ‘Python’ language to accept four numbers, check and display the highest value on the 
# # standard output device, using nested if..else. 
# a=int(input("Enter a 1st no. : "))
# b=int(input("Enter a 2nd No. : "))
# c=int(input("Enter a 3rd No. : "))
# d=int(input("Enter a 4th No. : "))
# if a > b:
#     if a > c:
#         if a > d:
#             print("A is the highest number:", a)
#         else:
#             print("D is the highest number:", d)
#     else: 
#         if c > d:
#             print("C is the highest number:", c)
#         else:
#             print("D is the highest number:", d)
# else:  
#     if b > c:
#         if b > d:
#             print("B is the highest number:", b)
#         else:
#             print("D is the highest number:", d)
#     else: 
#         if c > d:
#             print("C is the highest number:", c)
#         else:
#             print("D is the highest number:", d)

# # 13. Wap in ‘Python’ language to accept five numbers, check and display the highest value on the
# # standard output device, using nested if..else.

# a=int(input("Enter a 1st no. : "))
# b=int(input("Enter a 2nd No. : "))
# c=int(input("Enter a 3rd No. : "))
# d=int(input("Enter a 4th No. : "))
# e=int(input("Enter a 5th No. : "))

# if a > b:
#     if a > c:
#         if a > d:
#             if a>e:
#                 print("A is the Higest No. : ",a)
#             else:
#                 print("E is the Higest No. : ",e)
#         else:
#             if d>e:
#                 print("D is the higest No. :",d)
#             else:
#                 print("E is the higest No. : ",e)
#     else:
#         if c>e:
#             print("C is the higest No. : ",c)
#         else:
#             print("E is The Higest No. :",e)
# else:
#     if b>c:
#         if b>d:
#             if b>e:
#                 print("B is the Higest No. : ",b)
#             else:
#                 print("E is the higest No. : ",e)
#         else:
#             if d>e:
#                 print("D is the higest No. : ",d)
#             else:
#                 print("E is the higest no. : ",e)
#     else:
#         if c>e:
#             print("C is the Higest No. : ",c)
#         else:
#             print("E is the higest No. : ",e)


# # 14. Wap in ‘Python’ language for an institute to accept a student’s registration number and marks
# # obtained in the papers c, cpp and java. Display the marks detail in the following format as criteria
# # given below: -
# #  Each paper is of maximum 60 marks.
# #  Minimum pass marks in each paper is 30%.
# #  No any negative marking in any paper.
# #  The result will be PASS, if all the papers passed otherwise FAIL.

# stud_reg = input("Enter a Regersation No. : " )
# c=float(input("Enter a 'c' Marks (eg: maximum 60 marks) : ")) 
# cpp =float(input("Enter a 'cpp' Marks (eg: maximum 60 marks) : ")) 
# java = float(input("Enter a 'java' Marks (eg: maximum 60 marks) : ")) 

# max_marks= 60
# pass_marks=0.3* max_marks
# result = "FAIL"

# if c<0 or c>max_marks:
#     print("C Marks is Invalid",c)
#     result = "INVALID"
# else:
#     if cpp<0 or cpp>max_marks:
#         print("CPP Marks is Invalid. ",cpp)
#         result = "INVALID"
#     else:
#         if java < 0 or java > max_marks:
#             print("Java Marks is Invalid",java)
#             result = "INVALID"
#         else:
#             # Nested PASS/FAIL checking
#             if c >= pass_marks:
#                 if cpp >= pass_marks:
#                     if java >= pass_marks:
#                         result = "PASS"
#                     else:
#                         result = "FAIL"
#                 else:
#                     result = "FAIL"
#             else: 
#                 result = "FAIL"

# print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = = = = = = = = = = =")
# print("                             Marks Detail")
# print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = = = = = = = = = = =")
# print("  Registration Number    ::  ",stud_reg)
# print("  Marks Obtained in C    ::  ",c)
# print("  Marks Obtained in Cpp  ::  ",cpp)
# print("  Marks Obtained in Java ::  ",java)
# print("  Result remarks         ::  ",result)
# print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = = = = = = = = = = =")


# 15.Wap in ‘C’ language for an organization to accept employee number and basic salary, calculate
# DA@10% of basic salary if the basic salary is more than 4000 otherwise @15%. Similarly calculate
# HRA@20% of basic salary if the basic salary is less than 8000 otherwise @15%. Calculate and display
# the salary detail of the employee in the following format, as income tax to be deducted @12% of Gross
# Salary if Gross Salary exceeds from 12000.

eno = input("Enter a Employees No. : ")
bas_saly = float(input("Enetr a Basics Salary. : "))
if bas_saly>4000:
    da=bas_saly*10/100
else:
    da=bas_saly*15/100
if bas_saly<8000:
    hra =bas_saly*20/100
else:
    hra= bas_saly*15/100
gross=bas_saly+da+hra
if gross>12000:
    itax=gross*12/100
else:
    itax=0
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = = = = = = = = = = =")
print("                             Salary Detail")
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = = = = = = = = = = =")
print("Employee Number              :   ",eno)
print("Basic Salary in Rs.          :   ",bas_saly)
print("DA in Rs.                    :   ",da)
print("HRA in Rs.                   :   ",hra)
print("Gross Salary in Rs.          :   ",gross)
print("Income Tax Deduction in Rs.  :   ",itax)
print("Net Payable Amount in Rs.    :   ",gross-itax)
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = = = = = = = = = = =")
