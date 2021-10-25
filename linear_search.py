def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


number = [1,2,3,4,5,6,7,8,9,10]
linear_search(number, 9)