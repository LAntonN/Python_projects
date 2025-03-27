class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students= [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sara", 0.38)] 

student_results = []
for student in students:
  #  if student.score >= 0.7:
   #     student_results.append(f"{student.name} Passed")
  #  else:
   #     student_results.append(f"{student.name} Failed")
    
    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed")

map_results = list(map(lambda student: student.name, students))


print(map_results)


numbers = [1,2,3,4,5]
map_multiplier = list(map(lambda number: number * 2, numbers))


print(map_multiplier)










#size = 2
#waist = 45

#if size < 10 and waist < 50:
##    print("good job!")

#elif size < 15 or waist > 50:
#    print("I do not know what I'm taking about")

#else:
#    print("this is hardware shop!")


#direction = input("Which direction? ").lower()


#match direction:
#    case "north":
#        print("Up")
# .  case "south":
#print("Down")
#    case "east":
 #       print("Right")
#    case "west":
#        print("Left")
##    case _:
#        print("it's not a valid ditection")

      #switch statment for numbers

# num = 4;

#match num: 
 # case  4:
#     print("your number is 3")
  
#  case _:
 #   print("not a valid number")