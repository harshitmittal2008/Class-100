class Car: 
    def _init_(self, color, company, model, howmanyseater, price):
        self.color = color
        self.company = company
        self.model = model
        self.howmanyseater = howmanyseater
        self.price = price

    def propertiesofcar(self):
        print ("Properties of my favorite car" + self.color, self.company, self.model, self.howmanyseater, self.price)

bugatti = Car("Orange", "Bugatti", "MDX-3012", 2, 1000000)
bugatti.propertiesofcar()

# # class Car(object):
# #   """
# #     blueprint for car
# #   """

# #   def __init__(self, model, color, company, speed_limit):
# #     self.color = color
# #     self.company = company
# #     self.speed_limit = speed_limit
# #     self.model = model

# #   def start(self):
# #     print("started")

# #   def stop(self):
# #     print("stopped")

# #   def accelarate(self):
# #     print("accelarating...")
# #     "accelarator functionality here"

# #   def change_gear(self, gear_type):
# #     print("gear changed")
# #     " gear related functionality here"


# # audi = Car("A6", "red", "audi", 80)

# # print(audi.stop())

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()
