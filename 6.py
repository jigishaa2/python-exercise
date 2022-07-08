# s1 = {
# 	name: "sdad",
# 	age: "sd",
# 	...
# }

# s2 = {
# 	name: "sdadsdsa",
# 	...
# }
# ....
# ....


class Student:
	def __init__(self, name, age):
		self.name=name
		self.age=age
	def changeName(self, name):
		self.name = name

s1 = Student("jigi", "20")
# s2 = Student("abi", "50")

print(s1.name)
print(s1.age)

s1.changeName("jigiiii")

print(s1.name)
print(s1.age)

# print(s2.name)
# print(s2.age)
