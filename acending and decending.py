list = []
print("""
---this program arrange a set of numbers in a ACENDING and DECENDING order---

---if you are done entering press 0 to see results---
""")
while True:
    inp = int(input("enter a number : "))
    if inp==0:
        break
    else:
        list.append(inp)

def acending():
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i]=list[j]
                list[j]=temp
    print("Acending ->",list)

def decending():
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]<list[j]:
                temp = list[i]
                list[i]=list[j]
                list[j]=temp
    print("Decending ->",list)

print("Unordered -> ",list)
acending()
decending()

