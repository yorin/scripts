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

print LetterChanges(raw_input())
