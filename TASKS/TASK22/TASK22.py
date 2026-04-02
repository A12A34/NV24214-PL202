class car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)
c1 = car("Ford")
c1.show()