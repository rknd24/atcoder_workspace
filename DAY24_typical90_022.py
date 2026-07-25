a,b,c = map(int,input().split())

def gcd(a,b):
    d = 1
    while d != 0:
        if a > b:
            a = a % b
            if a != 0:
                d = a
            else:
                d = b
                break
        elif b > a:
            b = b % a
            if b != 0:
                d = b
            else:
                d = a
                break
        else:
            d = a
            break
    return d

d_3 = gcd(c,gcd(a,b))
cutcount =((a+b+c)//d_3)-3
print(cutcount)

