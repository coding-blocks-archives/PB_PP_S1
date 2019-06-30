import math
pi = math.pi

def square(x):
    return x**2

def circle(r):
    return pi*r**2

def rectange(a, b):
    return a*b

if __name__ == '__main__':
    import sys
    args = sys.argv
    if args[1] == 'circle':
        circle(int(args[2])))
    elif args[1] == 'square':
        square(int(args[2]))
    elif args[1] == 'rectange':
        rectangle(int(args[2]) , int(args[3]))
    else:
        print('This option is not supported.')
