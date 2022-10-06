while True:
    n1 = int(input("enter first number : "))
    n2 = int(input("enter second number : "))
    n3 = int(input("enter third number : "))
    higher = 0
    if n1>n2:
        if n1>n3:
            higher = n1
        else:
            higher = n3
    elif n2>n3:
        higher = n2
    else:
        higher = n3
    value = higher
    while True:
        if higher%n1 == 0 and higher%n2 == 0 and higher%n3 == 0:
            print('LCM of {0},{1},{2} is {3}\n'.format(n1,n2,n3,higher))
            break
        else:
            higher=higher+value