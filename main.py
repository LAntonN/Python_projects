#size = 2
#waist = 45

#if size < 10 and waist < 50:
##    print("good job!")

#elif size < 15 or waist > 50:
#    print("I do not know what I'm taking about")

#else:
#    print("this is hardware shop!")


direction = input("Which direction? ").lower()


match direction:
    case "north":
        print("Up")

    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        pring("Left")
    case _:
        print("it's not a valid ditection")

      #switch statment for numbers

num = input("Provide a number: "):

match: 
    case num>0:
        print("yyour number is grated than Zero")
    case num<0:
        print("It's a minus mate")
    case _:
        pring("not a valid number")