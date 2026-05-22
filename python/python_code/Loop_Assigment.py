# # 1. Wap in “Python‟ language to display “Python is General Purpose language” five times.

# i=1
# while i<=5:
#     print("Python is General Purpose language")
#     i=i+1

# # 2. Wap in “Python‟ language to display “I like „Python‟ very much!” three times and each after two
# # lines.

# i=1
# while i<=2:
#     print("“I like „Python‟ very much!”")
#     i=i+1

# # 3. Wap in “Python‟ language to display “I like „Python‟ very much!” continuously until a zero is
# # pressed.

# while True:
#     print("“I like „Python‟ very much!”")
#     user=input("Press 0 to stop: ")
#     if user=='0':
#         break

# # 4. Wap in “Python‟ language to display the counting starting from 1 and up to 30.
# i=1
# while i<=30:
#     print(i)
#     i=i+1

# # 5. Wap in “Python‟ language to display the following format:-
# # 1) 1 2 3 ... up to 19
# i=1
# while i<=19:
#     print(i,end=" ")
#     i=i+1
# print("\n")
# #  1 3 5......................... Up to 19
# i=1
# while i<=19:
#      print(i,end=" ")
#      i=i+2
# print("\n")
# #  1 4 7......................... Up to 19
# i=1
# while i<=19:
#      print(i,end=" ")
#      i=i+3
# print("\n")

# #  19 18 17.................... Up to 1

# i=19
# while i>=1:
#      print(i,end=" ")
#      i=i-1
# print("\n")

# #  19 17 15.................... Up to 1
# i=19
# while i>=1:
#      print(i,end=" ")
#      i=i-2
# print("\n")

# #  19 16 13.................... Up to 1
# i=19
# while i>=1:
#      print(i,end=" ")
#      i=i-3
# print("\n")

# #  2 4 8.......................... Up to 20
# i=2
# while i<=19:
#      print(i,end=" ")
#      i=i+2
# print("\n")

# #  3 6 9.......................... Up to 30
# i=3
# while i<=30:
#      print(i,end=" ")
#      i=i+3
# print("\n")
# #  4 8 12........................ Up to 40
# i=4
# while i<=40:
#      print(i,end=" ")
#      i=i+4
# print("\n")

# #  20 18 16..................... Up to 2
# i=20
# while i>=2:
#      print(i,end=" ")
#      i=i-2
# print("\n")
# #  30 27 23..................... Up to 3
# i=30
# while i>=3:
#      print(i,end=" ")
#      i=i-3
# print("\n")
# #  40 38 36..................... Up to 4
# i=40
# while i>=4:
#      print(i,end=" ")
#      i=i-4
# print("\n")

# #  1 4 9........................... Up to 100
# i=1
# while i<=100:
#      print(i,end=" ")
#      i=i+3
# print("\n")

# #  1 8 27......................... Up to 1000
# i=1
# while i**3 <=1000:
#      print(i**3,end=" ")
#      i=i+1
# print("\n")

# #  1 16 81....................... Up to 10000
# i=1
# while i**4 <=10000:
#      print(i**4,end=" ")
#      i=i+1
# print("\n")
# #  1 10 100..................... Up to 1000000000
# i=1
# while i<=1000000000:
#      print(i,end=" ")
#      i=i*10
# print("\n")
# #  1000000000................... Up to 1
# i=1000000000
# while i>=1:
#      print(i,end=" ")
#      i=i//10
# print("\n")
# #  123456789
# i=1
# while i<=9:
#      print(i,end="")
#      i=i+1
# print("\n")


# # 6. Wap in “Python‟ language to accept thirty numbers calculate and display the sum, product
# c = 1
# t = 0
# p = 1
# while c <= 30:
#     num = float(input("Enter number " + str(c) + ": "))
#     t = t + num
#     p = p * num
#     c = c + 1
# average = t / 30
# print("\nSum =", t)
# print("Product =", p)
# print("Average =", average)

# # 7. Wap in “Python‟ language to accept N numbers calculate and display the sum, product and
# # average value.
# n=int(input("Enter How many You Want! : "))
# c = 1
# t = 0
# p = 1
# while c <= n:
#     num = float(input("Enter number " + str(c) + ": "))
#     t = t + num
#     p = p * num
#     c = c + 1
# average = t / n
# print("\nSum =", t)
# print("Product =", p)
# print("Average =", average)

# 8. Wap in “Python‟ language to accept N numbers calculate and display the total count of even and
# odd numbers.
# n=int(input("Enter How many You Want! : "))
# c = 1
# even_c=0
# odd_c=0
# while c <= n:
#     num = float(input("Enter number " + str(c) + ": "))
#     if num%2==0:
#         even_c +=1
#     else:
#         odd_c +=1
#     c +=1
# print("\nTotal Even Number =", even_c)
# print("Total odd number ", odd_c)

# # 9. Wap in “Python‟ language to accept N numbers calculate and display the total count of +
# # ve
# # even
# # and -
# # ve odd numbers.
# n=int(input("Enter How many You Want! : "))
# c = 1
# even_c=0
# odd_c=0
# while c <= n:
#     num = float(input("Enter number " + str(c) + ": "))
#     if num%2==0:
#         even_c +=1
#     else:
#         odd_c +=1
#     c +=1
# print("\nTotal Even Number =", even_c)
# print("Total odd number ", odd_c)

# # 10. Wap in “Python‟ language to accept N characters one-by-one calculate and display the total count
# # of digits and alphabets.

# n=int(input("How many character you want ! :"))
# i=1
# dig=alp=0
# for i in range(1,n+1):
#     ch=ord(input("Enter a character :"))
#     if (ch>=65 and ch<=90) or (ch>=97 and ch<122):
#         alp=alp+1
#     elif ch>=48 and ch<=57:
#         dig=dig+1
#     i=i+1
# print("Total alpha",alp , "\n digits : ",dig)

# # 11. Wap in “Python‟ language to accept N numbers check and display the smallest and largest value
# n=int(input("Enter the number of elements: "))
# number = []
# for i in range(n):
#     num = int(input("Enter number {i+1}: "))
#     number.append(num)
# smallest=min(number)
# largest=max(number)
# print("Smallest No. is ",smallest,"\nLargest No.",largest)

# # 12. Wap in “Python‟ language to accept a number calculates and display the total count of digits.

# # n=input("Enter a No., You Want! :")
# # c=len(n)
# # print("The count of digits ",n," is : ",c)

# n=int(input("Enter a no : "))
# i=0
# while n>0:
#     n=n//10
#     i=i+1
# print("Total digit are : ",i)

# # 13. Wap in “Python‟ language to accept a number calculates and display the sum, product and
# # average of the digits.
# n=input("Enter a no. : ")
# b=len(n)
# n=int(n)
# sum=0
# product=1
# temp=n
# while n>0:
#     d=n%10
#     sum=sum+d
#     product=product*d
#     n = n // 10 
# avg = sum/b
# print("The Sum of digits ",temp,"is :",sum)
# print("The Product of digits ",temp,"is :",product)
# print("The Average of digits ",temp,"is :",avg)

# # # 14. Wap in “Python‟ language to generate even series from 1 to 50.
# i=1
# print("The evan series of 1 to 50 :")
# while i<=50:
#     if i%2==0:
#         print(i,end=" ")
#     i=i+1

# # 15. Wap in “Python‟ language to generate odd series from 1 to 50.
# print("Odd series from 1 to 50:")
# for i in range(1,51):
#     if i%2 !=0:
#         print(i,end=" ")
#     i=i+1

# # 16. Wap in “Python‟ language to accept a number, display it in reverse order
# n=int(input("Enter a no. : "))
# reverse_num = 0
# num = n 
# while num > 0:
#     digit = num % 10    
#     reverse_num = reverse_num * 10 + digit
#     num = num // 10 
# print("The reverse digit ",n,"is : ",reverse_num)

# # 17. Wap in “Python‟ language to generate a table of any number.
# n=int(input("Enter a no, you want to Generate Table! : "))
# i=1
# for i in range (1,11):
#     print(n,"X", i, "=" ,n*i)

# # 18. Wap in “Python‟ language to accept a number, check and display whether the number is prime or not.
# n=int(input("Enter a No to check, prime or Not-prime : "))
# if n<=1:
#         print(n,", It is Not prime.")
# else:
#     i = 2
#     while i < n:
#         if n % i == 0:
#             print(n,", It is Not Prime")
#             break
#         i += 1
#     else:
#         print(n,", It is Prime")

# # 19. Wap in “Python‟ language to accept initial and final position and find the prime numbers between the
# # initial and final position.
# initial=int(input("Enter a Initial Number : "))
# final=int(input("Enter a Final Number : "))
# num=initial
# while num<=final:
#     if num>1:
#         i=2
#         while i<num:
#             if num% i==0:
#                 break
#             i+=1
#         else:
#             print(num, "is Prime")
#     num +=1

# # 20. Wap in “Python‟ language to accept a number, check and display message whether it perfect number
# # or not.
# n=int(input("Enter a no : "))
# d=2
# s=1
# while d<=n/2:
#     if n%d==0:
#         s=s+d
#     d=d+1
# if s==n:
#     print("Given No is Perfect !")
# else:
#     print("Given no is not Perfect !")

# # 21. Wap in “Python‟ language to accept a number, check and display whether the number is Armstrong
# # or not.
# n=input("Enter a no. :")
# b=len(n)
# n=int(n)
# s=0
# temp = n
# while n>0:
#     d=n%10
#     s=s+d**n 
#     n=n//10
# if temp==s:
#     print("Given no ",temp," is armstrong : ")
# else:
#     print("Given no ",temp," is Not-armstrong : ")

# # 22. Wap in “Python‟ language to accept initial and final position, print Armstrong number between initial
# # and final position.
# initial=int(input("Enter a Initial Number : "))
# final=int(input("Enter a Final Number : "))
# num=initial
# while num<=final:
#     temp = num
#     sum_of_cubes = 0
#     while temp > 0:
#         digit = temp % 10
#         sum_of_cubes += digit ** 3
#         temp //= 10
#     if sum_of_cubes == num:
#         print(num, "is an Armstrong number")
#     num +=1

# # 23. Wap in “Python‟ language to accept a number and display its factorialvalue.
# # using for loop:
# n=int(input("Enter a no. : "))
# fact =1
# for n in range(n,0,-1):
#     fact=fact*n
# print("The factorial is : ",fact)

# 28. Wap in “Python‟ language to accept two numbers check and display the Highest Common Factor
# or Greatest Common Factor
# a=int(input("Enter first No.    : "))
# b=int(input("Enter a Second No. : "))
# if a<b:
#     n=a
# else:
#     n=b
# for d in range(1,n+1):
#     if a%d==0 and b%d==0:
#         h=d
# print("Heigest commmon factor: ",h)

# #or
# import math as m
# a=int(input("Enter first No.    : "))
# b=int(input("Enter a Second No. : "))
# print("Heigest common factor is : ", m.gcd(a,b))

# 29. Wap in “Python‟ language to accept two numbers check and display the Lowest Common Factor except 1 .
# a=int(input("Enter first No.    : "))
# b=int(input("Enter a Second No. : "))
# if a<b:
#     n=a
# else:
#     n=b
# for d in range(2,n+1):
#     if a%d==0 and b%d==0:
#         h=d
#         break
# print("Lowest  commmon factor: ",h)
# # 30. Wap in “Python‟ language to display 20 terms of Fibonacci series . (i.e 0,1,1,2,3,.).
# a=0
# b=1
# i=1
# print("Fibonancii seriecs are: ",a,b,end=" ")
# while i<=18:
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#         i=i+1

# # 31. Wap in “Python‟ language to accept a positive integer value, determine and print its binary
# # equivalent.
# num = float(input("Enter a positive integer: "))
# if num < 0:
#     print("Please enter a positive integer.")
# else:
#     if num == 0:
#         print("Binary equivalent is: 0")
#     else:
#         binary = ""     
#         while num > 0:
#             remainder = num % 2
#             binary = str(remainder) + binary
#             num = num // 2     
#         print("Binary equivalent is:", binary)

# # 32. Wap in “Python‟ language to accept a positive value, convert into hexadecimal equivalent.
# n = int(input("Enter a number: "))
# hexa = ""
# while n > 0:
#     d = n % 16
#     n = n // 16   
#     if d == 10:
#         hexa = "A" + hexa
#     elif d == 11:
#         hexa = "B" + hexa
#     elif d == 12:
#         hexa = "C" + hexa
#     elif d == 13:
#         hexa = "D" + hexa
#     elif d == 14:
#         hexa = "E" + hexa
#     elif d == 15:
#         hexa = "F" + hexa
#     else:
#         hexa = str(d) + hexa

# print("Hexadecimal is:", hexa)

# # 33. Wap in “Python‟ language to display the total count of Leap Years between 1000 and 2009.
# year = 1000
# count = 0
# while year <= 2009:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         count += 1
#     year += 1

# print("Total number of leap years between 1000 and 2009 is:", count)

# # 35. Wap in “Python‟ language to calculate and display the Fibonacci series up to n terms.
# # [Hint: 0 1 1 2 3 5 8 13 21 …..]
# a=0
# b=1
# i=1
# print("Fibonancii seriecs are: ",a,b,end=" ")
# while i<=18:
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#         i=i+1

# # 36. Write a program in “Python‟ to generate the following given series:-
# # using for loop:
# n=int(input("Enter a no. : "))
# fact =1
# for n in range(n,0,-1):
#     fact=fact*n
# print("The factorial is : ",fact)
# ###
# for i in range(1,6):
#     print(" "*(5-i),"*"*(2*i-1),sep="")

# ##########
# # # using for loop
# for i in range(1,6):
#     j=1
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# #############
# for i in range(1,6):
#     for j in range(1,i+1):
#         print((i+j)%2,end=" ")
#     print()

#E
for i in range (5):
    print("  "*(4-i), end="")  
    for j in range(i, -1, -1):
        print(j, end=" ")     
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# # #f
# for i in range(1,6):
#     k=i
#     for j in range(1,6):
#         if k==6:
#             k=1
#         print(end=str(k%6))
#         k=k+1
#     print()
