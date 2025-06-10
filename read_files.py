file = open("numbers.txt", "r")

#file_text = file.read()
#print(file_text)

#lines = file.readlines()
#print(lines)    
total = 1
for lines in file:
  number = float(lines.strip("/n"))  # Remove newline characters
  total *= number
print("The total is:", total)
# Close the file after reading

file.close()
# Alternatively, you can use a context manager to handle file opening and closing