import math
cnt = 0
b = int(input())
for i in range(1, int(math.sqrt(b))):
    if b%i==0:
        cnt+=1
cnt*=2
if(math.sqrt(b) == int(math.sqrt(b))):
    cnt+=1
print(cnt)