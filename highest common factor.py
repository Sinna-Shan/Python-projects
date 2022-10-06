num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))
num3 = int(input("enter number 3 : "))
greatest=0
if num1>num2:
    if num1>num3:
        greatest = num1
    else:
        greatest = num3
elif num2>num3:
    greatest = num2
else:
    greatest = num3

for i in range(greatest,0,-1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        print("Highest common factor is ",i)
        break
