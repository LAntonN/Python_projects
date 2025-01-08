import random

guess = int(input('What is your guess?: '))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    print(guess)
    guess_count += 1
    if guess < correct_number:
        guess =  int(input("wrong. You need to guess Higher. What is your Guess: "))
    else: guess =  int(input("wrong. You need to guess Lower. What is your Guess: "))
    
    guess = int(input('What is your guess?: '))

print(f"you get it in {guess_count} tries it's {correct_number}")








###def hello(name):
###
##hello("Nick")
###def add_numbers(num1,num2):
    #print(num1+num2)

###add_numbers(4,5)

###ef dog_info(age, name):
###    print(f"The {name} is a dog and they are {age} years old!")


###dog_info(23, "steven")*/

##def return_string(strings):
    

###hi what you wjat from me 3
###return strings.upper()

##print(return_string("ffbnfsfhk"))

#user_text = input('Enter some Text...: ')
#user_responce = input('Enter 1 if you want to uppercase or 2 to lowercase: ')

#if int(user_responce) == 1:
  #  print(user_text.upper())

##if int(user_responce) == 2:
 #   print(user_text.lower())


