num1 = 42 #variable declaration Primitive Numbers
num2 = 2.3 #variable declaration Primitive Numbers
boolean = True #variable declaration Primitive Boolean
string = 'Hello World' #variable declaration Primitive Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration Composite List  initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration Composite List Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration Composite Tuples initialize
print(type(fruit)) #log statement, access value composite tuple
print(pizza_toppings[1]) #log statement, access value composite list 
pizza_toppings.append('Mushrooms') #add value composite list 
print(person['name']) #access value composite list dictionary 
person['name'] = 'George' #change value composite list dictionary 
person['eye_color'] = 'blue' #change value composite list dictionary 
print(fruit[2]) #access value composite tuple

if num1 > 45: #conditional if
    print("It's greater") #
else: #conditional else
    print("It's lower") #

if len(string) < 5: #length check conditional 
    print("It's a short word!") #
elif len(string) > 15: #length check, conditional else if
    print("It's a long word!") #
else: # conditional 
    print("Just right!") #

for x in range(5): #for loop start
    print(x) #
for x in range(2,5): # 
    print(x) #
for x in range(2,10,3): #  
    print(x) #
x = 0 #
while(x < 5): # while loop start 
    print(x) #
    x += 1 #increment stop

pizza_toppings.pop() #
pizza_toppings.pop(1) #

print(person) #
person.pop('eye_color') #
print(person) #

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #
        continue #continue
    print('After 1st if statement') #
    if topping == 'Olives': #
        break #for loop stop break

def print_hello_ten_times(): #function 
    for num in range(10): #parameter
        print('Hello') #return

print_hello_ten_times()  #

def print_hello_x_times(x): #
    for num in range(x): #type check
        print('Hello') #

print_hello_x_times(4) #

def print_hello_x_or_ten_times(x = 10): #
    for num in range(x): #
        print('Hello') #

print_hello_x_or_ten_times() #
print_hello_x_or_ten_times(4) #


""" #comment multiline
Bonus section
"""

# print(num3)  #comment single line
# num3 = 72 #
# fruit[0] = 'cranberry' #
# print(person['favorite_team']) #
# print(pizza_toppings[7]) #
#   print(boolean) #
# fruit.append('raspberry') #
# fruit.pop(1) #