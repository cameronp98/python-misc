import misc.say
from misc.fib import fib

def say_all():
    """Say all the things"""

    misc.say.foo()
    misc.say.bar()
    misc.say.baz()
    misc.say.yes()

def main():
    """ Run `say_all()` then print a 10-iteration fibonnaci sequence."""

    say_all()

    print(list(fib(10)))

if __name__ == "__main__":
    main()

