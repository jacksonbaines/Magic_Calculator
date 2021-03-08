# First go at a program, that also has a laugh :-)


import re

print("Our Magic Calculator")
print("Type 'quit' to exit\n\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))    
    if equation == 'quit':
        print("Goodbye Human")
        run = False
    elif equation == 'weed':
        print("Smoooke Weed Everyday!")
    elif equation == 'joke':
        print("A man walks into a bar, says to the bar staff\nwhats a gwaanin?")  
    elif equation == 'boobs':
        print('Press 8 0 0 8 5 on a calculator and hold it upside down\nbut not your computer')      
    else:
        #420
        equation = re.sub('[a-zA-Z,.:()""]', '', equation)

        if previous == 0:
            previous=eval(equation)
        else:
            previous = eval(str(previous) + equation)  
while run:
    performMath()