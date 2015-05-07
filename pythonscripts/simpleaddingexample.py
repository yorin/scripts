def SimpleAdding(num): 
  # code goes here
  #text = "Code must be properly"
  #more = " indented in Python!"
  #return text + more 
  #count = 1
  for i in range(1, num):
      num = i + num
      i += 1
  return num

# return (num * (num + 1)) / 2

#  sum = 0
#  
#  for n in range(1, num + 1):
#    sum += n
#    
#  return sum
    


# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleAdding(raw_input())  

