
# def duplicate(number):
#     return number * 2

# def triplicate(number):
#     return number * 3

# def quadruple(number):
#     return number * 4

def make_multiply(multiplicador):
    def multiply(numero):
        return numero * multiplicador
    return multiply


duplicate = make_multiply(2)
triplicate = make_multiply(3)
quadruple = make_multiply(4)

print(duplicate(2))
print(triplicate(3))
print(quadruple(4))
