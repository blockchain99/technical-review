'''
Created on Nov 29, 2016

@author: Gloria
'''
boolean = True
number = 1.1
string = "String can be declared with single or double quotes"
list = ["List can have", 1,2,3,4, "or more types together !"]
tuple = ("Tuple", "can have", 2, "elements !")
dictionary = {'one': 1, 'two': 2, 'three':3}
variable_with_zero_data = None
print "Printed !"
cake = "delicious"

#if 
def if_cake(cake_in):
    if cake == "delicious":
        return "Yes please !"
    elif cake == "okay":
        return "I'll have a small piece."
    else :
        return "No, thank you."
print if_cake(cake)

#loop 
for item in list:
    print "item :",item
total = 0
max_val =  10  
values = []
for i in xrange(20):
     values.append(i)
print "values:",values

i = 0
while (total < max_val):
    total += values[i]
    i += 2
    print "i",i, "values[",i,"] : ",values[i]
print "total :",total

print"\ndivide : "    
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder
print divide(568,23)

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r
calculate_stuff(568, 44)

#Classes
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
        

