a=input("Enter Value For A : ")
b=input("Enter Value For B : ")

# Convert to Integer - int(var)
# Convert to Float - float(var)
# result=int(a) + int(b)

result=float(a) + float(b)
print(f"Addition is {result}")

result=float(a) - float(b)
print(f"Substraction is {result}")

result=float(a) * float(b)
print(f"Multiplication is {result}")
try:


    result=float(a) / float(b)
    print(f"Division is {result}")


    result=float(a) % float(b)
    print(f"Modulus is {result}")

    result=float(a) ** float(b)
    print(f"Exponent is {result}")
except:
    pass
print("==================================")


print("@"*5)

