# Your code goes here.
def has_remainder(num1, num2):
   remainder = num1 % num2
   if remainder == 0:
     return False
   else:
     return True

print(has_remainder(2,2))
print(has_remainder(5,9))