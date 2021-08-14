sum=1+2+3+\
+4+5+6+7         
+8+9

print(sum)

# ============================
# How to Output Text
# ============================
# crtl+/ For single line comments

a=15                #int(integer)
b=5.5               #float
c=True               #boolean
d="Gulshan Rahman"  #str

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print((a))
print((b))
print((c))
print((d))

studentName="Gulshan Rahman"
studentAge=25

print(studentName,studentAge)
#Convert Number to String- str(Var)
print("My name is "+studentName + " And I am "+str(studentAge) +" Years Old ")
print("I am %s and I am %s years old" %(studentName,studentAge))
print("I am {0} and I am {1} years old".format(studentName,studentAge))
print("I am {studentName} and I am {studentAge} years old")


"""
fn=input("Enter Your First name : ")
ln=input("Enter Your Last name : ")
print(fn+ ' '+ln)
"""

x=input("Enter Value For X : ")
y=input("Enter Value For Y : ")

# Convert to Integer - int(var)
# Convert to Float - float(var)
# result=int(x) + int(y)

result=float(x) + float(y)
print(f"Addition is {result}")

result=float(x) - float(y)
print(f"Substraction is {result}")

result=float(x) * float(y)
print(f"Multiplication is {result}")
try:

    result=float(x) / float(y)
    print(f"Division is {result}")

    result=float(x) % float(y)
    print(f"Mdulus is {result}")


    result=float(x) ** float(y)
    print(f"Exponent is {result}")
except: 
    pass
print("========================================")


print("@"*100)

