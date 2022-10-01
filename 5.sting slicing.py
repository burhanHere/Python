# we are learing about string slicing
learning_about_string = "now we are going to learn about strings."
print("1.", learning_about_string)
# if you want to print or select (or what ever the situationis) a single character from the string then you should to as follow.Keep in mind the a string starts with 0 in python.
print("12.", learning_about_string[1])
print("13.", learning_about_string[0])
print("14.", learning_about_string[39])
# if you want to print or select (or what ever the situation is) some specific characters the doas follow.
# supppose that you want to print characters form 0 to 4,where 0 character is 'n' and 5 character is a 'e';Now then follow as done below.
# you have to write 6 insted of 5 because the last characrter is excluded when printed of selected (or what ever the situation is);however 0 is included while printing, selecting (or what ever the situation is).
print("15.", learning_about_string[0:6])
# now suppose in some case you want to print character while skipping some of the chracters the do as follow
# if you want to skip only one character then write 2 after the second colon.
b = 6  # you can also you variables as follow.
# here every 2nd character will be printed b/t 0 and value of b.
print("16.", learning_about_string[0:b:2])
# here the 7th character will be printed b/t 0 and 9.
print(learning_about_string[0:9:7])
# if you use negitive values  the the string's charcter count will start from the end of the string; as follw:
# the negitive values are used then the string starts from -1.So in this case the -1st character is '.'
print("17.", learning_about_string[-1:-9:-9])
# So in this case the - 2ndcharacter is '.'
print("18.", learning_about_string[-2:-9:-7])
# now of you leave the places b/t ':' empity ;then the first value will be considered 0 by default by python,the second value will be considered the maximum number of charcter of the string by default, and the third value will be niglected.
print("19.", learning_about_string[::])
# if you want it print the charcters of the string in reverse the you can follow this:
print("20.", learning_about_string[::-1])
# if you want to print the string in reverse but you also want to skip some characters the you can follow this:
print("21.", learning_about_string[::-2])
print("22.", learning_about_string[::-6])
print("23.", learning_about_string[::-13])
# of you try to print extra character the that of the characters present in a string the python will through an error.
# print(learning_about_string[148])
# but this can be done by a other way,as follow:
# here it will print all the characters which a string contains and the extra number out of 147 will be niglected.and will not through an error.
print("24.", learning_about_string[0:148])
