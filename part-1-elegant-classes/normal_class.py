
class Number:
    def __init__(self, x=0):
        self.__x = x
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

if __name__ == "__main__":

    ## trying to print class
    n = Number()
    print "Class:", n 

    ## trying to compare with two classes (Normally it compares with the id)
    n1 = Number(20)
    n2 = Number(10)
    print "is ", n1, " == ", n2 , " ==> ", n1 == n2
    print "is ", n1, " >= ", n2 , " ==> ", n1 >= n2
    print "is ", n1, " <= ", n2 , " ==> ", n1 <= n2


    #converting to dict
    print "converting to dict", dict(n1)