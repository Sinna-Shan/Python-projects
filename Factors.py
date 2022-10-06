while True:
    number = int(input("Enter Your Number : "))
    x=1
    y=1
    while x<=int(number):
        if number%y==0 and number%number==0:
            if number%2==0 or number%3==0 or number%4==0 or number%5==0 or number%6==0 or number%9==0 or number%10==0:
                print(number / y)
            elif number/y==1 and number/number==1:
                print(number, "is a Prime number so there are no Factors")
        y+=1
        x+=1





