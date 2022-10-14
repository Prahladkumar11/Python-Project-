def calculator():
    print('======= CALCULATOR=========')
    c = int(input('Enter the no  for operation a:'))
    d = int(input('Enter the no for operation b:'))

    print('\n-----CHOOSE THE OPERATION TO PERFORM-----')
    cal(c,d)
    
    calculator()


def sum(a, b):
    a += b
    return a


def sub(a, b):
    a -= b
    return a


def mul(a, b):
    a *= b
    return a


def div(a, b):
    a //= b
    return a

def cal(c,d):
    print('1:Additon')
    print('2:Subtration')
    print('3:Multiplication')
    print('4:Division')
    print('5:exti')

    choice = int(input('>>>'))

    if choice == 1:
        s = sum(c, d)
        print('The sum of the no {} and {} is {}'.format(c, d, s))

    elif choice == 2:
        s = sub(c, d)
        print('The sub of the no {} and {} is {}'.format(c, d, s))
    elif choice == 3:
        s = mul(c, d)
        print('The mul of the no {} and {} is {}'.format(c, d, s))

    elif choice == 4:
        s = div(c, d)
        print('The div of the no {} and {} is {}'.format(c, d, s))

    elif choice==5:
        print('----Thanks you-------')
        return 0


calculator()
