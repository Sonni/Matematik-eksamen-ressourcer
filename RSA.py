__author__ = 'Sonni'

def encrypt(m, e_A, N_A):
    result = m**(e_A) % N_A
    print "$c=m^{e_A} (mod N_A)=" + str(m) + "^{" + str(e_A) + "} (mod " + str(N_A) + ")=" + str(result) + "$"
    print "\\\\Den krypterede besked er derfor " + str(result) + ".\\\\"
    return result

def decrypt(c, p, N_A):
    result = c**(p) % N_A
    print "$c=c^{p} (mod N_A)=" + str(c) + "^{" + str(p) + "} (mod " + str(N_A) + ")=" + str(result) + "$\\\\"
    print "Den orginale besked er derfor " + str(result) + ".\\\\"
    return result

def findPrivateKey(e_A, N_A):
    print "Det onskes at finde privatnoglen udfra den offentlignogle: " + str(e_A) + ", " + str(N_A) + "). \\\\"
    primeFactors = prime_factors(N_A)
    p = primeFactors[0]
    q = primeFactors[1]
    print "\\\\$n=" + str(N_A) + "$\\\\"
    print "$n=p*q$ hvor p og q er 2 primtal. Et script bruges nu til primtalsfaktorisering.\\\\"
    print "\\\\ \centerline{$p=" + str(p) + "$ og $q=" + str(q) + "$}\\\\"

    Z=(p-1)*(q-1)
    print "\\\\ $Z=phi(n)=(p-1)*(q-1)=(" + str(p) + "-1)*(" + str(q) + "-1)=" + str(Z) + "$\\\\"

    e = euclid(e_A, Z)
    privateKey = [e, N_A]
    print "\\\\Euklids udvidede algoritme bliver brugt til at finde privatnoglen udfra Z og $N_A$: (" + str(Z) + ", " + str(N_A) + ").\\\\"
    print "\\\\ Privatnoglen er derfor: (" + str(privateKey[0]) + ", " + str(privateKey[1]) + "). \\\\"
    return privateKey

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def euclid(d1, d0):
    s0 = 0
    s1 = 1
    t0 = 1
    t1 = 0
    n = 1
    d = d1

    while d > 0:
        n += 1
        q = d0/d1
        d = d0 % d1
        s = q*s1+s0
        t = q*t1+t0

        #Redefine
        s0 = s1
        s1 = s

        t0 = t1
        t1 = t

        d0 = d1
        d1 = d

    s = ((-1)**n) * s0 #Using s0 instead of s1, s is defined after calculations.
    t = ((-1)**(n-1))*t0#Using t0 instead of t1, t is defined after calculations.

    return s
print "Latex code:"
print "_____________________________"
encryptedMessage = encrypt(4, 3, 33)

privateKey = findPrivateKey(3, 33)

decrypt(encryptedMessage, privateKey[0], privateKey[1])
print "_____________________________"