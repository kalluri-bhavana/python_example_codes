def spam():
    eggs='spam local' #local variable
    print(eggs)

def bacon():
    eggs='bacon local' #local declaration
    print(eggs)
    spam()
    print(eggs)

eggs='global' #global variable
bacon()
print(eggs)

