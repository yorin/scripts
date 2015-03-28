#http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
class MyClass(object):
     i = 123
     def __init__(self):
         self.i = 345

a = MyClass()

print a.i
print MyClass.i
