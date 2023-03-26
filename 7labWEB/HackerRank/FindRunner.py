def maxnum(n,arr):
    l = []
    for i in arr:
        l.append(i)
    l.sort()
    l.reverse()
    for i in range(1,n):
        if l[i]!=l[0]:
            print(l[i])
            break


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maxnum(n,arr)