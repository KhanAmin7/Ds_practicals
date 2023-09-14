# linear search and binary search
def linear_search(lst, el):
    for i in range(len(lst)):
        if el == lst[i]:
            return f"Element found at index {i}"
    return -1

def binary_search(lst, el, start, end):
    if start <= end:
        mid = (start + end) // 2
        if el == lst[mid]:
            return mid
        elif el < lst[mid]:
            return binary_search(lst, el, start, mid - 1)
        else:
            return binary_search(lst, el, mid + 1, end)
    else:
        return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = int(input("Enter the element you want to search for: "))
option = int(input("Please select the search option (1 for linear search, 2 for binary search): "))

if option == 1:
    print(linear_search(my_list, element))
elif option == 2:
    result = binary_search(my_list, element, 0, len(my_list) - 1)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")
else:
    print("Invalid option selected.")

