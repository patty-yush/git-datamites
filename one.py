def find_target(arr,target):
    for i in arr:
        if i==target:
            return True
    return False
print(find_target([1,2,3,4,5],3))