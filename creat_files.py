#only creat4es the file if it does not exist
from os import write


file = open("cheese.txt", "x")

file.write("X marks the spot!")
file.close()
# The file is created in the current working directory

#to owerwrite the file

file = open("cheese.txt", "w")
file.write("For The W!")

file.close()
#append to the file
file = open("cheese.txt", "a")
file.write(" A+ work!")

file.close()