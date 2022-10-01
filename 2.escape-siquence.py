# \t is escape siquence for giving space netween characters of 1 tab. + \n is new line escape siquence

print("this is line9\t", end="this is line10\n")

# \" or \' is used to put quotes in line

print("this is line11\'\t", end="this is line12\"")

# \a is used for ASCII Bell(bel)

print("\nthis is line13 \a")

# \b is used for ASCII backspace.it can't be used at the end of string.if in any case you want to use its in the end of a string the a space is compulsery after \b(as on line 23 of vs code).

print("this is line1\b4")

print("this is line14\b ")

print("this is \bline14")

# \f is used for forfeed.But this is giving this output(♀).

print("this is \f line15 \f")

# \v is used for verticall tab.But this is giving this output(♂).

print("this is \v line16 \\v")

# \ooo is used with a chracter to print it's octel value.here o represent a chracter so to use this we replave the Os with the desired chracters.here the octal value of \111 is I and vise versa. with these Os the maximum number of chracters which can be put in it are 3  how ever the chracter can also be less then 3 as in the examples below.

print("this is line17 \111")

print("this is line17 \261")

print("this is line17 \65")

print("this is line17 \2")

# \xhh  is used with a chracter to print it's hex value. here x remains but hh are replaced with the desired chracters. here value of \x68 is h.

print("this is line18 \x68")

print("this is line18 \x15")

print("this is line18 \x01")

print("this is line18 \x54")
