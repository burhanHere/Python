# Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# add15=lambda a:a+15
# print(add15(10))
# mulXY=lambda x,y:x*y
# print(mulXY(10,15))

# sort a list
# myList=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print(myList)
# lastIndex=lambda a:a[-1]
# print(sorted(myList,key=lastIndex))

# Python program to sort a list of dictionaries using Lambda. Go to the editor Original list of dictionaries
# myList2=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# print(myList2)
# keyIndex=lambda x:int(x['model'])#sorted on the bases of model number of each dictionery
# print(sorted(myList2,key=keyIndex,reverse=True))

# Write a Python program to filter a list of integers using Lambda. Go to the editor Original list of integers:
# myList3= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list((filter(lambda a:a%2==0,myList3))))
# print(list((filter(lambda a:a%2!=0,myList3))))
# alternate
# myList3= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sorted(list(map(lambda a: a if a%2==0 else 0, myList3))))


# Write a Python program to square and cube every number in a given list of integers using Lambda.
# myList4=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda a:a**2,myList4)))
# print(list(map(lambda a:a**3,myList4)))

# Python program to find if a given string starts with a given character using Lambda
# myStr=str("Burhan")
# startsWith=lambda a,b:a[0]==b
# print(startsWith(myStr,'c'))
# print(startsWith(myStr,'b'))
# print(startsWith(myStr,'B'))

# Python program to extract year, month, date and time using Lambda.
# import datetime
# myDate=datetime.datetime.now()
# myYear=lambda a:a.year
# myMonth=lambda a:a.month
# myDay=lambda a:a.day
# myTime=lambda a:a.time()
# print(myYear(myDate))
# print(myMonth(myDate))
# print(myDay(myDate))
# print(myTime(myDate))

# Python program to check whether a given string is a number or not using Lambda
# def isString(a): return True if str(a) and (not (int(a) and float(b))) else False
# print(isString(int(456)))
# print(isString(456.65))
# print(isString("burhan"))

#Python program to find the intersection of two given arrays using Lambda
# myList5I=[1,2,3,4,5,6,7,8,9]
# myList5II=[1,2,3]
# intersect=lambda a,b:list(set(a).intersection(set(b)))
# print(intersect(myList5I,myList5II))

# Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
# myList6=[-1, 2, -3, 5, 7, 8, 9, -10]
# rearrange=lambda a:sorted(a)
# print(list(reversed(rearrange(myList6))))

#Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda
# myList7=["burhan","Monday","Friday","sana","zara","ali"]
# temp=list(map(lambda a:a if len(a)==6 else "None", myList7))
# while "None" in temp:
#     temp.remove("None")
# print(temp)
# or 
'''
map and filter a re almost same the take 2 argiment 1 is a fucntin and other is an iterable(list, arrar....)
then exicutes the fivern function in all the elements of the given iterable.
the difference is that the filter reduces the unnecessery data while the map does not. other that this there dunctionality is almost same.
'''
# myList7= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# myList7=list(filter(lambda a: a if len(a)==6 else '', myList7))
# print( myList7)
# myList7=list(map(lambda a: a if len(a)==6 else '', myList7))
# print( myList7)
