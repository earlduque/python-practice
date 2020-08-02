# collatz
import time

def collatz(user_input):
    if user_input % 2 == 0:
        return user_input / 2
    else:
        return user_input * 3 + 1

while True:
    print('Enter number:')
    try:
        x = int(input())
        tries = 0
        timer = 0.3
        while x != 1:
            x = collatz(x)
            print(int(x))
            time.sleep(timer)
            tries += 1
            if tries > 50:
                timer = 0.05
            elif tries > 10:
                timer = 0.15
        print('Completed after ' + str(tries) + ' tries.')
    except:
        print('Invalid input')