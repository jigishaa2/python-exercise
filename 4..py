# file = "test.txt"
#
# cursor = open(file)
#
# ml=(cursor.readlines())
#
# j=input("type a number")
#
# for index, i in enumerate(ml):
#     # print(i)
#     i = i.split(" ")
#     if int(j) < int(i[1]):
#         print(i[0])


# TEXT FILE:
# A 25
# B 26
# C 27
# D 25
# E 25
# F 36
# G 40
# H 1
# I 29
# J 12



# j=input("type a number")
#
#
# for i in range(1,int(j)+1):
#     print(i*i)
# #print("%d" %a)



# file = "test.txt"
#
# cursor = open(file)
#
# R=(cursor.readline())
#
# R = R.split(" ")
# print(R)
# Ans=0
# for i in R:
#     Ans=int(i)+Ans
# print(Ans)

# TEXTFILE:
# 1 7 8 92 2 12 22


# file = "test.txt"
# cursor = open(file)
#
# ml=cursor.readlines()
# temp1=0
# temp2=0
# temp3=0
#
# for index, i in enumerate(ml): 
#     i=i.split()
#     if (i[1]) == "M":
#         temp1=temp1+1
#         # print(temp1)
#     elif (i[1]) == "F":
#         temp2=temp2+1
#         # print(temp2)
#     else:
#         temp3=temp3+1
#         # print(temp3)
# print(temp1)
# print(temp2)
# print(temp3)
#
# cursor.close()

#print no of M,F and N
# TEXTFILE:
# A M
# B M
# C M
# D F
# E N
# F F
# G M
# H N
# I F



# file="test.txt"
#
# cursor=open(file)
#
# ml=cursor.readlines()
#
# list1=[]
# list2=[]
# list3=[]
# for index, i in enumerate(ml):
#      i=i.split()
#      # print(i)
#      if (i[1] == "M"):
#          list1.append(i[0])
#          print(i[0])
#      elif (i[1] == "F"):
#          list2.append(i[0])
#          print(i[0])
#      else:
#          list3.append(i[0])
#          print(i[0])
# print(list1)
# print(list2)
# print(list3)

# TEXTFILE:
# A M
# B M
# C M
# D F
# E N
# F F
# G M
# H N
# I F








