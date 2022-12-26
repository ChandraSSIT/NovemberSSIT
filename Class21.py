# Multiple Inheritance

print("//////Multiple Inheritance //////")
class father:
    def get_lands(self):
        print("My father earned lands")

class mother:
    def get_house(self):
        print("My mother earned house")

    def get_lands(self):
        print("My mother earned lands")


class child(father,mother):
    def get_lands(self):
        print("we sold it")
        super().get_lands()
        mother.get_lands(self)
        # father.get_lands(self)






obj = child()
obj.get_lands()
# obj.get_house()
# obj.get_car()

# class,object,abstraction,encapsulation,
# polymorphism(overloading ,overriding),Inhereitance(single,multi level,multiple)