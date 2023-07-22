userInput=input("Enter a file name: ")
fileNameParts=userInput.split('.')
print("Extention of the file is: .",end= fileNameParts[-1])