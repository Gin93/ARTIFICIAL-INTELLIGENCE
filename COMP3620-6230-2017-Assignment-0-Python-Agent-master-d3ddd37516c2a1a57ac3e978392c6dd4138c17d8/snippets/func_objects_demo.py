#!/usr/bin/python3

def main() :

    def add(x,y):
       return x + y
    def sub(x,y):
       return x - y
    def apply(func, x, y):
       return func(x,y)

    print(apply(add,10,1))
    print(apply(sub,10,1))

    funcs = [add,sub]
    for x in funcs:
        print(apply(x,10,1))


if __name__ == '__main__' :
    main()
