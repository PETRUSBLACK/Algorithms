def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found @ index:", index)
    else:
        print("Target not found in list")



number = [1,2,3,4,5,6,7,8,9,10]
# linear_search(number, 9)

result = linear_search(number, 12)
verify(result)