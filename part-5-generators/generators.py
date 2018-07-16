from memory_profiler import profile


def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


## with xrange
@profile
def get_square_of_all(n):
    for i in xrange(n):
        print(i**2)

# with range not a generator function
@profile
def get_square_of_all_range(n):
    for i in range(n):
        print(i**2)


#generator function to function to return only even numbers
@profile
def get_even_number(n):
    i = 0
    while True:
        i += 2
        if i > n:
            return 
        else:
            yield i

@profile
def print_even_numbers(n):
    for i in get_even_number(n):
         x = i

#simple test generator function
def test_generator_func():
    yield "calling test_generator_func - 1"
    yield "calling test_generator_func - 2"
    yield "calling test_generator_func - 3"
    yield "calling test_generator_func - 4"
    yield "calling test_generator_func - 5"
    yield "calling test_generator_func - 6"


if __name__ == '__main__':
    my_func()
    get_square_of_all(10)
    get_square_of_all_range(10)
    print_even_numbers(10)   
    print_even_numbers(100000)    

    x  = test_generator_func()

    print (next(x))
    print (next(x))
    print (next(x))
    print (next(x))
    print (next(x))
    print (next(x))
    print (next(x))






