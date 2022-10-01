myname = "burhan"
print(myname)


# function>> len()
# to find the length(number of characters ina string) of a string use the following funtion.
learning_about_string_related_functions_1 = "now we are going to learn about strings related functions."
print("1:", len(learning_about_string_related_functions_1))
b = "54"
print("2:", len(b))
c = "sdj"
print("3:", len(c))


# function>> capitalize()
# converts only the first character of the given string to upper case.
print("4:", learning_about_string_related_functions_1.capitalize())


# function>> casefold()
# Converts all the characters of the given string to lower case.
learning_about_string_related_functions_2 = "NOW WE ARE GOING TO LEARN ABOUT STRING RELATED FUNCTINOS>"
print("5:", learning_about_string_related_functions_2.casefold())


# function>> center(width,"any charcter")
# Returns a centered string.
# width>this is the numbers of  characters in which you want center your string"
# any charcter> this is the chrracter which will be at the side of your centered string. in python this is blank spaces by default.
# for example if you want to center you character b\t there character.
learning_about_string_related_functions_3 = "burhan"
print("6.1:", learning_about_string_related_functions_3.center(1))
# if you keep the width less then the number of characters in your string then it will just print the string as printed in vs-code line no1.this is the example below(vs-code line no26):
print("6.2:", learning_about_string_related_functions_3.center(5, "'"))
print("6.3:", learning_about_string_related_functions_3.center(10, "\U0001F49A"))
print("6.4:", learning_about_string_related_functions_3.center(50, "\U0001F49A"))


# function>> count()
# Returns the number of times a specified value occurs in a string.The character or the word you want to count in your desired string are written b\t these () perenthises.
print("7:", learning_about_string_related_functions_1.count("0"))
learning_about_string_related_functions_4 = "are,are,you,mad,mad,at,at,at,at,me,me,me,me,me"
print("7.1:", learning_about_string_related_functions_4.count("are"))
print("7.2:", learning_about_string_related_functions_4.count("you"))
print("7.3:", learning_about_string_related_functions_4.count("at"))
print("7.4:", learning_about_string_related_functions_4.count("me"))
print("7.5:", learning_about_string_related_functions_4.count("mad"))
print("7.6:", learning_about_string_related_functions_4.count(","))
# you can also gov it a starting and stopping character in your string of you want ot count the specific character b\t some characters.here value first after ',' is startting point and the value after second ',' is teh ending point.Note:Keep in mind the the index in python starts form 0 so the first charcter's number will be 0.
print("7.7:", learning_about_string_related_functions_1.count("l", 1, 15))
print("7.8:", learning_about_string_related_functions_1.count("a", 15, 20))
print("7.9:", learning_about_string_related_functions_4.count("mad", 15, 20))
print("7.10;", learning_about_string_related_functions_4.count("mad", 10, 20))
# if you write a bigger value first and smaller value after it,this will show 0 as the output because the string starts counting a character or word from left to right.
print("7.11:", learning_about_string_related_functions_1.count("e", 20, 0))


# function>> encode()
# there are manu types of encodings of data or strings in python, such as ascii,utf-8,utf-16 etc.
print("8;", learning_about_string_related_functions_1.encode(
    encoding='ascii', errors='strict'))
# i did not know how this works and how to used it.


# function>> endswith()
# Returns true if the string ends with the specified value
# the specific value should be written b\t ().
print("9.1:", learning_about_string_related_functions_1.endswith("today"))
print("9.2:", learning_about_string_related_functions_1.endswith("functions"))
print("9.3:", learning_about_string_related_functions_1.endswith("."))
# if you want to chack some of the characters and words then you can use this formate of this function
# endswith("sefix", starting point 'intigeral-positin', ending point 'intigeral-positin')
# the starting point and ending point are optionale.
# example:
print("9.4:", learning_about_string_related_functions_1.endswith(".", 4, 20))
print("9.5:", learning_about_string_related_functions_1.endswith(".", 57,))
print("9.6:", learning_about_string_related_functions_1.endswith(".", 0, 58))
# if you give the starting point value more then the number of characters in the string then it will always return false.
# if you leave the place of ending point value empity the it will consider it the maximum number of index of the string by default.Note:here the last character have the index value of 57.
print("9.7:", learning_about_string_related_functions_1.endswith(".", 58,))
print("9.8:", learning_about_string_related_functions_1.endswith(".", 70,))

# function>> expandtabs()
# this will increace(expand) or decrease(contract) the tab size.if you leave these () empity then the default size will be 8 tabs. the number specifie the size of the tab>> \t.
# the string must contain \t in it ,in order to use this funciton.\t can be used b\t character , words or sentances.
learning_about_string_related_functions_5 = "now\twe\tare\tgoing\tto\tlearn\tabout\tstrings\trelated\tfunctions."
print("10:", learning_about_string_related_functions_5.expandtabs())
print("10.1:", learning_about_string_related_functions_5.expandtabs(1))
print("10.2:", learning_about_string_related_functions_5.expandtabs(2))
print("10.3:", learning_about_string_related_functions_5.expandtabs(9))
print("10.4:", learning_about_string_related_functions_5.expandtabs(15))


# function>> find()
# it is used to search for a value in a string and give its position in return, the position will be the number of the index at which the value is prasent. the value can be any thing like characters,words or even sentences which are present in a string.
print("11:", learning_about_string_related_functions_1.find("we"))
print("11.1:", learning_about_string_related_functions_1.find("going"))
# we can also choose a starting and ending point by following this step:
print("11.2:", learning_about_string_related_functions_1.find("to", 0, 20))
# if your value is not present in the string or b\t the starting and ending point of the search the it will return -1.
print("11.3:", learning_about_string_related_functions_1.find("now", 4, 10))


# function>> formate()
# Formats specified values in a string.this means that it can be used as formate specifiers like we use in other languages like c, c++, etc. for example: %d, %f, %s, %c, etc.
# follow is teh way to use this finction:
learning_about_string_related_functions_6 = "now we are going to learn {} strings {} functions."
print("12:", learning_about_string_related_functions_6.format("about", "related"))
# or
ab = "about"
re = "related"
print("12.1:", learning_about_string_related_functions_6.format(ab, re))
print("12.1: this is {}".format(ab))
print("12.1: he is related to {}".format("me."))
