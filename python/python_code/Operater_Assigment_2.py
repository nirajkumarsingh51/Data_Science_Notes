# # 1. WAP in “Python” language to accept two numbers from keyboard and display the sum, product and 
# # average of the given numbers in the following sequence and format: - 
# # Both numbers 
# # Sum         ::
# # Product     ::
# # Average     ::  
# a=float(input("Enter a 1 No.:"))
# b=float(input("Enter a 2nd No.:"))
# sum= a+b
# product=a*b
# Average = sum/2
# print("Both numbers    ::"   ,a,"&",b)
# print("SUM             ::"   ,sum)
# print("product         ::"   ,product)
# print("Average         ::"   ,Average)


# # 2. WAP in “Python” language to accept basic, da , and hra from keyboard. Calculate total and display gross salary . 
# basic = float(input("Enter a basic salary: "))
# da = float(input("Enter a da salary: "))
# hra = float(input("Enter a hra salary: "))
# gross_salary = (basic + da + hra)
# print("The Total Gross Salary =",gross_salary)


# # 3. WAP in “Python” to accept total amount and currency type from keyboard and find out total no. of 
# # note in the specified currency. 

# total_note = int(input("Enter Total No.:"))
# cur_type = int(input("Enter Currency type as 20/10/20/50/100/200/500: "))
# t_note = total_note/cur_type
# print("Total Note:",t_note)


# #4. WAP in “Python” language to accept student registration number and marks obtained in physics, 
# # chemistry, and math papers. Each paper is of maximum 100 marks. Calculate and display the result 
# # in the following sequence and format: - 
# # ======================================== 
# # Registration No.       ::
# # ======================================== 
# # Marks Obtained in PHY  ::
# # Marks Obtained in CHE  ::
# # Marks Obtained in MATH :: 
# # ======================================== 
# # Total Marks Obtained   :: 
# # ======================================== 
# # Aggregate               ::
# # ========================================
# RegistrationNo = input("Enter a Registration No.:")
# phy = float(input("Enter a Marks Obtained PHY:"))
# che = float(input("Enter a Marks Obtained CHE:"))
# math = float(input("Enter a Marks Obtained MATH:"))
# total_Marks = (phy+che+math)
# aggregate = (total_Marks/300 * 100)
# print("=================================================")
# print("Registration No.       ::",    RegistrationNo     )
# print("=================================================")
# print("Marks Obtained in PHY  ::",    phy                )
# print("Marks Obtained in CHE  ::",    che                )
# print("Marks Obtained in MATH ::",    math               )
# print("=================================================")
# print("Total Marks Obtained   ::",    total_Marks        )
# print("=================================================")
# print("Aggregate              ::",    aggregate,"%"      )
# print("=================================================")



# # 5. WAP in “Python” language to accept item code, unit price and quantity taken. Calculate and print 
# # the bill in the following sequence and format, as 20% discount available on all items. 
# # ======================================== 
# # Item Code               :: 
# # ======================================== 
# # Unit Price in Rs.       :: 
# # Quantity Taken          :: 
# # ======================================== 
# # Total Amount in         :: 
# # Discount Amount         :: 
# # ======================================== 
# # Net Payable Amount      ::

# item_code = input("Enter a Item Code: ")
# unit_price= float(input("Enter Unit Price in Rs.: ")) 
# quantity_taken = int(input("Enter a Quantity Taken: "))
# total_amount = (unit_price * quantity_taken)
# total_Discount = (total_amount * 20 / 100)
# net_pay_amount = (total_amount-total_Discount)
# print("=============================================")
# print("Item Code            ::",   item_code)
# print("=============================================")
# print("Unit Price in Rs.    ::",   unit_price)
# print("Quantity Taken       ::",   quantity_taken)
# print("=============================================")
# print("Total Amount         ::",   total_amount)
# print("Total Discount       ::",   total_Discount)
# print("=============================================")
# print("Net Payable Amount   ::",   net_pay_amount)


# # 6. WAP in “Python” language to accept five digit no. from keyboard, calculate the sum of the digits 
# # of a given number and display the same on the screen. 

# a=int(input("Enter the five digit No.: "))
# d1= a % 10
# d2 = (a // 10) % 10
# d3 = (a // 100) %10
# d4 = (a // 1000) %10
# d5 = (a // 10000) %10
# digit_sum= (d1+d2+d3+d4+d5)
# print("the sum of the digits of a given number is :", digit_sum)



# # # 7. WAP in “Python” language to accept any five-digit number and print its reverse. 
# a=int(input("Enter the five digit No.: "))
# d1= a % 10
# d2 = (a // 10) % 10
# d3 = (a // 100) %10
# d4 = (a // 1000) %10
# d5 = (a // 10000) %10
# print("The reverse of five digit No.=",d1,d2,d3,d4,d5,sep="")

# 8. WAP in “Python” language to accept two number from keyboard and swap both to each other without 
# using third variable. 

# a=float(input("Enter a 1 no:"))
# b=float(input("Enter a 2 no :"))
# print("a=",a,",b=",b)
# a=a+b
# b=a-b
# a=a-b
# print("a=",a,",b=",b)

# # 9. WAP in “Python” language to accept kilometer from keyboard and convert it into meters. 
# Kilometer = float(input("Enter a Kalometer to conver in meeter: "))
# Meter = Kilometer*1000
# print("meter: ",Meter,"M")


# # 10. WAP in “Python” language to accept temperature of city in Fahrenheit degree then Convert this 
# # temperature into centigrade degrees. [Hint: c/100=(f-32)/180] 

# fr = float(input("Enter a Fahrenheit degree: "))
# centigrade = (fr - 32) * 5 / 9
# print("The centigrade degree is =", centigrade)

# 11. WAP in “Python” language to accept employee number and basic salary. Calculate dearness allowance 
# and house rent allowance @ 10% and 15% of basic salary respectively and display the salary details as 
# income tax is to be deducted @ 11% of gross salary. 

# emp_no = input("Enter Employee Number: ")
# basic_salary = int(input("Enter Basic Salary: "))

# da = basic_salary * 10 / 100          
# hra = basic_salary * 15 / 100        
# gross_salary = basic_salary + da + hra
# income_tax = gross_salary * 11 / 100  
# net_salary = gross_salary - income_tax

# print("\n-----------salary Details ------------------")
# print("Employee Number :", emp_no)
# print("Basic Salary in Rs :", basic_salary)
# print("Dearness Allowance (10%) :", da)
# print("House Rent Allowance (15%) :", hra)
# print("===============================================")
# print("Gross Salary    :", gross_salary)
# print("Income Tax (11%) :", income_tax)
# print("===============================================")
# print("Net Salary      :", net_salary)

# 12. WAP in “Python” language to accept the radius of a circle and calculate the circumference and area of 
# the circle and also display the same on the screen. 

# radius = float(input("Enter The Radius of circle: "))
# circumfrence = ( 2 *22/7 * radius )
# area = (22/7 * radius * radius)

# print("The circumference of circle : ",circumfrence)
# print("The Area of circle : ",area)

# # 13. WAP in “Python” language to accept the length and width of a rectangle and calculate its perimeter 
# # and area. Display the same on the screen. 

# length = float(input("Enter the length of rectangle : "))
# width = float(input("Enter the width of rectangle : "))

# p= length+width
# perim = 2*p

# print("The peremeter of rectangle is : ", perim)


# 14. WAP in “Python” language to accept an integer value of five-digits, calculate and display the 
# requirements as given below: - 
# First Line : <All Digits>
# Second Line: <All Except First Digit> 
# Third Line : <All Except First Two Digits> 
# ………………………………………………………………… 
# ………………………………………………………………… 
# Last Line   : <The Last Digit>

# n=int(input("Enter five digits no:"))
# print("First Line       ::",n)
# print("Second Line      ::",n%10000)
# print("Third Line       ::",n%1000)
# print("Fourth Line      ::",n%100)
# print("Last Line        ::",n%10)

