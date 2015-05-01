def FirstReverse(str): 

  # code goes here
  words = list(str)
  words.reverse()
  return ' '.join(words)
  text = "Code must be properly"
  more = " indented in Python!"
  return text + more 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input()) 

