import attr

@attr.s
class Number(object):
    x =  attr.ib()

if __name__ == "__main__":
    n = Number(10)
    print n

    #comparing objects
    n1 = Number(20)
    n2 = Number(10)

    print "is ", n1, " == ", n2 , " ==> ", n1 == n2
    print "is ", n1, " >= ", n2 , " ==> ", n1 >= n2
    print "is ", n1, " <= ", n2 , " ==> ", n1 <= n2

    #converting to dict
    print "Converting to dict", attr.asdict(n1)