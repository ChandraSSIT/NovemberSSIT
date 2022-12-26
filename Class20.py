# Single level
class Father:
    def getlands(self):
        print("get father lands")

    def get_house(self):
        print("get house")


class child(Father):
    # over riding
    def getlands(self):
        print("you child sold land")
        super().getlands()


obj = child()
obj.getlands()
obj.get_house()

# Multi level
class ourchild(child):
    pass

obj = ourchild()
obj.getlands()
obj.get_house()
