#pythonn scope resolutuon
def fun1():
    print(x)
x=10    
fun1()    
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()