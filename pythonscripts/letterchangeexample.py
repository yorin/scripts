#http://stackoverflow.com/questions/10956286/how-to-solve-this-python-puzzle-in-a-much-more-elegant-manner
#https://gomputor.wordpress.com/2008/09/27/search-replace-multiple-words-or-characters-with-python/
def LetterChanges(str):
    rv_str = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in str:
        if ord('a') <= ord(letter) and ord(letter) < ord('z'):
            ch_str = ord(letter) + 1
            if ch_str in map(ord, vowels):
                rv_str += chr(ch_str - 32)
            else:
                rv_str += chr(ch_str)
        elif letter == 'z':
            rv_str += 'A'
        else:
            rv_str += letter
    return rv_str

def LetterChanges2(str):
    orig = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = 'bcdEfghIjklmnOpqrstUvwxyzAbcdEfghIjklmnOpqrstUvwxyzA'
    capvowel = 'AEIOU'
    result = ''
    for c in str:
        if c in orig:
            c = new[orig.index(c)]
        result += c
    return result



#  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZA'
#  lower_chars = chars.lower()
#  vowels = 'aeiou'
#  result = ''
#  for char in str:
#    if char in chars:    
#      idx = chars.index(char)
#      result = result + chars[idx+1]
#    elif char in lower_chars:
#      idx = lower_chars.index(char)
#      new_char = lower_chars[idx+1]
#      if new_char in vowels:
#        new_char = new_char.upper()
#      result = result + new_char
#    else:
#      result = result + char
#      
#  
#  return result


#  next_str = ""
#  for c in _str:
#    if c.isalpha():
#      if c in ("z","Z"):
#        next_str += "a"
#      else:
#        next_str += chr(ord(c) + 1)
#    else:
#      next_str += c
#                
#  return "".join(map(lambda c: c.upper() if c in ("aeiou") else c, next_str))



print LetterChanges(raw_input())
print LetterChanges2(raw_input())
