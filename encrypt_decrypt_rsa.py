def mod_pow(x,y,p):
    res = 1
    x = x % p

    while(y > 0):
        if((y & 1) == 1):
            res = (res * x) % p

        y = y >> 1
        x = (x*x)%p

    return res

ch =  int(input("Enter choice \n1.Encrypt\n2.Decrypt : "))

if (ch == 1):
    m = int(input("Enter message to encrypt : "))
    e = int(input("Enter public key e : "))
    n = int(input("Enter n : "))
    print("Cipher text = " + str(mod_pow(m,e,n)))
else:
    c = int(input("Enter cipher text to decrypt : "))
    d = int(input("Enter private key d : "))
    n = int(input("Enter n : "))
    print("Decipher text = " + str(mod_pow(c,d,n)))

