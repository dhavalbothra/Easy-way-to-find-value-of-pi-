# Easy-way-to-find-value-of-pi-
Hi this is a simple way to find value of pi
I have used the logic that if x=3+sin(3);x1=x+sin(x) if this process is continued till infinite this will give the value of pi
The precision of this procces roughly triples
Note that the sine used here is in radians.
But the problem is that through float we will find only 15 digits of pi but our target is to calculate 10000 digits of pi.
So I have used the Decimal library, through which I could find 10000 digits.
Here There are two options to use math library of sine or make our own method to find sine.
Here is the link of the formula i have used for sine https://www.mathsisfun.com/algebra/taylor-series.html.
The reason i have done this is that the math library is not very accurate.
Hope you like my repo.(Please star it !!)
