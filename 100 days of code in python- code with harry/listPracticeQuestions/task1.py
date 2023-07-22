myList = list(range(1, 11))  # inetialized form 0 to 10-1
# myList=list()

# print sum of all the elements of the list
# if len(myList)!=0:#sum if length of the list is not 0
#     print(sum(myList))
# else:
#     print("List is empty!!!")
# print(myList)

# print multiply all the elements of the list
# result=float(1)
# if len(myList)!=0:
#     for i in myList:
#         result*=float(i)
#     print(result)
# else:
#     print("List is empty!!!")

# print the largest numebr in the list
# largestElement=max(myList)
# print(largestElement)

# print the smallest numebr in the list
# smallestElement=min(myList)
# print(smallestElement)

#count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same
# myList2 = ['abc', 'xyz', 'aba', '1221']
# count=int(0)
# for i in myList2:
#     # print(i[0])
#     if i.endswith(i[0]):
#         count+=1
# print(count)

#get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# myList3=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(myList3)
# ValAtLastIndex=lambda x:x[-1]
# print(sorted(myList3,key=ValAtLastIndex))