import sys

def askNumber(bottom,top):
    print("Please enter a number between %d and %d : " % (bottom, top))


if __name__ == '__main__':
    print("Welcome to the Number Guessing Game!")
    if len(sys.argv) < 2:
        target = int(input("Please enter the target number : "))
    else:
        target = int(sys.argv[1])

    top = 10
    bottom = 1

    while 1:
        askNumber(bottom, top)

        ans = int(input())

        if ans > target:
            top = ans-1
        elif ans < target:
            bottom = ans+1
        else:
            print("Bingo!")
            break


