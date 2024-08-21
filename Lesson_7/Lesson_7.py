# ООП - объектно-ориентированное программирование


class Dogs:
    def __init__(self, color=None, age=None, name=None,
                 weight=None):
        self.color = color
        self.age = age
        self.name = name
        self.weight = weight

    def print_info(self):
        print(f"Dog {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Weight: {self.weight} kg")
        print(f"Color: {self.color}")

    @staticmethod
    def voice():
        print("Гав")


my_dog = Dogs("Brown", 3, "Шарик", 15)
my_dog.voice()
my_dog.print_info()


# Наследование классов
class A:
    def __init__(self):
        pass

    def method_1(self):
        pass

    def method_2(self):
        pass

    def method_3(self):
        pass


class B:
    def method_1_b(self):
        pass

    def method_2_b(self):
        pass

    def method_3_b(self):
        pass


class C(A, B):
    def __init__(self):
        super().__init__()
        self.method_1_b()
        self.method_2()

    def method_1_c(self):
        pass

    def method_2_c(self):
        pass

    def method_3_c(self):
        pass


c = C()
