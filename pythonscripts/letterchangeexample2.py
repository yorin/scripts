# define our method
def replace_all(text, dic):
      for i, j in dic.iteritems():
          text = text.replace(i, j)
      return text
 
# our text the replacement will take place
#my_text = 'Hello everybody.'
my_text = 'Argument goes here'
print my_text 
# our dictionary with our key:values.
# we want to replace 'H' with '|-|'
# 'e' with '3' and 'o' with '0'
#reps = {'H':'|-|', 'e':'3', 'o':'0'}
reps = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}
# bind the returned text of the method
# to a variable and print it
txt = replace_all(my_text, reps)
print txt    # it prints '|-|3ll0 3v3ryb0dy'
 
# of course we can print the result
# at once with:
# print replace_all(my_text, reps)

#longest = max(sen.split(), key=len)

for my_text2 in my_text:
    #print my_text2
  test = []
  dics = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}
  for iii, jjj in dics.items():
        my_text2 = my_text2.replace(iii, jjj, 1)
  #return my_text2
  print my_text2

#def LetterChanges(str):
#    return str.gsub('z', 'a').gsub(/[a-y]/) {|x| x.next!}.gsub(/[a,e,i,o,u]/) {|x| x.upcase!}   
#end
