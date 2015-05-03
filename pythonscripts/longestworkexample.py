def LongestWord(sen): 

  # code goes here
  longest = max(sen.split(), key=len)
  text = "Code must be properly"
  more = " indented in Python!"
  return longest
  return text + more 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())  

