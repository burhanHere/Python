class a:
    def foo(self):
        print("a")
class b(a):
    def foo(self):
        print("b")
class c(a):
    def foo(self):
        print("c")
class d(c,b):
    pass
        
# diamind problem:
# python resolves this problem by using the attribute or functiuon of the class by which d was inharited first in this case c is inharited first so thed class  will use foo() of c if and only if class d donot have it's own 'over raided'foo() and vise versa...
if __name__=='__main__':
    myD=d()
    myD.foo()
    print("end")