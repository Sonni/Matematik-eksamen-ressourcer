__author__ = 'Sonni'

from fractions import gcd


def solve(a_n, m_n, interval):

    if not isRelativelyPrime(m_n):
        print "Ligningerne er ikke parvist indbyrdes primiske"
        exit()

    a_nString = []
    m_nString = []

    for i in range(len(a_n)):
        a_nString.append("$a_" + str(i) + "=" + str(a_n[i]) + "$ \\\\")
        m_nString.append("$m_" + str(i) + "=" + str(m_n[i]) + "$ \\\\")

    mString = "$m="
    for i in range(len(m_n)):
        mString += "m_" + str(i) + "\cdot "
    mString = mString[0:-6] + "="

    m = 1
    for i in range(len(m_n)):
        m *= m_n[i]
        mString += str(m_n[i]) + "\\cdot"
    mString = mString[0:-5] + "=" + str(m) + "$\\\\"
    print "m =", m

    M_n = []
    M_nString = []
    for i in range(len(m_n)):
        tmpString = "$M_" + str(i) + "=\\frac{m}{m_" + str(i) + "}=\\frac{" + str(m) + "}{" + str(m_n[i]) + "}=" + str(m/m_n[i]) + "$\\\\"
        M_nString.append(tmpString)
        M_n.append(m/m_n[i])

    print "M_n =", M_n

    y_k = []
    y_kString = []
    for i in range(len(m_n)):
        for y in range(m_n[i]):
            if (y * M_n[i]) % m_n[i] == 1:
                y_k.append(y)
                y_kString.append("$y_" + str(i) + "=" + str(y) + "$\\\\")
                break
    print "y_k =", y_k

    x = 0
    for i in range(len(m_n)):
        x += a_n[i] * m_n[i] * y_k[i]
    xString = "x=$\sum\limits_{i=0}^n(a_i\cdot M_i \cdot y_i)=" + str(x) + "$"
    print "x =", x
    print "___________________________"

    for i in range(len(a_nString)):
        print a_nString[i]
    print "\\\\"
    for i in range(len(m_nString)):
        print m_nString[i]
    print "\\\\"
    print mString
    print "\\\\"
    for i in range(len(M_nString)):
        print M_nString[i]
    print "\\\\"
    for i in range(len(y_kString)):
        print y_kString[i]
    print "\\\\"
    print xString,"\\\\"

    if interval[0] == 0 and interval[1] == 0:
        print "Fak"
        return True
    else:
        result = []
        result.append(x)
        tmpX = x
        while True:
            tmpX -= m
            if tmpX < interval[0]:
                break
            else:
                result.append(tmpX)

        tmpX = x
        while True:
            tmpX += m
            if tmpX > interval[1]:
                break
            else:
                result.append(tmpX)

        intervalString = "Kongruens-systemet har losningerne "

        for i in range(len(result)):
            intervalString += str(result[i]) + ", "
        intervalString = intervalString[0: -2]
        intervalString += " i intervallet " + str(interval[0]) + "-" + str(interval[1]) + "."
        print "\\\\", intervalString


def isRelativelyPrime(m_n):

    for x in range(len(m_n)):
        for y in range(len(m_n)):
            if gcd(m_n[x], m_n[y]) != 1 and x != y:
                print "gcd(" + str(m_n[x]) + ", " + str(m_n[y]) + ") er ikke 1."
                return False

    return True

result = 1
a_n = []
m_n = []

while result == 1:
    a = input("Enter a: ")
    m = input("Enter m: ")
    a_n.append(a)
    m_n.append(m)
    print "x =", a, "(mod " + str(m) + ")"

    result = input("Add more? (1/0): ")
    print ""
print "___________________________"
interval = raw_input("Interval (x-y   :   0-0 = intet interval): ")
interval = interval.split("-")
intervals = []
intervals.append(int(interval[0]))
intervals.append(int(interval[1]))

m = [2, 3, 5]
a = [1, 2, 3]
int = [0, 89]
solve(a_n, m_n, intervals)


