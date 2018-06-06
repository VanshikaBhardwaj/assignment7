#1
def calArea(r):
    print("Area of sphere is:",4*22/7*r**2)
r=float(input("Enter radius of sphere"))
calArea(r)

#2
def perfect(n):
    sum=0
    for i in range (1,(n//2)+1):
        if(n%i==0):
            sum+=i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    per=perfect(i)
    if(per==True):
        print(i)

#3
def table(n):
    if(n==120):
        print (n)
        return
    else:
        print(n)
        return table(12+n)

table(12)

#4
def power(a,b):
    if(b==1):
        return a
    else:
        return a*power(a,b-1)
print("Enter base and exponent")
a=int(input())
b=int(input())
print(power(a,b))

#5
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print("Enter a number to calculate its factorial else enter -1 to stop looping!")
factDict={}
n=int(input())
while(n!=-1):
    factDict[n]=fact(n)
    n=int(input())
print(factDict)
