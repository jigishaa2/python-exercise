# temp=0
# for i in range(1,9):
#     temp=temp+i
# print("sum is %d" %temp)




#
# fn=input("First name")
# mn=input("Middle name")
# ln=input("Last name")
#
# fn = fn.strip()      #removes the character in string; here no character is passed. so it removes the space and returns string.
# mn = mn.strip()
# ln = ln.strip()
#
# if mn=="":
#     print("%s%s" % (fn, ln))
# else:
#     print("%s%s%s" % (fn,mn,ln))



#
# name=input("Your fullname")
# name=name.split(" ")       # split- splits string and returns list
# while "" in name:
#     name.remove("")
# print(name)
# # name=name.strip()
# print("first name %s" %name[0])
# print("middle name %s" %name[1])
# print("last name %s" %name[2])



# file = "test.txt"
#
# cursor = open(file)
#
# print(cursor.readline())
#
# print(cursor.read())
#
# cursor.close()


#
# file = "test.txt"
#
# cursor = open(file)
#
# # print(cursor.readline())
#
# lines=cursor.readlines()
#
# for index, i in enumerate(lines):
#     i = i.split(" ")  # split- splits string and returns list
#     while "" in i:
#         i.remove("")
#     # print(i)
#     # print("first name %s" % i[0])
#     # print("middle name %s" % i[1])
#     # print("last name %s" % i[2].strip('\n'))
#     print("first name %s" %i[0].strip('\n'))
#     print("middle name %s" %i[1].strip('\n'))
#     print("last name %s" %i[2].strip('\n'))

# cursor.close()



# # st="jigishaa"
#
# file= "test.txt"
# cursor= open(file)
#
# n=cursor.write('jigishaa')
#
# cursor.close()
# print(n)


# st="abi"    #write string to the file
# text_file = open("test.txt", "w" )
# n = text_file.write(st)
# text_file.close()




# a_file = open("test.txt")
# file_contents = a_file.readlines()
# temp=1
# for l in file_contents:
#     if "int" in l:
#         # print(l)
#         n=l.split()
#         # len(n)
#         # print(len(n)-1)
#         # print(n[len(n)-1])
#         temp=temp*int(n[len(n)-1])
# print(temp)

# // abi
# // akdnla
# module start(
# int a = 2
# int b = 10
# ) stop

# #Multiply all int values in module and return the biggest value of all.
# a_file = open("test.txt")
# file_contents = a_file.readlines()
# temp=1
# com = 0
# for l in file_contents:
#     if "start" in l:
#         temp = 1    #temp takes value >1 in next loop. To avoid, we assign 1 to temp
#     if "int" in l:
#             n=l.split()
#             temp=temp*int(n[len(n)-1])
#     if "stop" in l:
#         if temp > com:
#             com = temp
# print(com)

# TEXTFILE
# // abi
# // akdnla
# module start(
# int a = 2
# int b = 10
# int c = 10
# ) stop
#
# module start(
# int a = 2
# int b = 1
# int c = 10
# int d = 6
# ) stop

