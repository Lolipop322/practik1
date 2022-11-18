a = int(input())
b = int(input())
c = int(input())
if a>=b:
    if a>=c:
        print("Max number:",a)
    else:
        print("Max number:",c)
else:
    if b>=c:
        print("Max number:",b)
    else:
        print("Max number:",c)