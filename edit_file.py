#read

import numbers


#file = open("cheese.txt", "r")
#lines = file.readlines()
#file.close()

#edit
#lines = ["Hello\n", "We are editing the file here"]
#lines.insert(0, "cheese is the King\n")
#lines[1] = "hello cheese Head!\n"
#lines[-1] = lines[-1] + "\n"
#lines.append("Goodbye")

#write
#file = open("cheese.txt", "w")
#file.writelines(lines)
#file.close() 

#multiply nymbers by 2 and replace curreect ones with teh total. 
#read
file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

#edit
for x in range(len(lines)):
    try:
        number = float(lines[x]) * 2
        lines[x] = f"{number}\n"  # Update the line with the new value
    except Exception as e:
        pass
#write
file = open("numbers.txt", "w")
file.writelines(lines)
file.close()