def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:
            high = mid - 1
        else:
            return mid

    return -1


list1 = [12, 24, 32, 39, 45, 50, 54, 89, 99, 75, 56]
print(list1)
n = int(input("enter number you want to search in given list : "))

result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("element is not present")