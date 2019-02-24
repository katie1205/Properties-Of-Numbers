import sys
import itertools
from sys import argv


script, filename = argv

print "We are going to do an activity to learn about the signs of the products of two real numbers."
print "You will be tested at the end of the activity and your answers will be stored in %r" % filename
print """
Specifically, you will explore: 
\t *the sign of product of two positive numbers
\t *the sign of the product of two negative numbers
\t *the sign of the product of a negative and a positive number
\t *the product of any number and zero
"""

print "First, let's empty the file %r so that we can start over fresh" % filename 

print "If you do NOT want to do empty the file, press CTRL-C  (^C)." 
print "If you DO want to empty the file, press RETURN."
raw_input("?")

print "Opening the file..."
target = open(filename, 'w') 
print "Emptying the file...."
target.truncate()

def sign(x):
	return 'positive' if x > 0 else 'negative' if x < 0 else 'zero'
	
print "Now let's begin the activity"
print "Lets determine the signs of 10 real numbers, their products, and their sums"
print "You will be prompted to enter numbers one at a time."
print "You must enter at least three positive numbers, at least three negative numbers, and one zero."
print "Aside from those constraints, you can choose whatever real numbers you want."
print "You may not enter letters, imaginary numbers, or any other characters. Only real numbers will work."

order = range(11)[1:11]

numbers = []

for i in order:
	while True:
		try:
			x = float(raw_input("Please enter a number: "))
			break
		except ValueError:
			print "Oops!  That was not a real number.  Try again..."
	numbers.append(x)


numbers_float = []
for number in numbers:
	numbers_float.append(float(number))
	
for number in numbers_float:
	print 'The sign of %d is %s' % (number, sign(number))
	
combos = list(itertools.combinations_with_replacement(numbers_float,2))

print 'There are %r different pairs of numbers' % len(combos)
print 'The sign of the product of each pair depends on the signs of both numbers in the pair'

products = []
signs_products = []
signs_pairs = []
for pair in combos:
	products.append(pair[0]*pair[1])
	signs_products.append(sign(pair[0]*pair[1]))
	signs_pairs.append(sign(pair[0])+' '+sign(pair[1]))
	print 'The sign of %r is %r, the sign of %r is %r, and the sign of their product, %r, is %r' % (pair[0],sign(pair[0]),pair[1],sign(pair[1]),pair[0]*pair[1],sign(pair[0]*pair[1]))


print 'You will now be asked some questions to see what you learned from this activity.'
print 'Your answers will be saved to the %r file' % filename
print "Don't worry; this is not for a grade! The purpose is to test the effectiveness of the activity."

prompt = ': '
name = raw_input('What is your name? ')
age = raw_input ('What is your age? ')
line1 = 'Name: %r \n age: %r' % (name, age)


q1 = 'What is the sign of the product of two positive numbers?'
print q1
a1 = raw_input(prompt)


q2 = 'What is the sign of the product of two negative numbers?'
print q2
a2 = raw_input (prompt)

q3 = 'What is the sign of the product of a positive and negative number?'
print q3
a3 = raw_input(prompt)

q4 = 'What is the product of any number and zero?'
print q4
a4 = raw_input(prompt)

q5 = 'Did you enjoy this activity?'
print q5
a5 = raw_input(prompt)

lines = [line1, q1, a1, q2, a2, q3, a3, q4, a4, q5, a5]
target.write("\n".join(lines))

target.close()

print 'Thank you for participating today.'
print 'I hope you learned a lot.'
print 'Goodbye!'

exit()









