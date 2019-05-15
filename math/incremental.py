

def find_max(nums):
 max_num = float("-inf") # smaller than all other numbers
 for num in nums:
     if num > max_num:
     # (Fill in the missing line here)
       max_num += 1
       print(max_num)
       return max_num
#print("hello")
#max_num2 = float("-inf") # smaller than all other numbers
#print(max_num2) 
print(find_max("hello"))