a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
for i in b:
    numbers.append(i)
print(*numbers[::2])

