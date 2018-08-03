

def greet_hello():
    return "Hello"

def greet_hi():
    return "hi"

def greet_good_morning():
    return "Good morning"

def greet_kamal(greeting):
    return greeting() + " " +"Kamal!"

if __name__ == "__main__":
    print greet_kamal(greet_hello)
    print greet_kamal(greet_good_morning)
    print greet_kamal(greet_hi)
