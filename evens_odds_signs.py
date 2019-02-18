def even_or_odd(x):
	return 'even' if x % 2 == 0 else 'odd'


p = 15
q = 16
g = 57

print even_or_odd(p)

print even_or_odd(7)

print even_or_odd(q + p * 2)

print 15 % 2

def sum_even_or_odd(a,b):
	c = a + b
	print "%d is the sum of %d and %d" % (c, a, b)
	print "%d is %s, %d is %s, so %d is %s. \n" % (a, even_or_odd(a), b, even_or_odd(b), c, even_or_odd(c))
	return c;

sum_even_or_odd(p,q)

sum_even_or_odd(g - q + 7, 2*p)

def sign(x):
	return 'positive' if x > 0 else 'zero' if x == 0 else 'negative' if x < 0 else 'not a real number'
	
sign(-1)

sign(5)

sign(0)

import math
i = math.sqrt(16)
print "The square root of 16 is %d, which is an %s and %s number. \n" % (i, even_or_odd(i), sign(i))

def product_even_or_odd(a,b):
	c = a * b
	print "%d is the product of %d and %d" % (c, a, b)
	print "%d is %s, %d is %s, so %d is %s. \n" % (a, even_or_odd(a), b, even_or_odd(b), c, even_or_odd(c))
	return c;
	
product_even_or_odd(p,q)
