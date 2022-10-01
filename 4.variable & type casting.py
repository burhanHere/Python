#
"""variable"""

# to make a variabelyou just write a variabel and the assign a value to it. the python interprator will automatically know about the type of the variable.for storing a string in a variabel "" are used the string will be stored between it. if you want to store an intiger or floting value the just write the value to after = of the variable.

burhan = "burhan"
print(burhan)
t = 9
print(t)
print("4455")
jf = 11
print(jf)
s = jf+t
mul = jf*t
minus = jf-t
dev = jf/t
print("sum=", s, "\nsubtrection", minus,
      "\nmultiplication", mul, "\ndevision", dev)
z = 456.9
print(z)
# you can perfrom arathematical operatins b\w intiger and float but not between string and intigers or string and floats.
print(z+jf)
# if you want to print a line multiple time the just write n* (number of time you want to do an action) before the string or the variable.
print(3*"this is line19\n")
print(2 * burhan)
# this will first solve the inner bracket the will multiply the value with 2 and will print the final value.
print(2*(t*jf))
# but if you want print the value of the two multiplying variable the you will use type casting. as below
print(4*str(int(t)*int(jf)))
# you can type cast into 3 types of variabels
# int() used for intigers
# str() used for strings
# float() used for floating point
"""giving input"""
# to give an input you use the input() function after the "name_of_variabel=" in which you want to store your value. the input value will be stored as a string.\
d = "Enter a value"
print(d)
f = input()
print("you entered ", f)
