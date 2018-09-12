import sys

p = int(input("Enter p : "))
q = int(input("Enter q : "))
e = int(input("Enter e : "))


n = p*q
phi = (p-1)*(q-1)

if(e <= 1 or e >= phi):
    print("The range of e exceeds")

def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1
 
    if (m == 1) :
        return 0
 
    while (a > 1) :
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
 
    # Make x positive
    if (x < 0) :
        x = x + m0
 
    return x

def gcd(a,b):
    if (a == 0):
        return b
    return gcd(b%a, a)

if (gcd(phi,e) != 1):
    print("phi and e are not co-prime")
    sys.exit(1)

d = modInverse(e,phi)


print ("n = " + str(n))
print ("Private Key (d)= " + str(d))
print ("Public Key (e)= " + str(e))

