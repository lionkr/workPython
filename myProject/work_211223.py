list1 = []


class Node:
    def __init__(self, data):
        self.data = data


list1.append(Node(4))
list1.append(Node(1))
list1.append(Node(3))
list1.append(Node(6))
list1.append(Node(2))
#
#
# # list1.sort(key=lambda x: x.data)
# def pred(val:Node):
#     return val.data
#
# # list1.sort(key=pred)
# sortList1 = sorted(list1,key=pred)
#
# for i in sortList1:
#     print(i.data)
#
# # for i in list1:
# #     print(i.data)

list2 = [3, 6, 1, 8, 4, 2]

# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def binSearch(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid
#
#         elif target < arr[mid]:
#             right = mid - 1
#
#         elif target > arr[mid]:
#             left = mid + 1
#
#     return -1

list1.sort(key=lambda x: x.data)
for i in list1:
    print(i.data)


def binSearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid].data == target:
            return mid

        elif target < arr[mid].data:
            right = mid - 1

        elif target > arr[mid].data:
            left = mid + 1

    return -1


#
# res = sorted(list2)
# print(res)
# # print(binSearch(list3, 40))
# print(binSearch(res, 6))
#
# print(list2)

print(binSearch(list1, 3))
