a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
for i in b:
    if i%2==0:
        print(i, end=" ")