def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello")
        fx(*args, **kwargs)
        print("Goodbye")
    return mfx
@greet
def welcome():
    print("Welcome to the world of Python programming!")
#greet(welcome)()

def add(a, b):
    print(a+b)
welcome()
greet(add)(5, 3)