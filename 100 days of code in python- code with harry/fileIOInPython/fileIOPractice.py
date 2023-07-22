# Write a Python program to read an entire text file.
# f=open("myText.txt",'r')
# f.read()
# print(fileText)

# Write a Python program to read first n lines of a file
# def countFilelines(fileNameHere):
#     counter = 0
#     with open(fileNameHere) as file:
#         for i in file:
#             if not (str(i) == ''):
#                 counter += 1
#     return int(counter)
# fileName = input("Enter the file name: ")
# fileLineCount = countFilelines(fileName)
# listOfLines = list()
# with open(fileName) as file:
#     while True:
#         numberOfLines = int(
#             input("Enter the number of lines you want to read: "))
#         try:
#             if numberOfLines > 0 and numberOfLines < fileLineCount:
#                 break
#         except:
#             print("Invalid Input!!!\n Try Again...")
#     while numberOfLines > 0:
#         listOfLines.append(file.readline())
#         numberOfLines -= 1
# print("File closed: ", file.closed)
# print(listOfLines)
# lengthOfList = len(listOfLines)
# while lengthOfList > 1:
#     listOfLines[0] += listOfLines[lengthOfList-1]
#     lengthOfList -= 1
#     listOfLines.pop()

# writting test to a file by creating the new file first
# with open("demo.txt", "x") as file:
#     for i in listOfLines:
#         file.write(i)
# print(listOfLines)

# Write a Python program to append text to a file and display the text
# with open("myText.txt","a") as file:
#     file.write("(Burhan ka text)")
# print(file.closed)

# Write a python program to find the longest words.
# fileDate = str()
# with open("myText2.txt") as file:
#     fileData = file.read()
# # print(fileData)
# # print("_____________________")
# fileData = fileData.split(" ")
# # print(fileData)
# # print("_____________________")
# for i in fileData:
#     if "\n" in i:
#         textIndex = fileData.index(i)
#         temp = i
#         fileData.remove(i)
#         temp = temp.split("\n")
#         for j in temp:
#             fileData.insert(textIndex, j)
#             textIndex += 1
# fileData = [i.replace(".", "")for i in fileData]
# # print(fileData)
# fileData = [i.replace(",", "")for i in fileData]
# # print(fileData)
# fileData = [i.replace("!", "")for i in fileData]
# # print(fileData)#formated the text of the file we converted the text into words then removed \n and some special characters from them. Now we have just english words in our list

# maxLengthWord=str()
# for i in fileData:
#     if len(maxLengthWord)<len(i):
#         maxLengthWord=i
# print(maxLengthWord," has length of ",len(maxLengthWord))

#count number of lines in a file
# linecount=0
# with open("myText.txt","r") as file:
#     while True:
#         fileData=file.readline()
#         if not(fileData==''):
#             linecount+=1
#         else:
#             break
# print("number of line in thhe file are: ", linecount)

# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. Go to the editor
# for i in range(ord('A'),ord('Z')):
#     file=open(f"{chr(i)}.txt","x")
#     file.close()#this code creates thesefiles
# import os#this code deletes the files
# for i in range(ord('A'),ord('Z')):
#     os.remove(f"{chr(i)}.txt")

#read a single character and print it
# with open("myText2.txt","r") as file:
#     print(file.read(1))