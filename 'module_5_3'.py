class House:

    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

def __eq__(self,other):
    return self.number_of_floors==other.number_of_floors
print(h1==h2) #  возвращает False


def __lt__(self, other): # (<)
    return self.nFloors < other.nFloors

 def __le__(self, other): #(<=)
        return self.nFloors <= other.nFloors

def __gt__(self, other): #(>)
        return self.nFloors > other.nFloors

def __ge__(self, other): #(>=)
        return self.nFloors >= other.nFloors

def __ne__(self, other): #(!=)
        return self.nFloors != other.nFloors

def __add__(self, value):
        self.nFloors += value
        return self

def __iadd__(self, other):
        return self + other

def __radd__(self, other):
        return self + other


def main():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

