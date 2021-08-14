# Syntax of Function
# =================================

# def function_name(parameters):
#     '''
#     Document String (doc String)    
#     '''
#     statements

# Function without arguments
def welcome():
    '''
    this function greets to the person
    '''
    print('Hello Gulshan. Good Morning!')

#Calling Function 
welcome()
print(welcome.__doc__)

# Function without arguments
def welcome(name):
    '''
    this function greets to the person
    '''
    print(f'Hello {name}. Good Morning!')

welcome("Gulshan")
welcome("Gulshan")

def welcome(name, msg):
   '''
    this function greets to the person
    '''
   print(f'Hello {name}.{msg} !') 
welcome("Gulshan","Hello")
welcome("Gulshan","Hi")

# Python Arbitrary Arguments 

def welcome(*names) :
    for x in names :
        print(f'Hello {x}')

welcome('gulshan','rahman','tanny')


def addition(*nums) :
    sum=0
    for n in nums :
        sum=sum+n
    # print(sum)
    print(f'The Sum Is {sum}')
addition(5,10,15,20)
# addition(3+5+10+15+20)

# anonymus Functions are also called Lambda Functions
# syntax:
# functionName=lambda arguments: expression

# showDouble = lembda x:x*2
# def getDouble(x):
#     # print(x*2)
#     return x*2

# getDouble(5)
# print(getDouble(20))

showDouble = lambda x:x*2
print(f'The Double Value is : {showDouble(2)}')

def getDouble(x):
    # print(x*2)
    return x*2

# getDouble(5)
# print(getDouble(20))

myList=[1,5,4,6,8,11,3,12]
