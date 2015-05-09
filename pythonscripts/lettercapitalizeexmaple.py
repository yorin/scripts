def LetterCapitalize(str): 
  return str.title()

#  res = sen.split()	
#  res = [item.capitalize() for item in res]
#  res = " ".join(res)
#  return res

#  tmp = str.split(' ')
#  rtn = []
#  for line in tmp:
#    rtn.append(line[0].upper()+line[1:])
#    
#  return ' '.join(rtn)    

#   orig = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   new =  ' ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   result = ''
#   for i,c in enumerate(str):
#       if i == 0:
#           if c in orig:
#             c = new[orig.index(c)]
#             result += c
#       else:
#         result += c
#   return result

# for i, letter in enumerate(str):
#   if (ord(letter.lower()) >= 97) and (ord(letter.lower()) <= 122):
#      if str[i-1] != "+" or str[i+1] != "+" or i <1 or i> len(str)-2 : return "false"
#        
# return "true"

# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCapitalize(raw_input())           

