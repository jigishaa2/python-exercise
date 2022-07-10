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



# class Student:
# 	def __init__(self, name, age):
# 		self.name=name
# 		self.age=age
# 	def changeName(self, name):
# 		self.name = name   #changes the previous name
# 	def doubleage(self):
# 		self.age = 2 * int(self.age)  #double the age and print
# s1 = Student("jigi", "20")
# s2 = Student("abi", "50")
#
# print(s1.name)
# print(s1.age)
#
# s1.changeName("jigiiii")
# s1.doubleage()
#
# print(s1.name)
# print(s1.age)

# print(s2.name)
# print(s2.age)

#double the age of s1; print age of s2 as such

class Student:
	def __init__(self, name, age):
		self.name=name
		self.age=age
		if age=="20":
			self.age = 2 * int(self.age)
		else:
			self.age=age

s1 = Student("jigi", "20")
s2 = Student("abi", "50")

print(s1.age)
print(s2.age)