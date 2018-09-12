def mod_pow(x,y,p):
    res = 1
    x = x % p

    while(y > 0):
        if((y & 1) == 1):
            res = (res * x) % p

        y = y >> 1
        x = (x*x)%p

    return res

n = int(input("Enter n : "))
c = int(input("Enter cipher text to decrypt : "))
m = int(input("Enter message to encrypt : "))

d = 1

while(mod_pow(c,d,n) != m):
    d = d+1

print(d)
