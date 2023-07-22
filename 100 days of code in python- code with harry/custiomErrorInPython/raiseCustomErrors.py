a=input("Input a number of enter (quit) to exit: ")
if a!="quit":
    if a>'5' and a<'9':
        print("if block is working")
        raise ValueError("Invalid input...")
else:
    print("else block is working")    

