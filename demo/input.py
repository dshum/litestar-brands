# name = input("Your name: ").strip().title()
# age = input("Your age: ").strip()
# height = input("Your height: ").strip()
#
# print(f"Your name is {name} and your age is {age} and your height is {height}")

class MyInt(int):
    def __str__(self):
        return f"My age is {self.__repr__()}"


age = MyInt(100)
print("Answer: " + str(age))
