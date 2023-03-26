def my_func(l,st):
    ans = []
    l.sort()
    min = 0
    for i in range (1,len(l)):
        if l[i] != l[0]:
            min = l[i]
            break
    for i in range(0,len(st)):
        if st[i][1] == min:
            ans.append(st[i][0])
    ans.sort()
    for i in range(0,len(ans)):
        print(ans[i])


l = []
st = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append(score)
        st.append([name,score])

my_func(l,st)