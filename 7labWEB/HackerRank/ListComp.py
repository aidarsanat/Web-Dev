def permutations(x,y,z,n):
    ans = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k)!=n:
                    ans.append([i,j,k])

    print(ans)
x = int(input())
y = int(input())
z = int(input())
n = int(input())
permutations(x,y,z,n)