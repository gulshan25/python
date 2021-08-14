class Point:
    '''
    This is my point class
    '''
    def __init__(self, x, y) -> None:
        self.x, self.y = x,y 

    # def __repr__(self) -> str:    #Unambiguous __repr__
    #     return f'Point(x = {self.x}, y = {self.y})'

    def __str__(self) -> str:
            return f'Point(x = {self.x}, y = {self.y})'
        
    def __len__ (self):
        return self.x + self.y

    def get_Total(self):
        return sum([self.x, self.y])

P = Point(5, 7)
print(P) 
print(len(P))

print(P.get_Total())


# Recurssion = Function Call itself

# 3!=3*2*1
Num=7

def factorial(N):
     if N==0:
         return 1
     else:
         return N*factorial(N-1)

print(factorial(Num))

# Prime Number 

def checkPrime(num,i):
    if num==i:
        return 0
    else:
        if num%i==0:
            return 1
        else:
            return checkPrime(num,i+1)




# prime range

n=int(input('Enter Last value : '))
for x in range(2,n+1):
    if checkPrime(x)==0:
        print(x,end='\t')