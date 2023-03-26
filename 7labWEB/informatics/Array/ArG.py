a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
cnt = 0
for i in b:
    numbers.append(i)
for i in range(0,a//2):
    cnt = numbers[i]
    numbers[i] = numbers[a-1-i]
    numbers[a-1-i] = cnt
print(*numbers)