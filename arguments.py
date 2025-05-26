import sys


total = 1
for argument in sys.argv:
   try:
       number = float(argument)
       total *= number
   except Exception as e:
       print(e)
       print("only numbers Bitte!!")
       sys.exit(1)

print(total)