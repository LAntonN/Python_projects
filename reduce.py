class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self): #https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]


score_total = 0 

for student in students:
    score_total += student.score

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total, students, 0)

#print(score_total / len(students))
#print(reduce_total / len(students))


# Challenge
# Use reduce to multiply all the number together

numbers = [1,2,3,4,5]

multiplication_total = reduce(lambda total,number:  number * total, numbers, numbers[0])
print(multiplication_total)
