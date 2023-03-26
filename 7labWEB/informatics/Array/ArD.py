a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
cnt = 0
for i in b:
    numbers.append(i)
for i in range(1,a):
    if numbers[i] > numbers[i-1]:
        cnt += 1
print(cnt)