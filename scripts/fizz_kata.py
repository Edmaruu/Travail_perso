#def fizzbuzz(entier:int) -> str:
def fizzbuzz(entier) -> str:
    if not isinstance(entier,int):
        raise ValueError
    if entier % 3 == 0 and entier % 5 == 0:
        return "FizzBuzz"
    elif entier % 3 == 0:
        return "Fizz"
    elif entier % 5 == 0:
        return "Buzz"
    else:
        return str(entier)

