def gcd(*numbers):
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):   
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)


def calcLCM(*numbers):
    result = lcm(*numbers)
    print "Latex code:"
    print "\n__________________________"
    print "\centerline{$lcm" + str(numbers) + "$ er $" + str(result) + "$}\\\\"
    print "__________________________"

def calcLCM(*numbers):
    result = lcm(*numbers)
    print "Latex code:"
    print "\n__________________________"
    print "\centerline{$lcm" + str(numbers) + "$ er $" + str(result) + "$}\\\\"
    print "__________________________"


calcLCM(20, 30)
