#!/usr/bin/python
import time

#Bubble Sort
changed = True 
passes = 0 
list = [9,4,6,8,1,3,2,5,7,0] 
print("Before: ",list) 

while changed == True:

    changed = False
    passes += 1
    print changed
    
    for i in range( len(list) - 1 ):
        print list[i]
        if list[i] > list[i+1]:
            print list[i]
            changed = True
            list[i], list[i+1] = list[i+1], list[i]
            print changed
            print list
            time.sleep(2)

print("After: ",list,"\ntook",passes,"passes")
