import calendar
x = calendar.TextCalendar()
choose = int(input("enter please the year you want to know the calendar of it:\n"))
print(x.pryear(choose))

print("#"*40)

print("Hi!")
name = input("What's your name? ")
print("It's nice to meet you,", name)
answer = input("Are you enjoying the course? ")
if answer == "Yes":
    print("That's good to hear!")
else:
    print("Oh no! That makes me sad!")
'''class family documentation'''
@staticmethod
class family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello():
        return f"Hello {name}!"

member1 = family("Hazem Yakout", 16)
member2 = family("Rana Yakout", 24 )
member3 = family("Ahmed Yakout", 26)
member4 = family("Eman Bassiony", 54)
member5 = family("Yakout Mohamed", 60)

class yakout(family):
   super().say_hello()


print(member1.name)
print("#"*40)
# dytime
from datetime import datetime
print(datetime(1999, 9, 8).now())
#your_birthday = input("enter your birth day date: ")
#print(f"you have {datetime(1999, 2, 4).now().date()-datetime(your_birthday).date()} years old, and your birthday is {your_birthday}")
print("           <3     <<<<happy new year>>>>      <3        ")
print("\"hazem yakout\"", sep="|")

print("                 Hello in 'HAZEM PROGRAM'                ")
while True:
 year = int(input("please enter your birth year:\n" ))
 answer = input("are you need your age by year or month or week or day or hour?\n")

 years = 2023-year
 if answer == "year":
    print(f'you have {years} years.')
 elif answer == "month":
    print(f"you have {years*12} months.")
 elif answer == "week":
    print(f"you have {years*12*4} weeks.")
 elif answer == "day":
    print(f"you have {years*12*4*7} days.")
 elif answer == "hour":
    print(f"you have {years*12*4*7*24} hours.")
 else:
    print("you have an error, please enter a correct answer.")
 choice = input("do you want to continue in hazem progrm (yes or no):\n")
 if choice == "no":
    break
print("program is exited")
print("^"*40)
y = input("is the shape square or rectangle ?\n").strip().lower()
if y == "square": 
 def square(side):
      h = input("do you want area or perimeter of square ?\n").strip().lower() 
      if h == "perimeter":
         print(side*4)
      elif h == "area":
         print(h*h)
elif y == "rectangle":
    def rectangle(length, width):
        h = input("do you want area or perimeter of square?\n").strip().lower() 
        if h == "perimeter":
           print((length+width)*2)
        elif h == "area":
           print(length*width)


         


