#This function takes an argument and returns 'even', 'odd', or 'neither' using the following:
	#if the number is divisible by 2, it is even
	#all other numbers are either non-integers or odd 
def even_or_odd(x):
	return 'even' if x % 2 == 0 else 'odd' if type(x) == int else 'neither'

#This function takes two numbers, adds them, applies the even_or_odd function, and prints statements
#about the results
def sum_even_or_odd(a,b):
	c = a + b
	print "%r is the sum of %r and %r" % (c, a, b)
	if c == int(c):
		print "%r is %s, %r is %s, and %d is %s." % (a, even_or_odd(a), b, even_or_odd(b), c, even_or_odd(c))
	else: 
		print "The sum is not an integer. \n"
	return c;

#Test it out:
sum_even_or_odd(7,9)     #it worked
sum_even_or_odd(6,4)     #it worked
sum_even_or_odd(5.4,2.6) #it worked

#NOTE: Does NOT work on strings
#sum_even_or_odd('sarah','john')<---- this led to an error
	
#This function takes two numbers, multiplies them, applies the even_or_odd function, and prints statements
#about the results	
def product_even_or_odd(a,b):
	c = a * b
	print "%r is the product of %r and %r" % (c, a, b)
	if c == int(c):
		print "%r is %s, %r is %s, and %d is %s." % (a, even_or_odd(a), b, even_or_odd(b), c, even_or_odd(c))
	else: 
		print "The product is not an integer. \n"
	return c;
	
#Test it out 
product_even_or_odd(-4,-3) #it worked
product_even_or_odd(5,5)   #it worked
product_even_or_odd(0,5)   #it worked


#NOTE: It only works on integers and floats!
#product_even_or_odd('sarah','john') #<---this led to an error


