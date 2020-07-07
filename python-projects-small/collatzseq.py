#The Collatz Sequence aka the simplest impossible math problem

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
#Validation Loop         
while True:
    try:
        num = int(input('Enter number: '))
        while num != 1:
            num = collatz(num)
            print(num)
        if num == 1:
            break
    except ValueError:
        print('Please you must enter an integer.')
