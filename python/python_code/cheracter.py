# Accept a character from keyboard, check and display a message whether given character is capital letter,
# small letter, digit or other character
ch=ord(input("Enter a character:"))
if ch>=65 and ch<=90:
    print("Capital letter")
elif ch>=97 and ch<=122:
    print("Small letter")
elif ch>=48 and ch<=57:
    print("Digits")
else:
    print("Other characters")

