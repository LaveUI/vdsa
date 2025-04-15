a = 12
b = 24

print(f"Before swap: a = {a}, b = {b}")
a = a^b
b = a^b
a=a^b
print(f"After swap: a = {a}, b = {b}")