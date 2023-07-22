class test:
    a=0
    _a2=0
    __a3=0

testing=test()
testing.a=2
print("testing.a",testing.a)
testing._a2=3
print("testing._a2",testing._a2)
testing.__a3=4# this make had added a new __a3 attribute to this class as a public attribute   
print("testing.__a3",testing.__a3)
print("______________________________")

class test2(test):
    pass

testing2=test2()
testing2.a=7
print("testing2.a",testing2.a)
print("testing.a",testing.a)
testing2._a2=8
print("testing2._a2",testing2._a2)
print("testing._a2",testing._a2)
testing2.__a3=3#not inharited because this is private in base class
#print(testing2.__a3)
print("End")