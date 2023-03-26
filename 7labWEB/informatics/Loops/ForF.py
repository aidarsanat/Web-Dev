b = int(input())
while(b%10 == 0): b//=10
while(b!=0):
    print(b%10,end="")
    b//=10