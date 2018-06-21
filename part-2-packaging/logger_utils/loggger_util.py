import datetime


def log_time(f):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = f(*args, **kwargs)
        end_time = datetime.datetime.now()
        print ('time taken to run',f.__name__, (end_time-start_time))
        return result
    return wrapper

def log_input_output(f):
    def wrapper(*args, **kwargs):
        print ("input to the function is", args, kwargs)
        result = f(*args, **kwargs)
        print ("output of the function is", result)
        return result
    return wrapper
