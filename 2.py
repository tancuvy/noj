a = int(input())
b = int(input())
c = input()
d = ['+','-','*','/','**','//','%']
if c in d :
    if c=='+':
        print(a, '+' ,b ,'=', a + b, sep='')
    elif c == '-':
        print(a, '-' ,b ,'=', a - b, sep='')
    elif c== '*':
        print(a, '*' ,b ,'=', a * b, sep='')
    elif c== '/':
        if b == 0:
            print("ERROR")
        else:
            print(a, '/' ,b ,'=', a / b, sep='')
    elif c == '**':
        print(a, '**' ,b ,'=', a ** b, sep='')
    elif c == '//':
        if b == 0:
            print("ERROR")
        else:
            print(a, '//' ,b ,'=', a // b, sep='')
    elif c == '%':
        if b == 0:
             print("ERROR")
        else:
            print(a, '%' ,b ,'=', a % b, sep='')
else:
    print("ERROR")