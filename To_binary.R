#This function converts nonnegative integers into binary strings 
#It stores the bits in a vector and prints the vector
#Be careful! This function does not apply to decimal numbers, fractions, or negative numbers.

to_binary<-function(x){ 
  bin = c() #initialize vector that will store the bits (0s or 1s)
  if(x==0){  #the first if chunk addresses the special case for 0, because the rest of the formula won't apply
    bin=append(bin,0) #the binary number for zero is also zero!
  } else {  #this chunk works for an integer greater than zero
     len=max(which(2^c(0:99)<=x))-1  #gets the number of bits for our binary number by finding the maximum power of 2 that does not exceed .
     for(i in c(len:0)){  #iterates backwards through the digits executing the code below
       val = ifelse(x/(2^i) >= 1, 1,0) #calculates the ith bit value (always a zero or a one)
       x = x%%(2^i) #gets remainder of the current (ith iteration) x value and the ith power of 2
       bin = append(bin,val) #tacks the bit value onto the vector
     }
  }
  print(bin) #prints the binary number (technically its a vector of bits)
}

#Let's test it out!
to_binary(25) #result: 11001 
to_binary(5) #result: 101
to_binary(0) #result: 0

#It seems to work!
