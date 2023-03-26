def my_pow(a,b):
    pow = 1
    while b != 0:
        pow*=a
        b-=1
    print(pow)
a, b = input().split()
my_pow(float(a),int(b))