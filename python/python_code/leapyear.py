# Accept a year from keyboard, check and display a message whether given year is leap year or not 
# leap year

year=int(input("Enter a year. :"))
if year%100==0:
    if year%400==0:
        print("Give year:",year," is leep year")
    else:
        print("Given year ",year," is not leep year.")
elif year%4==0:
    print("Given year ",year," is leep year")
else:
    print("Given year ",year," is not leep year")

