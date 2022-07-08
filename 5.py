

# st = "sssbbbbggggfddcffvvxssdfghjj" #count letters in string and print the count
#
# sum = [0]*26
# for i in st:
# sum[ord(i)-97] = sum[ord(i)-97]+1
# print(sum)


# st = "sssbbbbggggfddcffvvxssdfghjj"   #print non-repeating character in st2
#
# sum = [0]*26
# st2 = ""
#
# for i in st:
#     if sum[ord(i)-97]==0:
#         st2=st2+i
#         sum[ord(i)-97]=1
# print(st2)


# st = "ijbsadhbasjigidsjkndjksda" #remove repeating characters and print the rest
# pattern = "abi"
#
# if pattern in st:
#     print("True")
# else:
#     print("false")


# # SETS AND DICTIONARY
# jigi = {
#     "name": "jigi",
#     "age":30,
#     "height": 20
# }
#
# abi = {
#     "name": "abi",
#     "age":30,
#     "height": 120
# }

#
# se = {"apple", "orange","banana","pumpkin","apple","pumpkin"}
# print(se)

# database = [jigi,abi]
#
# def add(person):   #adds a person to the list
#     database.append(person)
# def remove(person):
#     database.remove(person)
# def update(person):
#     for i in database:
#        if  i["name"] == person["name"]:
#            i["age"] = person["age"]
#            i["height"] = person["height"]
#
# print(database)
#
# # add(abi)
# # remove(jigi)
# update({ "name": "jigi","age":25,"height": 20})
# print(database)
#

# set1 = ['apple', 'orange', 'banana', 'apple', 'banana', 'banana'] #if set1 elements not in set2, print the ! elements
# set2 = ['apple', 'banana' ]
# count=0
# for i in set1:
#         if i not in set2:
#             print(i)


# set1 = ['apple', 'orange', 'banana', 'apple', 'banana', 'banana']  #check set2 elements in set1 and print the count
# set2 = ['apple', 'banana' ]
# count=[0]*len(set2)
# for i in set1:
#     # print(count)
#     for index,j in enumerate(set2):
#         if j==i:
#             count[index]=count[index]+1
# print(count)

set1 = ['apple', 'orange', 'banana', 'apple', 'banana', 'banana']  #check set2 elements in set1 and print the count
set2 = ['apple', 'banana']




