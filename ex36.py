#the collatz sequence

def collatz(number):
    if(number%2==0):
        x=number//2
    else:
        x=3*number+1
    print(x)
    return x

def main():
    try:
        number=int(input('enter number:  '))
        while number!=1:
            number=collatz(number)
    except valueError:
        print('enter a valid integer')


main()

