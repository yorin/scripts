def SimpleSymbols(str): 
    prev = ""
    in_cmp = False
    for ch in str:
        if ch.isalpha():
            if prev != "+":
                return 'false'
            in_cmp = True
        elif prev.isalpha():
            if ch != '+':
                return 'false'
            in_cmp = False
        prev = ch
    return 'false' if in_cmp else 'true'


#    letters = "abcdefghijklmnopqrstuvwxyz"
#
#    if str[0] in letters or str[-1] in letters:
#        return "false"
#
#    for n in range(1, len(str)-1):
#        if str[n] in letters and (str[n-1] != "+" or str[n+1] != "+"):
#            return "false"
#    
#    return "true"

#  if str[0].isalpha() or str[-1].isalpha():
#    return 'false'
#  for i in xrange(1, len(str)-1):
#    if str[i].isalpha() and (not str[i-1] == '+' or not str[i+1] == '+'):
#      return 'false'
#  return 'true'

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())  
