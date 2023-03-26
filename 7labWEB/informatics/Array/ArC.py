a = int(input())
b = map(int, input().split(maxsplit=a))
cnt = 0
numbers = []
for i in b:
    if i > 0:
        cnt+=1

print(cnt)