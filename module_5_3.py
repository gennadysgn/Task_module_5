class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print("Значение value должно быть типом int")
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print("Значение value должно быть типом int")
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
        else:
            print("Значение value должно быть типом int")
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# 1-й этап.

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# Вывод на консоль:

# Название: ЖК Эльбрус, количество этажей: 10
# Название: ЖК Акация, количество этажей: 20
# 10
# 20

# 2-й этап.

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10
print(h1)  # __iadd__

h2 = 10 + h2
print(h2)  # __radd__

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

# Вывод на консоль:

# Название: ЖК Эльбрус, количество этажей: 10
# Название: ЖК Акация, количество этажей: 20
# False
# Название: ЖК Эльбрус, количество этажей: 20
# True
# Название: ЖК Эльбрус, количество этажей: 30
# Название: ЖК Акация, количество этажей: 30
# False
# True
# False
# True
# False
