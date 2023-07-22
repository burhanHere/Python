instruction="Enter the radious: "
while True:#infinite loop to get a valid input until user enter a number (int or float) 
    radious=input(instruction)
    try:#try except blocj to convert the input ot a float if done successfully the loop will break else except bloak will exicute 
        radious=float(radious)
        print("Area of the circle: ",format(3.14*radious*radious,'.2f'))#formated the output upto 2 decimal point
        break
    except:
        instruction="Invalid input!!!\nEnter again: "

