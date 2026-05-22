# import datetime as m
# p=m.datetime.now()
# print(p)
# # print(p.year)
# # print(p.day)
# # print(p.month)
# # print(p.second)

# print(p.strftime("%A"))

import datetime as m

# ==============================
# 🔹 1. Current Date & Time
# ==============================

p = m.datetime.now()

print("Current Date & Time:", p)

# Individual components
print("Year:", p.year)
print("Month:", p.month)
print("Day:", p.day)
print("Hour:", p.hour)
print("Minute:", p.minute)
print("Second:", p.second)


# ==============================
# 🔹 2. Basic strftime Usage
# ==============================

print("\nDAY NAME:", p.strftime("%A"))   # Full day name
print("SHORT DAY:", p.strftime("%a"))   # Short day name


# ==============================
# 🔹 3. COMPLETE strftime FORMAT CODES
# ==============================

print("\n--- STRFTIME ALL FORMATS ---")

print("%a :", p.strftime("%a"))   # Sun
print("%A :", p.strftime("%A"))   # Sunday

print("%w :", p.strftime("%w"))   # Weekday number (0=Sunday)
print("%d :", p.strftime("%d"))   # Day of month (01-31)

print("%b :", p.strftime("%b"))   # Jan
print("%B :", p.strftime("%B"))   # January

print("%m :", p.strftime("%m"))   # Month (01-12)

print("%y :", p.strftime("%y"))   # Year (short)
print("%Y :", p.strftime("%Y"))   # Year (full)

print("%H :", p.strftime("%H"))   # Hour (00-23)
print("%I :", p.strftime("%I"))   # Hour (01-12)

print("%p :", p.strftime("%p"))   # AM/PM

print("%M :", p.strftime("%M"))   # Minute
print("%S :", p.strftime("%S"))   # Second

print("%f :", p.strftime("%f"))   # Microseconds

print("%z :", p.strftime("%z"))   # UTC offset
print("%Z :", p.strftime("%Z"))   # Timezone name

print("%j :", p.strftime("%j"))   # Day of year (001-366)

print("%U :", p.strftime("%U"))   # Week number (Sunday start)
print("%W :", p.strftime("%W"))   # Week number (Monday start)

print("%c :", p.strftime("%c"))   # Full date & time
print("%x :", p.strftime("%x"))   # Date
print("%X :", p.strftime("%X"))   # Time

print("%% :", p.strftime("%%"))   # % symbol


# ==============================
# 🔹 4. Custom Formatting Examples
# ==============================

print("\n--- CUSTOM FORMATS ---")

print("Format 1:", p.strftime("%d/%m/%Y"))        # 03/04/2026
print("Format 2:", p.strftime("%A, %d %B %Y"))    # Friday, 03 April 2026
print("Format 3:", p.strftime("%I:%M %p"))        # 10:30 AM
print("Format 4:", p.strftime("%H:%M:%S"))        # 24-hour format
print("Format 5:", p.strftime("%d-%b-%Y"))        # 03-Apr-2026