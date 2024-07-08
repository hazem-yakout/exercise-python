from time import time
list_first = time()
list = ["hazem", "khaled", "osama"]
for x in list:
    print(x)
print(time()-list_first)

print("*"*42)
import random
print(random.randint(0,101))
print("#"*42)
def say_hello(name):
    print(f"hello {name}")
   
my_new_list = ["hazem", "khaled", "ahmed", "hazem"]
myResult = map(say_hello, my_new_list)
for x in myResult:
  print(x)


print(id("hazem"))
print(bin(22))
print(max(1, 2, 3, 4))
a = [8, 44, 6, 2]
print(sum(a, 30))
print(my_new_list.insert(0, "hassan"))
print(my_new_list)
from datetime import datetime
print(datetime.now().date())
my_birthday = datetime(2007, 8, 28).date()

print(f"happy birthday and your birthday is {my_birthday}")



print(7%2)

print("#"*40)
import termcolor
import pyfiglet
print(termcolor.colored("hazem", color="red"))


