import datetime


def greet_hello():
    return "Hello"


def greet_good_morning():
    return "Good morning"


def greet_good_noon():
    return "Good noon"


def greet_good_evening():
    return "Good evening"


def time_based_greeting(function):

    hour = datetime.datetime.now().hour
    greeting_func = greet_hello
    if hour < 12:
        greeting_func = greet_good_morning
    elif hour < 15:
        greeting_func = greet_good_noon
    elif hour < 20:
        greeting_func = greet_good_evening

    print(datetime.datetime.time, datetime.datetime.now().hour)

    def wrapper(*args, **kwargs):
        print(function, args, kwargs)
        return function(*args, greeting_word=greeting_func, **kwargs)

    return wrapper


def greet_kamal(greeting_word=greet_hello):
    return greeting_word() + " " + "Kamal"


@time_based_greeting
def greet_by_name(name, greeting_word=greet_hello):
    return greeting_word() + " " + name


if __name__ == "__main__":
    # without decorator
    print(greet_kamal())

    # with decorator
    print(time_based_greeting(greet_kamal)())

    print(greet_by_name("Kannan"))

