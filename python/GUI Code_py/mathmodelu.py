import math as m
# print(m.floor(3.2))
# print(m.floor(3.8))
# print(m.floor(3.0))
# print(m.floor(-3.2))

# print(m.ceil(3.2))
# print(m.ceil(3.8))
# print(m.ceil(3.0))
# print(m.ceil(-3.2))

# print(round(3.2))
# print(round(3.8))
# print(round(3.0))
# print(round(-3.2))


# print(m.trunc(3.2))
# print(m.trunc(3.8))
# print(m.trunc(3.0))
# print(m.trunc(-3.2))
# print(m.trunc(-3.9))

# print(m.degrees(3))
# print(m.radians(171.88733853924697))

# print(m.exp(2))
# print(m.pow(2,3))

# print(m.factorial(4))
# print(m.fmod(5,2))
# print(5%2)
# print(m.fsum([12,5,6,2.5]))
# print(m.fabs(3.4))
# print(m.fabs(-3.4))
# print(m.fabs(-5))
# print(m.gcd(12,30))
# print(m.lcm(9,30))
# print(m.modf(3.7))
# print(m.modf(-3.7))
# print(m.prod([12,5,6,2.5]))
# print(m.remainder(5.5,2))
# print(m.fmod(5.5,2))
# print(m.sqrt(25))

import math as m

# ==============================
# 🔹 1. Rounding Functions
# ==============================

print("FLOOR")
print(m.floor(3.2))   # 3
print(m.floor(3.8))   # 3
print(m.floor(3.0))   # 3
print(m.floor(-3.2))  # -4

print("\nCEIL")
print(m.ceil(3.2))    # 4
print(m.ceil(3.8))    # 4
print(m.ceil(3.0))    # 3
print(m.ceil(-3.2))   # -3

print("\nROUND")
print(round(3.2))     # 3
print(round(3.8))     # 4
print(round(3.0))     # 3
print(round(-3.2))    # -3

print("\nTRUNC")
print(m.trunc(3.2))   # 3
print(m.trunc(3.8))   # 3
print(m.trunc(3.0))   # 3
print(m.trunc(-3.2))  # -3
print(m.trunc(-3.9))  # -3


# ==============================
# 🔹 2. Angle Conversion
# ==============================

print("\nANGLE CONVERSION")
print(m.degrees(3))                 # radians → degrees
print(m.radians(171.88733853924697))  # degrees → radians


# ==============================
# 🔹 3. Power & Exponential
# ==============================

print("\nPOWER & EXPONENTIAL")
print(m.exp(2))     # e^2
print(m.pow(2, 3))  # 2^3


# ==============================
# 🔹 4. Factorial
# ==============================

print("\nFACTORIAL")
print(m.factorial(4))   # 24


# ==============================
# 🔹 5. Modulus & Remainder
# ==============================

print("\nMODULUS & REMAINDER")
print(m.fmod(5, 2))   # float remainder
print(5 % 2)          # normal modulus

print(m.remainder(5.5, 2))  # IEEE remainder
print(m.fmod(5.5, 2))       # float remainder


# ==============================
# 🔹 6. Summation & Product
# ==============================

print("\nSUM & PRODUCT")
print(m.fsum([12, 5, 6, 2.5]))   # accurate sum
print(m.prod([12, 5, 6, 2.5]))   # product


# ==============================
# 🔹 7. Absolute Value
# ==============================

print("\nABSOLUTE VALUE")
print(m.fabs(3.4))
print(m.fabs(-3.4))
print(m.fabs(-5))


# ==============================
# 🔹 8. Number Theory
# ==============================

print("\nGCD & LCM")
print(m.gcd(12, 30))   # 6
print(m.lcm(9, 30))    # 90


# ==============================
# 🔹 9. Fractional & Integer Parts
# ==============================

print("\nMODF")
print(m.modf(3.7))    # (fraction, integer)
print(m.modf(-3.7))   # (fraction, integer)


# ==============================
# 🔹 10. Square Root
# ==============================

print("\nSQUARE ROOT")
print(m.sqrt(25))   # 5.0