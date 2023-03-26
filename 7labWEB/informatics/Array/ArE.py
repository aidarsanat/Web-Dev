a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
ok = False
for i in b:
    numbers.append(i)
for i in range(0,a-1):
    if (numbers[i] >= 0 and numbers[i+1] >= 0) or (numbers[i] < 0 and numbers[i+1] < 0):
        print("YES")
        ok = True
        break
if ok == False:
    print("NO")