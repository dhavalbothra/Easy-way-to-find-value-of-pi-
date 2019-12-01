import time
from decimal import *

x=int(input("Enter no. of digits: "))
y=input("Enter name of file with .txt :")

getcontext().prec = x+1

pi=Decimal(3)
a=time.time()

def sin(x):
  
  sin=Decimal(0)
  i=Decimal(1)
  pw=x
  fact=Decimal(1)
  sign=Decimal(1)

  while i<3500:
    sin += sign*pw/fact
    i += Decimal(2)
    fact *= i*(i-1)
    pw *= Decimal(x**2)
    sign *= Decimal(-1)
  return sin

def pi():
  i = 1
  while(i < 50):
    pi += Decimal(sin(pi))
    i += 1
retrn(pi)

f = open(y, "w")
f.write(str(pi()))
f.close()

b=time.time()

print("Time took in seconds are:")
print(float(b-a))

s=input()
