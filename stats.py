from sys import argv
import random

script, filename = argv

#Defining some functions that we will use

#average(x) returns the average number in a set x
def average(x):
	return sum(x)/len(x)

#median(x) returns the median number in a set x
def median(x):
	n = len(x)
	if n % 2 == 0:
		mid_nums = [x[(n/2)-1],x[n/2]]
		return average(mid_nums)
	else:
		return x[n/2]

#skewness(x) returns a description of the skewness of the distribution of a set x
def skewness(x):
	return "left skewed" if average(x) < median(x) else "right skewed" if average(x) > median(x) else "symmetric" 

#min_max(x) returns the list (min(x),max(x)) containing the min and max values of a set x
def min_max(x):
	n = len(x)
	return x[0],x[n-1]
	
#score_one grades a user's answer to a given question, gives the user 2 extra tries if the answer is not correct, providing a hint on the last try
def score_one(q,a,ans,hint):
	points = 0
	if str(a) == ans:
		print "Correct!"
		points =+ 1
		return points
	else:
		print "Incorrect or improper format. Please try again:"
		print q
		a = raw_input(": ")
		if str(a) == ans:
			print "Correct!"
			points =+ 1
			return points
		else:
			print "Incorrect or improper format."
			print "You have one more attempt. Please try again."
			print hint
			print q
			a = raw_input(": ")
			if str(a) == ans:
				print "Correct!"
				points =+ 1
				return points
			else:
				print "Incorrect or improper format."
				print "No more tries. Sorry. Better luck next time."
				return points
					
					
#Introduce activity
print "We are going to simulate a sample of 50 integers between 1 and 100."
print "Then, we are going to calculate some statistics from the sample."
print "Finally, we will ask you some questions about this activity."
print "Your results will be stored in %r" % filename

#Empty input file (gives option to opt out)
print "First, let's empty the file %r so that we can start over fresh" % filename 

print "If you do NOT want to do empty the file, press CTRL-C  (^C)." 
print "If you DO want to empty the file, press RETURN."
raw_input("?")

print "Opening the file..."
target = open(filename, 'w') 

print "Emptying the file...."
target.truncate()

print "Let's start the activity. \n"

#Begin activity
for i in range(1,6):
	"We are going to do this activity %d more times. Take note of any patterns you observe in the summary statistics."
	print "Simulating 50 random integers between 1 and 100..."

	#Initializing (empty) list for our numbers to be stored:
	numbers = []

	for i in range(1,51):
		numbers.append(random.randint(1,100))

	#turn numbers into floats to allow for non-integer statistics
	numbers_fl = []
	for i in numbers:
		numbers_fl.append(float(i))
	
	#sort numbers to make stat calcs easier
	numbers_fl.sort()

	#print statistics:
	print "Here are some stats about the numbers generated: "

	print "The average number was %d" % average(numbers_fl)

	print "The distribution of the numbers is %s" % skewness(numbers_fl)

	print "The median (ie 'middle number') was %d" % median(numbers_fl)

	print "The minimum number was %d and the maximum was %d" % (min_max(numbers_fl)[0],min_max(numbers_fl)[1])

	print "The range of the numbers is %d" %(min_max(numbers_fl)[1]-min_max(numbers_fl)[0])
	print "Let's do this again \n \n"

#Introduce assessment
print "Now I'm going to ask you some questions to see what you have learned."
print "Don't worry- this isn't for a grade."
print "Your answers will be stored in the file %r." % filename

#Begin assessment 
name = raw_input('What is your name? ')
age = raw_input ('What is your age? ')
line1 = 'Name: %r \n age: %r' % (name, age)

q1 = 'What is the distribution of a set when the median is less than the average? Type "left skewed", "right skewed", or "symmetric".'
print q1
a1 = raw_input(': ')
ans_1 = "right skewed"
hint_1 = "Here is a hint: If the median of a set is 4 and the average is 6, the distribution is right skewed."
p1  = score_one(q1,a1,ans_1,hint_1)
print p1


q2 = 'What is the distribution of a set when the median is greater than the average? Type "left skewed", "right skewed", or "symmetric".'
print q2
a2 = raw_input (': ')
ans_2 = "left skewed"
hint_2 = "Here is a hint: If the median of a set is 8 and the mean is 7, the distribution is left skewed."
p2 = score_one(q2,a2,ans_2,hint_2)
print p2


q3 = 'What is the distribution of a set when the median is equal to the average? Type "left skewed", "right skewed", or "symmetric".'
print q3
a3 = raw_input(': ')
ans_3 = "symmetric"
hint_3 = "Here is a hint: Of the median of a set is 5 and the mean is 5, the distribution is symmetric."
p3 = score_one(q3,a3,ans_3,hint_3)
print p3

q4 = 'What is the range of a set that has a minimum of 2 and a maximum of 10? For your answer, just type the number.'
print q4
a4 = raw_input(': ')
ans_4 = "8"
hint_4 = "Here is a hint: The range of a set with a max of 15 and a min of 5 is 10."
p4 = score_one(q4,a4,ans_4,hint_4)
print p4
	
q5 = 'Did you enjoy this activity?'
print q5
a5 = raw_input(': ')
print "You suck." if (str(a5) == "no" or str(a5) == "No") else "Thank you for your feedback."

#Calculate score
your_score = 100*(p1+p2+p3+p4)/4
last_line = "Your score was %d." % your_score  #still rendering score as zero

#write answers to file
lines = [line1, q1, a1, q2, a2, q3, a3, q4, a4, q5, a5,last_line]
target.write("\n".join(lines))

#close file 
target.close()

#Closing remarks
print 'Thank you for participating today.'
print last_line  #tells you your score
print "Don't forget that your answers are stored in the file %r." % filename #reminds you where answers are stored
print 'I hope you learned a lot.'
print 'Goodbye!'

