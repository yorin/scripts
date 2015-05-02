def FirstFactorial(num): 

  # code goes here
  factorial = 1
  for i in range(1,num + 1):
    factorial = factorial*i  
  return factorial
  text = "Code must be properly"
  more = " indented in Python!"
  return text + more 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
#print FirstFactorial(raw_input())  
print FirstFactorial(input())  

