def simpletwosum(arr,target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left,right]
        elif s < target:
            left +=1
        else:
            right -=1
    return []

print(simpletwosum([1,2,3,4,6],6))
