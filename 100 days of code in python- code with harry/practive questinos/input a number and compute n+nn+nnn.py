#input a number and compute n+nn+nnn
instruction="Enter a number(1-9): ";
while True:
    try:
        userInput=input(instruction) 
        if len(userInput)==int(1):
            print("n+nn+nnn: ",int(n)+int(n+n)+int(n+n+n))
            break
        else:
            instruction="Invalid Input!!!\nTry again: "
    except:
        instruction="Invalid Input!!!\nTry again: "

